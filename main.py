import tkinter as tk
from tkinter import ttk
from user import User
from db_functions import *
import tkinter.font as font
from VKeyboard import VKeyboard


class CafeApp(tk.Tk):
    database = "database/kittybase.sqlite3"
    
    def __init__(self):
        super().__init__()

        # Initiate virtual keyboard
        VKeyboard(self)

        # Configure the toplevel
        self.title("Cafe App")
#        self.attributes('-zoomed', True)
        self.geometry('600x400+100+100')
        self.resizable(False, False)
        self.wm_attributes('-type', 'splash')

        # Head frame
        self.frame_header = ttk.Frame()
        self.frame_header.pack(pady=20)
        self.frame_header.columnconfigure(0, weight=1)
        self.frame_header.columnconfigure(1, weight=2)
        self.logo = tk.PhotoImage(file='img/cafe_logo.png')
        self.header_logo = ttk.Label(self.frame_header, image=self.logo)
        self.header_logo.grid(column=0, row=0, rowspan=2)
        self.header_label1 = ttk.Label(self.frame_header, text="Choose your product wisely!")
        self.header_label1.grid(column=1, row=0)
        self.header_label2 = ttk.Label(self.frame_header, text="asalkdjflajds")
        self.header_label2.grid(column=1, row=1)

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
                self.users.append(User(id=user[0], username=user[1]))
            self.items_price_dict = get_products_list(db_conn)

        # Add data to the treeview.
        for user in self.users:
            self.content_tree.insert('', tk.END, values=[user.username, user.balance])

        self.button_add = ttk.Button()

    def create_tree(self, parent):
        columns = ('name', 'balance')
        style = ttk.Style()
        font_size = 24
        style.configure('Treeview.Heading', font='None, 28')
        style.configure('Treeview', font=f'None, {font_size}', rowheight=int(font_size*1.6))
        tree = ttk.Treeview(parent, columns=columns, show='headings', height=8)
        tree.heading(columns[0], text='Name')
        tree.column(columns[0], anchor=tk.CENTER, stretch=tk.NO, width=250)
        tree.heading(columns[1], text='Balance')
        tree.column(columns[1], anchor=tk.CENTER, stretch=tk.NO, width=250)
        tree.bind('<<TreeviewSelect>>', self.user_selected)
        tree.grid(column=0, row=0)
    
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        return tree

    def user_selected(self, event):
        selected_item = self.content_tree.selection()
        user_idx = self.content_tree.index(selected_item[0])

        item_price = self.popup_window()
        self.users[user_idx].calculate_debt(item_price)
        # Update the tree.
        user = self.users[user_idx]
        self.content_tree.item(selected_item[0], values=[user.username, user.balance])
        # Update database.
        db_conn = create_connection(self.database)
        with db_conn:
            update_user_debt(db_conn, user)

    def exit(self):
        pass

    def popup_window(self):
        item_price = PopupWindowItems(self).get_price()
        return item_price


class PopupWindowItems(tk.Toplevel):
    item_price = 0

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Select")

        self.products_dict = parent.items_price_dict
        products = self.products_dict.keys()

        label = ttk.Label(self, text="Hello World!")
        label.pack(fill='x', padx=50, pady=5)

        self.center_win()
        self.wm_attributes('-type', 'splash')

        #  Configure button style
        style = ttk.Style()
        style.configure('MyStyle.TButton', font='helvetica, 28')

        self.button_item = []
        for item in products:
            self.button_item = ttk.Button(self, text=item, command=lambda m=item: self.get_selected_item_price(m))
            self.button_item['style'] = 'MyStyle.TButton'
            self.button_item.pack(fill='x')
        
        self.button_close = ttk.Button(self, text="Close", command=self.destroy)
        self.button_close['style'] = 'MyStyle.TButton'
        self.button_close.pack(fill='x')

    def center_win(self):
        width = self.winfo_screenwidth() // 4
        height = self.winfo_screenheight() // 2
        x = self.winfo_screenwidth() // 2 - width // 2
        y = self.winfo_screenheight() // 2 - height // 2

        self.geometry(f'{width}x{height}+{x}+{y}')

    def get_selected_item_price(self, item):
        self.item_price = self.products_dict[item]
        self.destroy()

    def get_price(self):
        self.wait_window()
        return self.item_price


if __name__ == "__main__":
    app = CafeApp()
    app.mainloop()
