from os import system
from time import sleep

from click_generator import click_event
from info_screen import message_error, message_winner
from selenium.common.exceptions import (ElementNotSelectableException,
                                        ElementNotVisibleException,
                                        NoSuchElementException,
                                        TimeoutException)
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from settings import App_Settings


class Automatic_play:
    def __init__(self) -> None:
        # chrome_options = ChromeOptions()'
        self.set_up = App_Settings()
        options = Options()
        options.page_load_strategy = self.set_up.eager
        options.add_argument('--disable-extensions')
        # --> starta com a janela maximizada <-- #
        options.add_argument('--start-maximized')
        # -------------------------------------- #
        # ---> starta com a janela 2° plano <--- #
        # options.add_argument(self.set_up.headless) -> Descomentar para
        #                                               ocultar janela
        # -------------------------------------- #

        self.driver = Chrome(options=options)
        self.driver.get(
            self.set_up.url_rb
        )
        self.start()
        self.frame = 1

    @property
    def list_of_buttons_play(self) -> list[WebElement]:
        return self.numbers_play(self.driver)

    @property
    def less_time(self) -> WebDriverWait:
        """
        Hold property to create interaction with web elements.
        """
        return WebDriverWait(
            self.driver, timeout=500,
            poll_frequency=1,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
                NoSuchElementException
            ]
        )

    @property
    def long_time(self) -> WebDriverWait:
        """
        Hold property to create interaction with web elements.
        """
        return WebDriverWait(
            self.driver, timeout=12000,
            poll_frequency=1,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
                NoSuchElementException,
                TimeoutException
            ]
        )

    @property
    def average_time(self) -> WebDriverWait:
        """
        Hold property to create interaction with web elements.
        """
        return WebDriverWait(
            self.driver, timeout=1000,
            poll_frequency=1,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
                NoSuchElementException,
                TimeoutException
            ]
        )

    @property
    def server_time(self) -> str:
        return self.iframe_two(self.driver).find_element(
            By.CSS_SELECTOR, 'div.server-time'
        ).text

    @property
    def regulations_text(self) -> str:
        return self.iframe_two(self.driver).find_element(
            By.CSS_SELECTOR, 'div.regulations__text'
        ).text

    @property
    def status(self) -> str:
        """
        Returns the game state in string.
        """
        return self.iframe_two(self.driver).find_element(
            By.CSS_SELECTOR, '.fit-container__content--l2noR'
        ).text

    @property
    def title_game(self) -> str:
        """
        Returns the game title of the window.
        """
        return self.iframe_two(self.driver).find_element(
            By.CSS_SELECTOR, '.table-info__name--Wp_dB'
        ).text

    @property
    def time_game(self) -> WebElement:
        """
        Brazilian roulette time web element.
        """
        return self.iframe_two(self.driver).find_element(
            By.CSS_SELECTOR, '.round-timers'
        )

    @property
    def balance_value(self) -> float:
        """
        Petorna the value of Brazilian roulette bank.

        :return: float
        """
        return float(self.iframe_two(self.driver).find_element(
            By.CSS_SELECTOR,
            'div.balance__value'
        ).text.replace('R$', ''))

    @property
    def bet_value(self) -> float:
        bet_value = self.iframe_two(self.driver).find_element(
            By.CSS_SELECTOR, 'div.account-panel__value'
        ).text.replace('R$', '')
        return float(bet_value)

    @property
    def results(self) -> list[int]:
        '''
        Returns a list of the last roulette results int
        '''
        str_results = self.iframe_two(self.driver).find_element(
            By.CSS_SELECTOR, 'div.roulette-game-area__history-line'
        ).text.split()
        int_results = [int(x) for x in str_results]
        return int_results

    def keep_waiting(
            self, time: float | int, poll: float | int, function
    ) -> None:
        """
        Method to customize your waits for elements on the page.

        parameter: time -> float | int wait time in seconds.

        parameter: poll -> float | int frequency time per fetch in seconds.

        parameter: function -> Function that will
        receive the driver in question.
        """
        wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll)
        wait.until(function)
        return

    def user_name(self, driver: WebDriver) -> WebElement:
        """
        Email field web element to login to the blaze website.
        """
        return driver.find_element('name', 'username')

    def password(self, driver: WebDriver) -> WebElement:
        """
        Web element of the password field for logging into the blaze.
        """
        return driver.find_element('name', 'password')

    def button(self, driver: WebDriver) -> WebElement:
        """
        Web element of button for login on blaze.
        """
        return driver.find_element(
            By.CLASS_NAME, "submit"
        )

    # def real_mode(self, driver: WebDriver) -> WebElement:
    #     """
    #     Web element of button to switch from demo mode to real mode.
    #     """
    #     check_button = driver.find_element(
    #         By.XPATH,
    #         '//*[@id="slots-container"]/div[2]/div[2]/div[1]/div[1]/label/span'
    #     )
    #     return check_button

    def iframe(self, driver: WebDriver) -> WebElement:
        """
        iframe element of the element in question in case frame 1.
        """
        return driver.find_element(By.CSS_SELECTOR, 'iframe')

    def change_frame(
            self, driver: WebDriver,
            iframe: WebElement = None,
            previous_frame: bool = False
    ) -> WebElement:
        """
        Function responsible for changing frames, entering or leaving a frame.

        parameter: iframe: None -> pass the frame where we are.

        parameter: previous_frame: Boll ->
        default False -> move to frame 2 or higher.
        True -> go back one frame.
        """
        if previous_frame:
            self.frame = 1
            driver.switch_to.default_content()
            return
        driver.switch_to.frame(iframe)
        html = driver.find_element(By.TAG_NAME, 'html')
        self.frame = 2
        return html

    def iframe_two(self, driver: WebDriver) -> WebElement:
        """
        Function responsible for always keeping
        the driver in the Brazilian Roulette iframe.
        """
        if self.frame == 2:
            self.change_frame(driver, None, True)
        replace_iframe = self.change_frame(driver, self.iframe(driver))
        # body = self.body_iframe(replace_iframe)
        # div_root_iframe = self.div_id_root(body)
        return replace_iframe.find_element(By.CSS_SELECTOR, '#root')

    def game_chips(self) -> list[WebElement]:
        """
        Returns a list of web elements referring to the game's chips
        """
        return self.iframe_two(self.driver).find_elements(
            By.CSS_SELECTOR, 'div.arrow-slider__scrollable-content>svg'
        )

    def numbers_play(self, driver: WebDriver) -> list[WebElement]:
        """
        Function returns a list with the button elements,
        on the Brazilian roulette page.
        """
        try:
            # element = self.iframe_two(driver).find_elements(
            #     By.CSS_SELECTOR, '.with-size-wrapper'
            # )
            el1 = self.iframe_two(driver).find_elements(
                By.CSS_SELECTOR, 'div.with-size-wrapper'
            )[1].find_elements(
                By.CSS_SELECTOR, 'svg.roulette-digital-table--pIoRZ'
            )[0].find_elements(
                By.CSS_SELECTOR, 'g g.table-cell--Wz6uJ'
            )
            return el1

        except Exception:
            message_error('''
   Ocorreu um erro em seu aplicativo inesperado,
   erro ao pesquisar elementos da página.
                          ''', size=53)
            return

    def click_button(
            self,
            index: int | None,
            list_of_buttons: list | None
    ) -> None:
        """
        Function responsible for clicking on the number of the number panel
        """
        return list_of_buttons[index].click()

    def play_signal(
            self,
            list_of_buttons: list[WebElement],
            list_of_index: list[int],
    ) -> None:
        """
        Function responsible for clicking on all the numbers,
        at the same time making the move.
        """
        try:
            for x in click_event(list_of_index):
                list_of_buttons[x].click()
                message_winner(
                    f'Número {list_of_buttons[x].text} jogado com sucesso!'
                )
            return
        except Exception:
            system('cls')
            txt = self.iframe_two(self.driver).find_element(
                By.CSS_SELECTOR, 'div.default-modal-text--RCv5G'
            ).text

            self.box_alert(self.driver)

            message_error(text=txt)
            return

    def box_alert(self, driver: WebDriver) -> str:
        try:
            close = self.iframe_two(driver).find_element(
                    By.CSS_SELECTOR, 'div.modal-close-button--g76dn'
                )
            if close.is_displayed():
                close.click()
        except Exception:
            raise 'Erro ao carregar a pagina'

    def close_chat(self) -> None:
        self.iframe_two(self.driver).find_element(
            By.CSS_SELECTOR, 'div#close-chat'
        ).click()
        return

    def start(self) -> None:
        """
        Function responsible for logging into the blaze website,
        directly on the Brazilian roulette page.
        """
        user_name = self.average_time.until(self.user_name)
        user_name.send_keys(self.set_up.user_name)
        password = self.average_time.until(self.password)
        password.send_keys(self.set_up.password)
        click_entry = self.long_time.until(self.button)
        click_entry.click()
        # real_mode = self.long_time.until(self.real_mode)
        # real_mode.click()
        sleep(20)
        return


if __name__ == '__main__':

    a = Automatic_play()
    # list_of_buttons = a.numbers_play()
    # a.play_signal(a.numbers_play(a.driver), a.set_up.indexes_of_buttons)
    # 'FAÇA AS SUAS APOSTAS'
    # 'AGUARDE O INÍCIO DA PRÓXIMA JOGADA'
    # 'ÚLTIMAS APOSTAS'
