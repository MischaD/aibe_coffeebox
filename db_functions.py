import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    db_conn = None
    try:
        db_conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return db_conn


def get_products_list(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM products ORDER BY name ASC")  
    products_list = cur.fetchall()
    # Column 0 is name, column 1 is price
    row1= [item[0] for item in products_list]
    row2= [item[1] for item in products_list]
    items_price_dict = dict(zip(row1, row2))

    return items_price_dict


def get_users(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM statistics")
    users = cur.fetchall()
    
    return users


def get_product_price(db_conn):
    product = "lemonade"
    cur = db_conn.cursor()
    cur.execute("SELECT price FROM products WHERE name=?",(product,))

    price = cur.fetchone()
    print("asdf", price[0])


def add_user(db_conn):
    username = "Michael"
    cur = db_conn.cursor()
    cur.execute("INSERT INTO statistics (user) VALUES(?)", (username,))

    db_conn.commit()


def update_user_debt(db_conn, user):
    cur = db_conn.cursor()
    cur.execute("UPDATE statistics SET balance=? WHERE id=(?)", (user.balance,user.id))
    cur.execute("UPDATE statistics SET consumed=? WHERE id=(?)", (user.consumed,user.id))

    #conn.commit()


if __name__ == '__main__':
    database = "database/kittybase.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
        get_products_list(conn)
        bla = (1,'kokolores')
        update_user_debt(conn,bla)
        bla = get_users(conn)
        print(bla)
