from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

from user import User
from db_functions import *

class CafeApp(Tk):
    database = "database/kittybase.sqlite3"
    
    def __init__(self):
        super().__init__()

        # Configure the toplevel
        self.title("Cafe App")
        #self.state('zoomed')
        self.geometry('600x400+100+100')
        self.resizable(False,False)

        self.frame_header = ttk.Frame()
        self.frame_header.pack()
        self.frame_header.columnconfigure(0, weight=1)
        self.frame_header.columnconfigure(1, weight=2)
        
        self.logo = PhotoImage(file = 'img/cafe_logo.png')
        self.header_logo = ttk.Label(self.frame_header, image = self.logo)
        self.header_logo.grid(column=0, row=0, rowspan=2)
        self.header_label1 = ttk.Label(self.frame_header, text = "Choose your product wisely!")
        self.header_label1.grid(column=1, row=0)
        self.header_label2 = ttk.Label(self.frame_header, text = "asalkdjflajds")
        self.header_label2.grid(column=1, row=1)

        self.frame_content = ttk.Frame()
        self.frame_content.pack()
        self.content_tree = self.create_tree(self.frame_content)
        
        self.users = []
        conn = create_connection(self.database)
        with conn:
            users = get_users(conn)
            for user in users:
                self.users.append(User(id=user[0], username=user[1]))
            self.items_price_dict = get_products_list(conn)

        # add data to the treeview
        for user in self.users:
           self.content_tree.insert('', END, values=[user.username, user.balance])

    def create_tree(self,parent):
        columns = ('name', 'balance')
        tree = ttk.Treeview(parent, columns=columns, show='headings')
        tree.grid(column=0, row=0, rowspan=3)
        tree.heading(columns[0], text='Name')
        tree.heading(columns[1], text='Balance')
        tree.bind('<<TreeviewSelect>>', self.user_selected)
        tree.grid(column=0, row=0, rowspan=3)
    
        scrollbar = ttk.Scrollbar(parent, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, rowspan=3, sticky='ns')

        return tree

    def user_selected(self,event):
        selected_item = self.content_tree.selection()
        user_idx = self.content_tree.index(selected_item)

        item_price = self.popup_window()
        self.users[user_idx].calculate_debt(item_price)
        # Update the tree.
        user = self.users[user_idx]
        self.content_tree.item(selected_item[0], values=[user.username, user.balance])
        # Update database.
        conn = create_connection(self.database)
        with conn:
            update_user_debt(conn,user)


    def popup_window(self):
        item_price = PopupWindow(self).get_price()
        return item_price

class PopupWindow():
    def __init__(self, parent):
        self.parent = parent      
        self.products_dict = parent.items_price_dict
        products = self.products_dict.keys()
        self.toplevel = Toplevel(parent)
        self.toplevel.title("Select")
        label = Label(self.toplevel, text="Hello World!")
        label.pack(fill='x', padx=50, pady=5)

        self.button_item = []
        for item in products:
            self.button_item = Button(self.toplevel, text=item, command=lambda m=item:self.get_selected_item_price(m))
            self.button_item.pack(fill='x')
        
        self.button_close = Button(self.toplevel, text="Close", command=self.toplevel.destroy)
        self.button_close.pack(fill='x')

    def get_selected_item_price(self,item):
        self.item_price = self.products_dict[item]
        self.toplevel.destroy()

    def get_price(self):
        self.toplevel.wait_window()
        return self.item_price

if __name__ == "__main__":
    app = CafeApp()
    app.mainloop()