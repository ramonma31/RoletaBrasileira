import sqlite3
from sqlite3 import Connection


class Data_base:
    def __init__(self, data_base) -> None:
        self._connect = sqlite3.connect(data_base)
        self._cursor = self._connect.cursor()

    @property
    def connect(self):
        return self._connect

    @property
    def cursor(self):
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

        for linha in self._cursor.fetchall():
            print(linha)

    def close_db(self):
        self.cursor.close()
        self.connect.close()


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