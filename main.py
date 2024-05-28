import os
import threading
import time
import tkinter as tk
from datetime import datetime
from functools import partial
from tkinter import ttk

from ttkbootstrap import Style

from db_functions import *
from shelly_log import log_voltage_main
from user import *
from VKeyboard import VKeyboard


class App(tk.Tk):
    path_to_file = os.path.abspath(__file__)
    dir_path = os.path.dirname(path_to_file)
    database = dir_path + "/database/kittybase.sqlite3"

    def __init__(self):
        super().__init__()

        # Initiate virtual keyboard
        # VKeyboard(self)

        # Configure the toplevel
        self.title("AIBE Coffee")
        self.attributes("-fullscreen", True)

        #  Configure label style
        style = Style()
        style.configure('TLabel', font=('Helvetica', 30))

        # Head frame
        self.frame_header = ttk.Frame()
        self.frame_header.pack(pady=0)
        self.logo = tk.PhotoImage(file=self.dir_path + '/img/cafe_logo.png')
        self.header_logo = ttk.Label(self.frame_header, image=self.logo)
        self.header_logo.grid(column=0, row=0)
        self.header_label1 = ttk.Label(
            self.frame_header, text="Please select who you are:"
        )
        self.header_label1.grid(column=1, row=0)

        # Content frame
        self.frame_content = ttk.Frame()
        self.frame_content.pack()
        self.frame_content.columnconfigure(0, weight=1)
        self.content_tree = self.create_tree(self.frame_content)

        self.users = []
        db_conn = create_connection(self.database)
        with db_conn:
            users = get_users(db_conn)
            for user in users:
                self.users.append(
                    User(id=user[0], username=user[1], debts=user[2])
                )
            self.items_price_dict = get_products_list(db_conn)

        # Add data to the treeview.
        for user in self.users:
            self.content_tree.insert(
                '', tk.END, values=[user.username, user.debts]
            )

        self.button_add = ttk.Button(
            self, text="Add User", command=self.call_adduser_popup
        )

        # increase button size and pack
        self.button_add.pack(fill='x', ipady=100, padx=200, pady=10)

        self.bind("<Escape>", self.close_app)

    def create_tree(self, parent):
        columns = ('name', 'debts')
        style = Style()
        font_size = 36
        style.configure('Treeview.Heading', font='None, 28')
        style.configure(
            'Treeview',
            font=f'None, {font_size}',
            rowheight=int(font_size * 1.6),
        )
        style.configure("Custom.Vertical.TScrollbar", arrowsize=60)

        tree = ttk.Treeview(parent, columns=columns, show='headings', height=6)
        tree.heading(columns[0], text='Name')
        tree.column(columns[0], anchor=tk.CENTER, stretch=tk.NO, width=350)
        tree.heading(columns[1], text='Debts')
        tree.column(columns[1], anchor=tk.CENTER, stretch=tk.NO, width=350)
        tree.bind('<<TreeviewSelect>>', self.user_selected)
        tree.grid(column=0, row=0, pady=20)

        scrollbar = ttk.Scrollbar(
            parent,
            orient=tk.VERTICAL,
            style="Custom.Vertical.TScrollbar",
            command=tree.yview,
        )
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        return tree

    def user_selected(self, event):
        selected_item = self.content_tree.selection()
        user_idx = self.content_tree.index(selected_item[0])
        item, amount, payment = self.call_items_popup(self.users[user_idx])

        if payment:
            self.users[user_idx].pay_debt(amount)
        elif amount == 0:
            pass
        else:
            self.users[user_idx].calculate_debt(amount)

        # Update the tree.
        user = self.users[user_idx]
        self.content_tree.item(
            selected_item[0], values=[user.username, user.debts]
        )
        # Update database.
        db_conn = create_connection(self.database)
        with db_conn:
            update_user_debt(db_conn, user)

            # Add consumed product to database
            dt = datetime.now()
            if item is not None:
                add_consumed_product(
                    db_conn,
                    user,
                    product=item,
                    time_stamp=dt.strftime("%Y-%m-%d--%H-%M-%S.%f"),
                )

    def exit(self):
        pass

    def close_app(self, event):
        self.destroy()

    def call_items_popup(self, user):
        # Get item price and return it.
        return PopupWindowItems(self, user).get_price()

    def call_adduser_popup(self):
        name, debts = PopupNewUser(self).get_user()
        if name == "":
            return
        self.update_new_user(name, debts)

    def update_new_user(self, name, debts):
        user = User(username=name, debts=debts)
        db_conn = create_connection(self.database)
        self.users = []
        with db_conn:
            add_user(db_conn, user)
            users = get_users(db_conn)
            for user in users:
                self.users.append(
                    User(id=user[0], username=user[1], debts=user[2])
                )
        # Add data to the treeview.
        self.content_tree.delete(*self.content_tree.get_children())
        for user in self.users:
            self.content_tree.insert(
                '', tk.END, values=[user.username, user.debts]
            )


class PopupWindowItems(tk.Toplevel):
    value = 0
    payment = False
    item = None

    def __init__(self, parent, user):
        super().__init__(parent)
        self.title("Select")
        self.user = user

        self.products_dict = parent.items_price_dict

        label = ttk.Label(self, text="Select Product:")
        label.pack(fill='x', padx=150, pady=5)
        # Configure window appearance
        self.attributes("-fullscreen", True)
        #  Configure button style
        self.style = Style()
        self.style.configure('TButton', font=('Helvetica', 24))

        self.button_item = []
        for i, (item, price) in enumerate(self.products_dict.items()):
            # Construct the display string with consistent spacing between item and price
            display_string = f"{item:<28.30}\t\t{price} €"
            self.button_item = ttk.Button(
                self,
                text=display_string,
                command=lambda m=item, p=price: self.get_selected_item(m, p),
                style='LeftAlign.TButton',
            )
            self.button_item.pack(fill='x', ipady=6)

        self.button_pay = ttk.Button(
            self,
            text="Pay Debt",
            style='info.TButton',
            command=self.open_pay_popup,
        )
        self.button_pay.pack(fill='x', ipady=6)

        self.button_close = ttk.Button(
            self, text="Close", style='danger.TButton', command=self.destroy
        )
        self.button_close.pack(fill='x', ipady=6)

    def open_pay_popup(self):
        self.value, self.payment = PopupPay(self).do_payment()
        if self.payment:
            self.destroy()

    def get_selected_item(self, item, price):
        self.item = item
        self.value = price
        self.destroy()

    def get_price(self):
        self.wait_window()
        return self.item, self.value, self.payment


def main():
    # Signal for background thread to stop
    stop_signal = threading.Event()

    # Create and start the thread
    thread = threading.Thread(target=log_voltage_main, args=(stop_signal,))
    # Start the thread
    thread.start()

    # continue
    app = App()
    style = Style()
    app.mainloop()

    stop_signal.set()
    # Wait for the thread to finish
    thread.join()


if __name__ == '__main__':
    main()
