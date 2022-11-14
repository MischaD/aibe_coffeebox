from dataclasses import dataclass
import tkinter as tk


@dataclass
class User:
    id: int
    username: str = ''
    balance: float = 0.0
    consumed: float = 0.0
    paid: float = 0.0

    def calculate_debt(self, item_price):
        self.balance = self.balance - item_price
        self.consumed = self.consumed + item_price


class PopupNewUser(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('New User Data')
