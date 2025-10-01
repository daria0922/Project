import sqlite3

db_name = "products.db"

def open_connection():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # ✅ щоб результати були як словники
    cursor = conn.cursor()
    return conn, cursor

def close_connection(conn, cursor):
    cursor.close()
    conn.close()

def execute_query(query, params=()):
    conn, cursor = open_connection()
    if isinstance(params[0] if params else None, (tuple, list)):
        cursor.executemany(query, params)
    else:
        cursor.execute(query, params)
    conn.commit()
    close_connection(conn, cursor)

def clear_db():
    execute_query("DROP TABLE IF EXISTS products")

def create_table():
    query = """CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    description TEXT,
                    size TEXT,
                    color TEXT,
                    category TEXT,
                    stock INTEGER DEFAULT 0,
                    image_url TEXT,
                    is_new BOOL
               )"""
    execute_query(query)

# ✅ прибрав product_id — бо id створюється автоматично
def add_product(name:str, price:int, description:str, size:str, color:str, category:str, stock:int, image_url:str, is_new:bool):
    query = """INSERT INTO products (name, price, description, size, color, category, stock, image_url, is_new)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    execute_query(query, (name, price, description, size, color, category, stock, image_url, is_new))

def get_all_products():
    conn, cursor = open_connection()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    close_connection(conn, cursor)
    return rows

def get_product(product_id: int):
    conn, cursor = open_connection()
    cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    row = cursor.fetchone()
    close_connection(conn, cursor)
    return row

def update_product(product_id: int, name:str, price:int, description:str, size:str, color:str, category:str, stock:int, image_url:str, is_new:bool):
    query = """UPDATE products 
               SET name=?, price=?, description=?, size=?, color=?, category=?, stock=?, image_url=?, is_new=?
               WHERE id=?"""
    execute_query(query, (name, price, description, size, color, category, stock, image_url, is_new, product_id))

def delete_product(product_id: int):
    execute_query("DELETE FROM products WHERE id=?", (product_id,))

def get_new_products():
    conn, cursor = open_connection()
    cursor.execute("SELECT * FROM products WHERE is_new=1")
    rows = cursor.fetchall()
    close_connection(conn, cursor)
    return rows


if __name__ == "__main__":
    clear_db()
    create_table()
