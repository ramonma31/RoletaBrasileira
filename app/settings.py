'''
App settings contain all passwords, commands, lists, parameters,
and additional settings that must not be modified by the user,
only if he has knowledge.
'''
import pendulum as time


class App_Settings:
    def __init__(self) -> None:
        # --INSERIR AQUI SEU PASSWORD E SENHA-- #
        self.__password: str = ''
        self.__user_name: str = ''
        # ------------------------------------- #
        # ---ISERIR AQUI SEU TOKEN E CHAT_ID--- #
        self.__token: str = ''
        self.__chat_id: str = ''
        # ------------------------------------- #
        # ---------------NÃO MODIFICAR  NENHUMA PROPIEDADE---------------- #
        self.__eager: str = 'eager'
        self.__headless: str = '--headless=new'
        self.__parse: str = 'html'
        self.__url_api: str = 'https://casino.betfair.com/api/tables-details'
        self.__url_rb: str = (
            'https://blaze.com/pt/games/roleta-brasileira/fun?modal=auth&tab=login'
        )
        self.__headers: dict[str, str] = {
            "cookie": "vid=210bec56-62f7-4616-939d-077cf4ff0f25"
        }
        # ---------------------------------------------------------------- #
        # -----LISTA DE NUMEROS DO PADRÃO----- #
        self.__list_one: list[int] = [
            2, 4, 6, 7, 12, 17, 18, 21, 22, 25, 27, 28, 29, 34
        ]

        # -----LISTA DE NÚMEROS A SEREM JOGADOS----- #
        self.__list_bet: list[int] = [
            1, 2, 5, 8, 9, 10, 11, 13, 14, 15, 16, 19,
            20, 23, 24, 26, 30, 31, 32, 33, 35, 36
        ]
        # --------------STICKER LOSS--------------- #
        self.__lose: str = (
            'CAACAgEAAxkBAAEJSXJkhm2UV4YM15Fc8qxS8q1L-uC8pAACFwIAAng1kUdAdid1ISufKy8E'
        )
        # --------------STICKER WIN--------------- #
        self.__winner: str = (
            'CAACAgEAAxkBAAEJSWpkhm2B3AABa4kd7U0AAQi7Vils1MANAAI8AgACMfeZR8QcG-o23geZLwQ'
        )
    # ------NÃO MODIFICAR EM IPOTESE ALGUMA------- #

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

# Por favor não mudar


RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;93m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


MARTINGALE_STEPS = 1  # -> Quantidade de gales do jogo

# ____CONSTANTES DE DATA E HORA DO PROGRAMA____ # 
TIME_ZONE = time.now().timezone_name
DATA = time.now(tz=TIME_ZONE).format('D/MM/YY')
HOUR = time.now(tz=TIME_ZONE).format('HH:mm:ss')
# --------------------------------------------- #

# DESCONSIDERAR SERVE APENAS PARA FINS DE TESTE #
if __name__ == '__main__':
    a = App_Settings()

    print(a.password)
# --------------------------------------------- #