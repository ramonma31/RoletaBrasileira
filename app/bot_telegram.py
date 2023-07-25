from settings import App_Settings
from telebot import TeleBot


class Init_telebot(TeleBot):
    def __init__(self, token, parse):
        super().__init__(
            token=token,
            parse_mode=parse,
            disable_web_page_preview=True
        )
        self.sett = App_Settings()

    def message(self, Text):
        self.send_message(self.sett.chat_id, Text)
