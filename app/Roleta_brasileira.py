import re

from bot_telegram import Init_telebot
from info_screen import message_alert, message_info, message_winner
from settings import DATA, HOUR, MARTINGALE_STEPS, App_Settings
from templates import GENERATE_REPORT, SIGNAL_TEXT
from web_screaper import Automatic_play


class Roleta_brasileira(Init_telebot):
    def __init__(self, token, parse):
        super().__init__(token, parse)

        self.settings = App_Settings()
        self.automatic = Automatic_play()
        # ---Não modifique os valores--- #
        # -----Em hipótese alguma------- #
        self.signal: bool = False
        self.active_play: bool = False
        self.round_two: bool = False
        self.message_ID: int = 0
        self.entry: int = 0
        self.total_lost: int = 0
        self.total_winner: int = 0
        self.hits: int = 0
        self.accurate_shot: int = 0
        self.all_entries: int = 0
        self.last_result: int = 0

    @property
    def init_bank(self):
        return self.automatic.bet_value

    def info_screen(self):
        """
        Function to pass the values of the
        Brazilian roulette screen in the command prompt.
        """
        text = f'''GAME: {self.automatic.title_game.upper()}
   STATUS: {self.automatic.status}
   BANCA: {self.automatic.balace_value}
   RESULTADOS: {self.automatic.results}'''
        message_info(text=text, size=(len(self.automatic.results) * 5))

    def check_alert(self, data: list | None) -> None:
        """
        It checks the results of the assembled strategy,
        if the condition is satisfied,
        it sends the signal directly to the telegram.

        :parameter: -> data: pass the list of results to be compared.
        """
        if self.round_two:
            self.delete_message(
                self.settings.chat_id,
                self.message_ID
            )

        signal_colect = [x for x in data[0:2] if x in self.settings.list_one]

        if len(signal_colect) >= 2 or self.active_play:
            if self.signal:
                self.correction(data[0], self.settings.list_bet)
            else:
                self.active_play = True
                message_info(
                    text=f'''SAIU: {signal_colect}
   ULTIMO RESULTADO: {data[0]}
   APOSTAR: {self.settings.list_bet}''',
                    size=len(self.settings.list_bet) + 9
                )
                self.all_entries += 1
                self.send_signal(data[0])
                self.signal = True
            if not self.stopping_conditions(
                starting_bank_amount=self.init_bank,
                stopping_condition=15,
                banking_value=self.automatic.balance_value,
                amount_of_loss=self.total_lost,
            ):
                self.automatic.click_button(1, self.automatic.game_chips())
                self.automatic.play_signal(
                    self.automatic.list_of_buttons_play,
                    self.settings.indexes_of_buttons,
                )
        return

    def correction(
            self, last_result: int | None, list_bet: list | None
    ) -> None:
        """
        Corrects the result with the sign,
        checking if it was a first-time victory,
        or if you have to go to gale.

        parameter: last_result: -> list of results to be compared.
        parameter: list_bet: -> list of moves of the signal.
        """
        for num in list_bet:
            if last_result == num and not self.entry:
                message_winner(text='TIRO SECO')
                self.accurate_shot += 1
                self.winner()
                self.reset()
                return
            elif last_result == num and self.entry:
                message_winner(text=f'WIN NO GALE {self.entry}')
                self.winner()
                self.reset()
                return

        self.martingale()

    def lose(self) -> None:
        """
        Send the defeat signal to the bot on telegram,
        and increment another 1 in the defeats and reset the successes.
        """
        self.total_lost += 1
        self.send_sticker(
            self.settings.chat_id,
            self.settings.Stiker_lose
        )
        self.hits = 0
        self.generate_report()

    def winner(self) -> None:
        """
        Send the victory signal to the bot on telegram,
        and increase 1 more in successes and 1 more in general successes.
        """

        self.total_winner += 1
        self.hits += 1
        self.send_sticker(
            self.settings.chat_id,
            self.settings.winner
        )
        self.generate_report()

    def generate_report(self) -> None:
        """
        Send the bot's report to telegram, with percentage,
        number of hits in a row and number of hits at first, hits in general,
        and losses in general,
        such as date and time.
        """

        total = self.total_winner + self.total_lost
        hit_percentage = (
            (self.total_winner / total) * 100 if self.total_winner > 0
            else 0
        )
        self.message(
            self.text_format(hit_percentage)
        )

    def martingale(self) -> None:
        """
        Checks the gale of the move,
        and performs the necessary action to move,
        whether or not to play by doubling the value.
        """
        self.entry += 1

        if self.entry <= MARTINGALE_STEPS:
            self.message_ID = self.send_message(
                self.settings.chat_id,
                f'''🔁 <b>Entramos com a {self.entry}° proteção</b>"'''
            ).message_id
            self.round_two = True
            if not self.stopping_conditions(
                starting_bank_amount=self.init_bank,
                stopping_condition=15,
                banking_value=self.automatic.balance_value,
                amount_of_loss=self.total_lost,
            ):
                self.automatic.click_button(1, self.automatic.game_chips())
                self.automatic.play_signal(
                    self.automatic.list_of_buttons_play,
                    self.settings.indexes_of_buttons,
                )
        else:
            self.lose()
            self.reset()

    def send_signal(self, last_result: int | None) -> None:
        """
        Send the play signal, which numbers should be played,
        to telegram, with html text and link to enter the game.
        """
        self.message(
            f'''{SIGNAL_TEXT}
<b>{last_result}</b>'''
        )

    def reset(self) -> None:
        """
        Resets the control variables,
        on the time and results of the bot
        """
        self.round_two = False
        self.active_play = False
        self.signal = False
        self.entry = 0

    def stopping_conditions(
            self,
            starting_bank_amount: float | int,
            stopping_condition: float | int,
            banking_value: float | int,
            amount_of_loss: int,
    ):
        """
        Function responsible for orchestrating
        the stops of automatic plays
        """

        stopping_condition = (
            15 / starting_bank_amount
        ) * 100 if starting_bank_amount > 0 else 0
        if banking_value >= stopping_condition or amount_of_loss >= 2:
            message_alert('Chegamos ao fim das operaçoes por hoje...')
            return True
        else:
            return False

    def text_format(self, percentage: int | None) -> str:

        new_data = re.sub(r'data', f'{DATA}', GENERATE_REPORT)
        new_hora = re.sub(r'hour', f'{HOUR}', new_data)
        new_winner = re.sub(r'totalwinner', f'{self.total_winner}', new_hora)
        new_lose = re.sub(r'totallost', f'{self.total_lost}', new_winner)
        new_percentage = re.sub(
            r'hitpercentage', f'{percentage:.2f}', new_lose
        )
        new_acurrace = re.sub(
            r'accurateshot', f'{self.accurate_shot}', new_percentage
        )
        new_text = re.sub(r'hits', f'{self.hits}', new_acurrace)
        return new_text


if __name__ == '__main__':
    settings = App_Settings()
    bot = Roleta_brasileira(settings.token, settings.parse)
