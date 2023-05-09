import tkinter as tk
from tkinter import ttk
import os
from user import *
from db_functions import *
from VKeyboard import VKeyboard
from ttkbootstrap import Style


class App(tk.Tk):
    path_to_file = os.path.abspath(__file__)
    dir_path = os.path.dirname(path_to_file)
    database = dir_path+"/database/kittybase.sqlite3"

    last_y = 0
    is_scrolling = False
    
    def __init__(self):
        super().__init__()

        # Initiate virtual keyboard
        # VKeyboard(self)

        # Configure the toplevel
        self.title("Cafe App")
        self.attributes("-fullscreen", True)

        #  Configure label style
        style = Style()
        style.configure('TLabel', font=('Helvetica', 30))

        # Head frame
        self.frame_header = ttk.Frame()
        self.frame_header.pack(pady=0)
        self.logo = tk.PhotoImage(file=self.dir_path+'/img/cafe_logo.png')
        self.header_logo = ttk.Label(self.frame_header,
                                     image=self.logo)
        self.header_logo.grid(column=0, row=0)
        self.header_label1 = ttk.Label(self.frame_header,
                                       text="Please select who you are:")
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
                self.users.append(User(id=user[0], username=user[1], balance=user[2]))
            self.items_price_dict = get_products_list(db_conn)

        # Add data to the treeview.
        for user in self.users:
            self.content_tree.insert('', tk.END, values=[user.username, user.balance])

        self.button_add = ttk.Button(self,
                                     text="Add User",
                                     command=self.call_adduser_popup)
        self.button_add.pack()

    def create_tree(self, parent):

        columns = ('name', 'balance')
        style = Style()
        font_size = 24
        style.configure('Treeview.Heading', font='None, 28')
        style.configure('Treeview', font=f'None, {font_size}', rowheight=int(font_size*1.6))

        tree = ttk.Treeview(parent, columns=columns, show='headings', height=6)
        tree.heading(columns[0], text='Name')
        tree.column(columns[0], anchor=tk.CENTER, stretch=tk.NO, width=350)
        tree.heading(columns[1], text='Balance')
        tree.column(columns[1], anchor=tk.CENTER, stretch=tk.NO, width=350)
        tree.bind('<B1-Motion>', self.scroll_treeview)
        tree.bind('<ButtonRelease-1>', self.user_selected)

        tree.grid(column=0, row=0, pady=20)

        return tree

    def scroll_treeview(self, event):
        delta_y = event.y_root - self.last_y
        if delta_y > 10:
            self.is_scrolling = True
            self.content_tree.yview_scroll(-1 * int(delta_y/10), "units")
            self.last_y = event.y_root

    def user_selected(self, event):
        if self.is_scrolling:
            self.is_scrolling = False
            return

        selected_item = self.content_tree.selection()
        user_idx = self.content_tree.index(selected_item[0])

        amount, payment = self.call_items_popup()
        if payment:
            self.users[user_idx].pay_debt(amount)
        else:
            self.users[user_idx].calculate_debt(amount)

        # Update the tree.
        user = self.users[user_idx]
        self.content_tree.item(selected_item[0], values=[user.username, user.balance])
        # Update database.
        db_conn = create_connection(self.database)
        with db_conn:
            update_user_debt(db_conn, user)

    def exit(self):
        pass

    def call_items_popup(self):
        # Get item price and return it.
        return PopupWindowItems(self).get_price()

    def call_adduser_popup(self):
        name, balance = PopupNewUser(self).get_user()
        if name == "":
            return
        self.update_new_user(name, balance)

    def update_new_user(self, name, balance):
        user = User(username=name, balance=balance)
        db_conn = create_connection(self.database)
        self.users = []
        with db_conn:
            add_user(db_conn, user)
            users = get_users(db_conn)
            for user in users:
                self.users.append(User(id=user[0], username=user[1], balance=user[2]))
        # Add data to the treeview.
        self.content_tree.delete(*self.content_tree.get_children())
        for user in self.users:
            self.content_tree.insert('', tk.END, values=[user.username, user.balance])


class PopupWindowItems(tk.Toplevel):
    value = 0
    payment = False

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Select")

        self.products_dict = parent.items_price_dict
        products = self.products_dict.keys()

        label = ttk.Label(self, text="Select Product:")
        label.pack(fill='x', padx=150, pady=5)

        # Configure window appearance
        self.attributes("-fullscreen", True)

        #  Configure button style
        self.style = Style()
        self.style.configure('TButton', font=('Helvetica', 18))
        self.style.configure('TLabel', font=('Helvetica', 30))

        self.button_item = []
        for item in products:
            self.button_item = ttk.Button(self, text=item, command=lambda m=item: self.get_selected_item_price(m))
            self.button_item.pack(fill='x')

        self.button_pay = ttk.Button(self,
                                     text="Pay Debt!!",
                                     style='info.TButton',
                                     command=self.open_pay_popup)
        self.button_pay.pack(fill='x')

        self.button_close = ttk.Button(self,
                                       text="Close",
                                       style='danger.TButton',
                                       command=self.destroy)
        self.button_close.pack(fill='x')

    def open_pay_popup(self):
        self.value = PopupPay(self).get_value()
        self.payment = True
        self.destroy()

    def get_selected_item_price(self, item):
        self.value = self.products_dict[item]
        self.destroy()

    def get_price(self):
        self.wait_window()
        return self.value, self.payment


if __name__ == "__main__":
    app = App()
    style = Style()
    app.mainloop()
