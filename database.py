import sqlite3

def create_connection():
    connection = sqlite3.connect('bookkeeping.db')
    return connection

def create_tables():
    connection = create_connection()
    cursor = connection.cursor()

    # Müşteriler tablosu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            company TEXT,
            address TEXT
        )
    ''')

    # İşlemler tablosu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            transaction_type TEXT,
            amount REAL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
    ''')

    connection.commit()
    connection.close()

# Bu dosyayı çalıştırarak tabloları oluşturun
if __name__ == '__main__':
    create_tables()
