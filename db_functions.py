import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def get_products_list(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM products ORDER BY name ASC")  
    products_list = cur.fetchall()
    # Column 0 is name, column 1 is price
    row1= [item[0] for item in products_list]
    row2= [item[1] for item in products_list]
    items_price_dict = dict(zip(row1, row2))

    return items_price_dict

def get_users(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM statistics")
    users = cur.fetchall()
    
    return users

def get_product_price(conn):
    product = "lemonade"
    cur = conn.cursor()
    cur.execute("SELECT price FROM products WHERE name=?",(product,))

    price = cur.fetchone()
    print("asdf", price[0])

def add_user(conn):
    username = "Michael"
    cur = conn.cursor()
    cur.execute("INSERT INTO statistics (user) VALUES(?)", (username,))

    conn.commit()

def update_user(conn,user):
    cur = conn.cursor()
    cur.execute("INSERT INTO statistics (balance) WHERE VALUES(?)", (user.balance,))


if __name__ == '__main__':
    database = "database/coffeebase.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
        get_products_list(conn)
        get_users(conn)
