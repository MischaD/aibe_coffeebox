from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk
from VKeyboard import VKeyboard
from tkinter import messagebox


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

        self.new_user = WidgetNewUser(self)
        self.new_user.pack()
        VKeyboard(self, self.new_user.entry_name).pack()


class WidgetNewUser(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        vcmd = (self.register(self.validate_entry), '%d', '%s', '%S')
        self.svar_name = tk.StringVar()
        self.ivar_credit = tk.IntVar()

        self.label_name = ttk.Label(self,
                                    text='Name',
                                    background='lightblue',
                                    width=10)
        self.label_name.grid(row=0, column=0)

        self.entry_name = ttk.Entry(self,
                                    textvariable=self.svar_name,
                                    invalidcommand=self.is_invalid,
                                    validate='all',
                                    validatecommand=vcmd,
                                    width=20,
                                    takefocus=False)
        self.entry_name.grid(row=0, column=1)

        self.label_credit = ttk.Label(self,
                                      text='Credit',
                                      background='lightblue',
                                      width=10)
        self.label_credit.grid(row=1, column=0)

        self.entry_credit = ttk.Entry(self,
                                      textvariable=self.ivar_credit,
                                      invalidcommand=self.is_invalid,
                                      validate='all',
                                      validatecommand=vcmd,
                                      width=20,
                                      takefocus=False)
        self.entry_credit.grid(row=1, column=1)

    def validate_entry(self, reason, old_text, edit_text):
        if reason == '0':
            return True
        if reason == '1':
            return edit_text.isalpha() or edit_text.isspace()
        return True

    def is_invalid(self):
        messagebox.showerror("Error", "Only characters allowed!")

    def get(self):
        return self.entry_name.get()


if __name__ == "__main__":
    root = tk.Tk()
    PopupNewUser(root)
    root.mainloop()
