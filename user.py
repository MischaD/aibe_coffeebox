import tkinter
from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk
from VKeyboard import VKeyboard
from tkinter import messagebox
from decimal import Decimal, InvalidOperation
from ttkbootstrap import Style


@dataclass
class User:
    id: int = 0
    username: str = ''
    balance: float = 0.0
    consumed: float = 0.0
    paid: float = 0.0

    def calculate_debt(self, item_price):
        scaling_factor = 1
        if self.balance > 25.0:
            scaling_factor = 1.5
        elif self.balance > 50.0:
            scaling_factor = 2

        self.balance = round(self.balance - item_price*scaling_factor, 2)
        self.consumed = round(self.consumed + item_price*scaling_factor, 2)

    def pay_debt(self, amount):
        self.balance = round(self.balance + amount, 2)


class ValidatedMixin:
    """Adds a validation functionality to input"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        vcmd = self.register(self._validate)
        invcmd = self.register(self._invalid)

        self.configure(
            validate='all',
            validatecommand=(vcmd, '%P', '%s', '%S', '%V', '%i', '%d'),
            invalidcommand=(invcmd, '%P', '%s', '%S', '%V', '%i', '%d')
        )

    def _toggle_error(self, on=False):
        if on:
            self.configure(style='danger.TEntry')
        else:
            self.configure(style='primary.TEntry')

    def _validate(self, proposed, current, char, event, index, action):
        """The validation method.
        Don't override this, override _key_validate, and _focus_validate
        """
        self._toggle_error()
        valid = True

        if event == 'focusout':
            valid = self._focusout_validate(event=event)
        elif event == 'key':
            valid = self._key_validate(
                proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action
            )
        elif event == 'focusin':
            self.master.master.keyboard.change_target(self)

        return valid

    def _focusout_validate(self, **kwargs):
        """Will be overwritten in actual widget"""
        return True

    def _key_validate(self, **kwargs):
        """Will be overwritten in actual widget"""
        return True

    def _invalid(self, proposed, current, char, event, index, action):
        if event == 'focusout':
            self._focusout_invalid(event=event)
        elif event == 'key':
            self._key_invalid(
                proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action
            )

    def _focusout_invalid(self, **kwargs):
        """Handle invalid data on a focus event"""
        self._toggle_error(True)

    def _key_invalid(self, **kwargs):
        """Handle invalid data on a key event. By default, we want to do nothing"""
        pass


class ValidatedNumEntry(ValidatedMixin, ttk.Entry):
    """An Entry that only accepts numbers with 2 decimals"""

    def _key_validate(self, char, index, current, proposed, action, **kwargs):
        if action == '0':
            return True

        precision = -2

        # First, filter out obviously invalid keystrokes
        if any([
            (char not in '-1234567890.'),
            (char == '-' and index != '0'),
            (char == '.' and '.' in current)
        ]):
            Error("Only numbers allowed!")
            return False

        # At this point, proposed is either '-', '.', '-.',
        # or a valid Decimal string
        if proposed in '-.':
            return True

        # Proposed is a valid Decimal string
        # convert to Decimal and check more:
        proposed = Decimal(proposed)
        proposed_precision = proposed.as_tuple().exponent

        if proposed_precision < precision:
            return False

        return True

    def _focusout_validate(self, **kwargs):

        value = self.get()
        try:
            d_value = Decimal(value)
        except InvalidOperation:
            return False

        return True


class ValidatedStringEntry(ValidatedMixin, ttk.Entry):
    """An Entry that only accepts ISO Date strings"""

    def _key_validate(self, action, index, char, **kwargs):

        if action == '0':  # This is a delete action
            return True
        if char.isalpha() or char.isspace():
            return True

        Error("Only characters allowed!")
        return False

    def _focusout_validate(self, event):

        if not self.get():
            return False

        return True


class Error(tk.Toplevel):
    def __init__(self, message):
        tk.Toplevel.__init__(self)
        self.title('Error')
        self.attributes('-topmost', 'true')
        ttk.Label(self, text=message, font='Helvetica 24', style='danger.TLabel').grid(row=0, column=0)
        ttk.Button(self,style='warning.TButton', command=self.destroy, text="OK").grid(row=1, column=0)
        self.lift()
        self.grab_set()


class LabelInput(ttk.Frame):
    """A Widget containing label and input."""
    def __init__(self, parent, label, var, input_class=ttk.Entry,
                 input_args=None, label_args=None, **kwargs):
        super().__init__(parent, **kwargs)

        input_args = input_args or {}
        label_args = label_args or {}
        self.label = ttk.Label(self, text=label, **label_args)
        self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
        self.input = input_class(self, textvariable=var, **input_args)
        self.input.grid(row=0, column=1, sticky=(tk.W + tk.E))


class NewUserForm(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.svar_name = tk.StringVar()
        self.svar_balance = tk.StringVar()

        window_height = super().winfo_screenheight()
        window_width = super().winfo_screenwidth()
        input_width = int(window_width/40)
        label_width = int(window_width/60)
        button_width = int(window_width/5)

        LabelInput(self, "Name", self.svar_name,
                   input_class=ValidatedStringEntry,
                   input_args={"width": input_width, "style": 'primary.TEntry', "font": 'Helvetica 18'},
                   label_args={"width": label_width, "style": 'primary.Inverse.TLabel', "anchor": 'center'},
                   ).grid(row=0, column=0, sticky=tk.N)

        LabelInput(self, "Credit", self.svar_balance,
                   input_class=ValidatedNumEntry,
                   input_args={"width": input_width, "style": 'primary.TEntry', "font": 'Helvetica 18'},
                   label_args={"width": label_width, "style": 'primary.Inverse.TLabel', "anchor": 'center'},
                   ).grid(row=1, column=0, sticky=tk.N)

        self.keyboard = VKeyboard(self)
        self.keyboard.grid(row=2)

        buttons = tk.Frame(self)
        buttons.grid(row=3)

        self.save_button = ttk.Button(buttons,
                                      text="Save",
                                      style='success.TButton',
                                      command=self._on_save)
        self.save_button.grid(row=0,
                              column=0,
                              sticky=tk.W + tk.E,
                              rowspan=2,
                              padx=2,
                              pady=2,
                              ipadx=button_width,
                              ipady=10)

        self.close_button = ttk.Button(buttons,
                                       text="Close",
                                       style='danger.TButton',
                                       command=self.master.destroy)
        self.close_button.grid(row=0,
                               column=1,
                               sticky=tk.W + tk.E,
                               rowspan=2,
                               padx=2,
                               pady=2,
                               ipadx=button_width,
                               ipady=10)

    def get_user(self):
        self.wait_window()
        return

    def _on_save(self):
        if not self.svar_name.get():
            messagebox.showerror("Error", "Name needed!", parent=self)
            return
        value = self.svar_balance.get()
        try:
            d_value = Decimal(value)
        except InvalidOperation:
            messagebox.showerror("Error", "Credit needed!", parent=self)
            return
        self.master.balance = float(self.svar_balance.get())
        self.master.name = self.svar_name.get()
        self.master.destroy()


class PopupNewUser(tk.Toplevel):
    name = ""
    balance = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('New User Data')

        NewUserForm(self).pack()
        self.attributes("-fullscreen", True)
        self.style = Style()
        self.style.configure('TButton', font=('Helvetica', 18))
        self.style.configure('TLabel', font=('Helvetica', 30))
        self.style.map('TButton', foreground=[
            ('disabled', 'white'),
            ('active', 'yellow')])

    def get_user(self):
        self.wait_window()
        return self.name, self.balance


class PopupPay(tk.Toplevel):
    value = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Pay')
        self.attributes("-fullscreen", True)
        self.svar_amount = tk.StringVar()

        window_width = super().winfo_screenwidth()
        input_width = int(window_width / 40)
        label_width = int(window_width / 60)
        button_width = int(window_width / 5)

        LabelInput(self, "Credit", self.svar_amount,
                   input_class=ValidatedNumEntry,
                   input_args={"width": input_width, "style": 'primary.TEntry', "font": 'Helvetica 18'},
                   label_args={"width": label_width, "style": 'primary.Inverse.TLabel', "anchor": 'center'},
                   ).grid(row=1, column=0, sticky=tk.N)
        self.keyboard = VKeyboard(self)
        self.keyboard.grid(row=2)

        buttons = tk.Frame(self)
        buttons.grid(row=3)

        self.save_button = ttk.Button(buttons,
                                      text="Save",
                                      style='success.TButton',
                                      command=self._on_save)
        self.save_button.grid(row=0,
                              column=0,
                              sticky=tk.W + tk.E,
                              rowspan=2,
                              padx=2,
                              pady=2,
                              ipadx=button_width,
                              ipady=10)

        self.close_button = ttk.Button(buttons,
                                       text="Close",
                                       style='danger.TButton',
                                       command=self.master.destroy)
        self.close_button.grid(row=0,
                               column=1,
                               sticky=tk.W + tk.E,
                               rowspan=2,
                               padx=2,
                               pady=2,
                               ipadx=button_width,
                               ipady=10)

    def get_value(self):
        self.wait_window()
        return self.value

    def _on_save(self):
        self.value = float(self.svar_amount.get())
        try:
            d_value = Decimal(self.value)
        except InvalidOperation:
            messagebox.showerror("Error", "Enter valid amount!")
            return
        self.destroy()


if __name__ == "__main__":
    style = Style()
    root = style.master
    PopupNewUser(root)
    root.mainloop()
