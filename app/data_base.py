import sqlite3
from sqlite3 import Connection, Cursor

from info_screen import message_info
from percentage_calculations import percentage_hits
from settings import DATA


class Data_base:
    def __init__(self, data_base) -> None:
        self._connect = sqlite3.connect(data_base)
        self._cursor = self._connect.cursor()

    @property
    def connect(self) -> Connection:
        return self._connect

    @property
    def cursor(self) -> Cursor:
        return self._cursor

    def insert_db(
            self,
            current_bank_value: float | int,
            total_bank_value: float | int,
            before_date: str,
            current_date: str,
            percentage_hits: float | int,
            total_wins: int,
            total_loss: int,
            win_of_the_day: int,
            loss_of_the_day: int,
    ):
        consulta = "INSERT INTO brazilian_roulette_dice (current_bank_value, total_bank_value, before_date, current_date, percentage_hits, total_wins, total_loss, win_of_the_day, loss_of_the_day) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(consulta, (
            current_bank_value,
            total_bank_value,
            before_date,
            current_date,
            percentage_hits,
            total_wins,
            total_loss,
            win_of_the_day,
            loss_of_the_day,
        ))
        self.connect.commit()

    def edit_db(
            self,
            current_bank_value: float | int,
            total_bank_value: float | int,
            before_date: str,
            current_date: str,
            percentage_hits: float | int,
            total_wins: int,
            total_loss: int,
            win_of_the_day: int,
            loss_of_the_day: int,
            id: int,
    ):
        consulta = "UPDATE OR IGNORE brazilian_roulette_dice SET current_bank_value=?, total_bank_value=?, before_date=?, current_date=?, percentage_hits=?, total_wins=?, total_loss=?, win_of_the_day=?, loss_of_the_day=? WHERE id=?"
        self.cursor.execute(consulta, (
            current_bank_value,
            total_bank_value,
            before_date,
            current_date,
            percentage_hits,
            total_wins,
            total_loss,
            win_of_the_day,
            loss_of_the_day,
            id,
        ))
        self.connect.commit()

    def list_db(self):
        self.cursor.execute('SELECT * FROM brazilian_roulette_dice')
        return self.cursor.fetchone()
        # for linha in self._cursor.fetchall():
        #     print(linha)

    def close_db(self):
        self.cursor.close()
        self.connect.close()

    def info_bot(self):
        b_t = 10.25
        b_at = 51.65
        w = 10
        ls = 1
        self.edit_db(
            b_at, b_t, DATA, DATA, percentage_hits(w, w + ls), w, ls, w, ls, 2
        )

        info = self.list_db()

        text = f'''   DATA BASE
      {DATA}
   TOTAL DE WINS: {info[6]}
   TOTAL DE LOSS: {info[7]}
   WINS DO DIA:   {info[8]}
   LOSS DO DIA:   {info[9]}
   ACERTOS:       {info[5]:.2f}%
   BANCA ATUAL: R${str(info[2]).replace('.', ',')}
   BANCA INICI: R${str(info[1]).replace('.', ',')}'''
        message_info(text=text, size=24)


if __name__ == '__main__':
    db = Data_base('data_base.db')

    # db.insert_db(
    #     current_bank_value=0.31,
    #     total_bank_value=0.31,
    #     before_date='25/07/2023',
    #     current_date='26/07/2023',
    #     percentage_hits=0.0,
    #     total_wins=0,
    #     total_loss=0,
    #     loss_of_the_day=0,
    #     win_of_the_day=0,
    # )
    db.list_db()