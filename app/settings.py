'''
App settings contain all passwords, commands, lists, parameters,
and additional settings that must not be modified by the user,
only if he has knowledge.
'''
import pendulum as time


class App_Settings:
    def __init__(self) -> None:
        # --INSERIR AQUI SEU PASSWORD E SENHA-- #
        self.__password = 'Qpzm1598753'
        self.__user_name = 'rafaelmoraes_jm@hotmail.com'
        # ------------------------------------- #
        # ---ISERIR AQUI SEU TOKEN E CHAT_ID--- #
        self.__token = '6011083439:AAHnLMBkhAy9RfHIla1WwxN6P6jtOrImKeI'
        self.__chat_id = '@imperio_sinais_gratis'
        # ------------------------------------- #
        # ---------------NÃO MODIFICAR  NENHUMA PROPIEDADE---------------- #
        self.__eager = 'eager'
        self.__headless = '--headless=new'
        self.__parse = 'html'
        self.__url_api = 'https://casino.betfair.com/api/tables-details'
        self.__url_rb = (
            'https://blaze.com/pt/games/roleta-brasileira/fun?modal=auth&tab=login'
        )
        self.__headers = {"cookie": "vid=210bec56-62f7-4616-939d-077cf4ff0f25"}
        # ---------------------------------------------------------------- #
        
        self.__list_one = [2, 4, 6, 7, 12, 17, 18, 21, 22, 25, 27, 28, 29, 34]
        self.__list_bet = [
            1, 2, 5, 8, 9, 10, 11, 13, 14, 15, 16, 19,
            20, 23, 24, 26, 30, 31, 32, 33, 35, 36
        ]
        self.__lose = (
            'CAACAgEAAxkBAAEJSXJkhm2UV4YM15Fc8qxS8q1L-uC8pAACFwIAAng1kUdAdid1ISufKy8E'
        )
        self.__winner = (
            'CAACAgEAAxkBAAEJSWpkhm2B3AABa4kd7U0AAQi7Vils1MANAAI8AgACMfeZR8QcG-o23geZLwQ'
        )

    @property
    def indexes_of_buttons(self) -> list[int]:
        indexes_of_buttons = [
            13, 14, 17, 20, 21, 22, 23, 25, 26, 27, 28, 31,
            32, 35, 36, 38, 42, 43, 44, 45, 47, 48
        ]
        return indexes_of_buttons

    @property
    def winner(self) -> str:
        return self.__winner

    @property
    def Stiker_lose(self) -> str:
        return self.__lose

    @property
    def password(self) -> str:
        return self.__password

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def headless(self) -> str:
        return self.__headless

    @property
    def token(self) -> str:
        return self.__token

    @property
    def chat_id(self) -> str:
        return self.__chat_id

    @property
    def parse(self) -> str:
        return self.__parse

    @property
    def url_api(self) -> str:
        return self.__url_api

    @property
    def url_rb(self) -> str:
        return self.__url_rb

    @property
    def headers(self) -> dict:
        return self.__headers

    @property
    def eager(self) -> str:
        return self.__eager

    @property
    def list_one(self) -> list:
        return self.__list_one

    @property
    def list_bet(self) -> list:
        return self.__list_bet


RED = "\033[1;31m"  
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;93m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


MARTINGALE_STEPS = 2

TIME_ZONE = time.now().timezone_name
DATA = time.now(tz=TIME_ZONE).format('D/MM/YY')
HOUR = time.now(tz=TIME_ZONE).format('HH:mm:ss')


if __name__ == '__main__':
    a = App_Settings()

    print(a.password)
