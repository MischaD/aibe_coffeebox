from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk
from VKeyboard import VKeyboard


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
        self.svar_name = tk.StringVar()
        self.LabelName = ttk.Label(self,
                                   text='Name',
                                   background='lightblue',
                                   width=10)
        self.LabelName.pack(side=tk.LEFT)
        validate_func = self.register(self.validate_entry)
        self.EntryName = ttk.Entry(self,
                                   textvariable=self.svar_name,
                                   invalidcommand=self.is_invalid,
                                   validate='all',
                                   validatecommand=(validate_func, '%d', '%s', '%S'),
                                   width=20)
        self.EntryName.pack(side=tk.RIGHT)

        VKeyboard(self)

    def is_invalid(self):
        print('invalid')

    def validate_entry(self, reason, old_text, edit_text):
        if reason == '0':
            print('Delete Text:', edit_text, 'from: ', old_text)
            return True
        if reason == '1':
            print('Insert Text:', edit_text, 'to: ', old_text)
            return edit_text in '0123456789'
        return True


if __name__ == "__main__":
    root = tk.Tk()
    PopupNewUser(root)
    root.mainloop()
