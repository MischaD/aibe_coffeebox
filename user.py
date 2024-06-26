import tkinter
from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk
from VKeyboard import VKeyboard
from tkinter import messagebox
from decimal import Decimal, InvalidOperation
from ttkbootstrap import Style
from payment import get_payment_img_path


@dataclass
class User:
    id: int = 0
    username: str = ''
    debts: float = 0.0
    consumed: float = 0.0
    paid: float = 0.0

    def calculate_debt(self, item_price):
        self.debts = round(self.debts + item_price, 2)
        self.consumed = round(self.consumed + item_price, 2)

    def pay_debt(self, amount):
        self.debts = round(self.debts + amount, 2)


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

        # Error("Only characters allowed!")
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

        window_width = super().winfo_screenwidth()
        input_width = int(window_width/20)
        label_width = int(window_width/100)
        button_width = int(window_width/5)

        label_input = LabelInput(self, "Name", self.svar_name,
                   input_class=ValidatedStringEntry,
                   input_args={"width": input_width, "style": 'primary.TEntry', "font": 'Helvetica 18'},
                   label_args={"width": label_width, "style": 'primary.Inverse.TLabel', "anchor": 'center'},
                   )
        label_input.grid(row=0, column=0, sticky=tk.N, pady=50)

        self.keyboard = VKeyboard(self, label_input.input)
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

        self.master.debts = 0
        self.master.name = self.svar_name.get()
        self.master.destroy()


class PopupNewUser(tk.Toplevel):
    name = ""
    debts = 0

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
        return self.name, self.debts


class PopupPay(tk.Toplevel):
    value = 0
    payment = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Payment Form")
        self.attributes("-fullscreen", True)

        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill='both')

        # Assuming self.master.user exists and has the necessary attributes
        self.user = self.master.user
        self.header_label = ttk.Label(self.frame,
                                       text=f"User: {self.user.username} - Pay amount:  {self.user.debts} €")
        self.header_label.grid(column=0, row=0, columnspan=2)  # Spanning across both button columns

        # QR Code Image
        self.qr = tk.PhotoImage(file=get_payment_img_path(self.master.user.debts))
        self.header_logo = ttk.Label(self.frame, image=self.qr)
        self.header_logo.grid(column=0, row=1, columnspan=2)  # Adjusting to span both columns

        # Buttons with uniform size and spacing
        self.save_button = ttk.Button(self.frame, text="Back", style='danger.TButton', command=self.destroy)
        self.save_button.grid(row=2, column=0, sticky=tk.EW, padx=5, pady=2)

        self.close_button = ttk.Button(self.frame, text="Pay", style='success.TButton', command=self._on_paid)
        self.close_button.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=2)

        # Configure the frame's grid to center content and equalize button sizes
        self.frame.columnconfigure(0, weight=1, uniform='btn')
        self.frame.columnconfigure(1, weight=1, uniform='btn')
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)

        # Ensuring the window and its content are updated to apply layout changes
        self.update()   

    def do_payment(self):
        self.wait_window()
        return self.value, self.payment

    def _on_paid(self):
        self.value = -1 * self.user.debts # paied debts
        self.payment = True
        self.destroy()


if __name__ == "__main__":
    style = Style()
    root = style.master
    PopupNewUser(root)
    root.mainloop()
