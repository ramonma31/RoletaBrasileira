import os
from time import sleep

# from data_base import Data_base
from info_screen import message_alert, message_info
# from percentage_calculations import percentage_hits
from Roleta_brasileira import Roleta_brasileira
from settings import App_Settings

"""
Gerenciador de tarefas do bot aqui é onde a magica acontece.
"""
# __________DESCRIPTIONS__________ #
__author__ = "AutoDev"
__copyright__ = "@Autodev__"
__contact__ = "https://github.com/ramonma31"
__license__ = "MIT"
__version__ = "01.000"
__maintainer__ = "Ramon AUTODEV"
__status__ = "BETA"
# ________________________________ #


if __name__ == "__main__":
    message_info(text=f'''BOT INICIADO AGUARDANDO AS CONFIGUARÇÕES INICIAIS...
   AUTOR: {__author__}
   CONTATO: {__contact__}
   LICENÇA: {__license__}
   VERSÃO: {__version__}
   STATUS: {__status__}''', size=54)
    game_screen: bool = True
    please_wait: bool = False
    time_refresh: int = 0
    attempt_limit: int = 0

    set_up = App_Settings()
    bot = Roleta_brasileira(set_up.token, set_up.parse)
    message_id = bot.send_message(
        set_up.chat_id, bot.automatic.regulations_text
    ).message_id
    # bot.message(bot.automatic.server_time)
    message_info(bot.automatic.regulations_text)
    message_info(bot.automatic.server_time)

    while True:
        try:

            if bot.automatic.status == 'FAÇA AS SUAS APOSTAS' and game_screen:

                os.system('cls')
                game_screen = False
                please_wait = True
                bot.info_screen()
                bot.check_alert(bot.automatic.results)
                time_refresh += 1
                continue

            elif (
                bot.automatic.status == 'AGUARDE O INÍCIO DA PRÓXIMA JOGADA'
                ) and please_wait or (
                bot.automatic.status == 'NÃO HÁ MAIS APOSTAS'
                    ) and please_wait:
                try:
                    bot.delete_message(set_up.chat_id, message_id)
                except Exception:
                    pass
                os.system('cls')
                please_wait = False
                game_screen = True
                message_info(text=bot.automatic.status)

                if time_refresh >= 20:
                    time_refresh = 0
                    bot.automatic.driver.refresh()
                    message_alert("Updating the page please wait...")
                    sleep(15)
                    # bot.automatic.close_chat()
            else:
                continue
        except Exception:
            message_alert('Pagina carregando...')
            sleep(5)
            continue
