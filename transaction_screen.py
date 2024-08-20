import tkinter as tk
from tkinter import ttk
from datetime import datetime
from database import create_connection

def get_customers():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name FROM customers')
    customers = cursor.fetchall()
    connection.close()
    return customers

def record_transaction(customer_id, transaction_type, amount):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO transactions (customer_id, transaction_type, amount)
        VALUES (?, ?, ?)
    ''', (customer_id, transaction_type, amount))

    connection.commit()
    connection.close()

def open_transaction_screen():
    transaction_window = tk.Tk()
    transaction_window.title("İşlem Ekranı")
    
    tk.Label(transaction_window, text="Müşteri Seçin").pack()
    
    customers = get_customers()
    customer_var = tk.StringVar()
    customer_dropdown = ttk.Combobox(transaction_window, textvariable=customer_var)
    customer_dropdown['values'] = [f"{customer[1]}" for customer in customers]
    customer_dropdown.pack()
    
    tk.Label(transaction_window, text="İşlem Türü Seçin").pack()
    
    transaction_type_var = tk.StringVar(value="Alacak")
    tk.Radiobutton(transaction_window, text="Alacak", variable=transaction_type_var, value="Alacak").pack()
    tk.Radiobutton(transaction_window, text="Verecek", variable=transaction_type_var, value="Verecek").pack()
    
    tk.Label(transaction_window, text="Tutar").pack()
    amount_entry = tk.Entry(transaction_window)
    amount_entry.pack()
    
    def submit_transaction():
        customer_name = customer_var.get()
        transaction_type = transaction_type_var.get()
        amount = amount_entry.get()
        customer_id = None

        for customer in customers:
            if customer[1] == customer_name:
                customer_id = customer[0]
                break
        
        if customer_id and amount:
            record_transaction(customer_id, transaction_type, amount)
            tk.messagebox.showinfo("Başarılı", "İşlem kaydedildi!")
        else:
            tk.messagebox.showerror("Hata", "Tüm alanları doldurmalısınız.")
    
    tk.Button(transaction_window, text="Kaydet", command=submit_transaction).pack()
    
    transaction_window.mainloop()
