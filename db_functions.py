import sqlite3
from sqlite3 import Error

from user import User


#################################################################
# GENERAL
#################################################################
def create_connection(db_file):
    """create a database connection to the SQLite database
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


def init_table(db_conn):
    """
    Initialize the database with the necessary tables
    """
    cur = db_conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS statistics (id INTEGER PRIMARY KEY, user TEXT, debts REAL, consumed REAL)"
    )
    cur.execute("CREATE TABLE IF NOT EXISTS products (name TEXT, price REAL)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS consumed (id INTEGER PRIMARY KEY, user TEXT, product TEXT, time_stamp TEXT)"
    )
    db_conn.commit()


def get_products_list(db_conn):
    """
    Get the list of products and their prices
    """
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM products")
    products_list = cur.fetchall()
    # Column 0 is name, column 1 is price
    row1 = [item[0] for item in products_list]
    row2 = [item[1] for item in products_list]
    items_price_dict = dict(zip(row1, row2))
    return items_price_dict


#################################################################
# USERS
#################################################################
def get_users(db_conn):
    """
    Get the list of users and their debts
    """
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM statistics ORDER BY user ASC")
    users = cur.fetchall()
    return users


def add_user(db_conn, user=User):
    """
    Add a user to the database
    """
    cur = db_conn.cursor()
    cur.execute(
        "INSERT INTO statistics (user, debts) VALUES(?, ?)",
        (user.username, user.debts),
    )
    db_conn.commit()


def update_user_debt(db_conn, user=User):
    """
    Update the user's debt in the database
    """
    cur = db_conn.cursor()
    cur.execute(
        "UPDATE statistics SET debts=? WHERE id=(?)", (user.debts, user.id)
    )
    db_conn.commit()


#################################################################
# PRODUCTS
#################################################################
def get_product_price(db_conn, product: str):
    """
    Get the price of a product

    :param product: the name of the product
    """
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM products WHERE name=?", (product,))


def _add_product(db_conn, product: tuple):
    """
    Add a product to the database

    :param product: tuple with the product name and price
    """
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM products WHERE name=?", (product[0],))
    existing_product = cur.fetchone()
    if existing_product:
        print("Product already exists")
    else:
        cur.execute(
            "INSERT INTO products (name, price) VALUES(?, ?)",
            (product[0], product[1]),
        )
        db_conn.commit()


def add_products(db_conn):
    """
    Add some products to the database
    """
    _add_product(db_conn, ("coffee/americano", 0.30))
    _add_product(db_conn, ("coffee/americano (sugar)", 0.35))
    _add_product(db_conn, ("coffee/americano (milk)", 0.35))
    _add_product(db_conn, ("coffee/americano (sugar&milk)", 0.40))
    _add_product(db_conn, ("cappuccino/macchiato", 0.40))
    _add_product(db_conn, ("glass of milk", 0.50))


#################################################################
# CONSUME
#################################################################
def add_consumed_product(db_conn, user: User, product: str, time_stamp: str):
    """
    Add a consumed product to the database

    :param user: the name of the user
    :param product: the name of the product
    :param time_stamp: the time of the consumption
    """
    print(user.username, product, time_stamp)
    cur = db_conn.cursor()
    cur.execute(
        "INSERT INTO consumed (user, product, time_stamp) VALUES(?, ?, ?)",
        (user.username, product, time_stamp),
    )
    db_conn.commit()


if __name__ == '__main__':
    database = "database/kittybase.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
        init_table(conn)
        add_products(conn)
