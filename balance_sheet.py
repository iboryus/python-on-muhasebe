import tkinter as tk
from database import create_connection
from datetime import datetime

def calculate_balance():
    connection = create_connection()
    cursor = connection.cursor()

    start_date = datetime.now().replace(day=1).strftime('%Y-%m-%d')

    cursor.execute('''
        SELECT SUM(amount) FROM transactions
                   WHERE transaction_type = 'Alacak' AND date >= ?
    ''',(start_date,))
    total_income = cursor.fetchone()[0] or 0.0

    cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE transaction_type = 'Verecek' AND date >= ?
    ''', (start_date,))
    total_expense = cursor.fetchone()[0] or 0.0
    net_balance = total_income - total_expense

    connection.close()

    return total_expense, total_income, net_balance

def open_balance_sheet():
    balance_window = tk.Tk()
    balance_window.title("Bilanço")

    tk.Label(balance_window, text="Aylık Bilanço").pack()

    total_income, total_expense, net_balance = calculate_balance()

    tk.Label(balance_window, text=f"Toplam Gelir: {total_income:.2f}").pack()
    tk.Label(balance_window, text=f"Toplam Gider: {total_expense: .2f}").pack()

    balance_text = "Net Kar" if net_balance >= 0 else "Net Borç"
    tk.Label(balance_window, text=f"{balance_text}: {abs(net_balance):.2f}").pack()

    balance_window.mainloop()
