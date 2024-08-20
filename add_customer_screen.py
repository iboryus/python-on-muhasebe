import tkinter as tk
from database import create_connection

def add_customer(name, company, address):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO customers (name, company, address)
        VALUES (?, ?, ?)
    ''', (name, company, address))

    connection.commit()
    connection.close()

def open_add_customer_screen():
    add_customer_window = tk.Tk()
    add_customer_window.title("Müşteri Ekle")
    
    tk.Label(add_customer_window, text="Ad Soyad").pack()
    name_entry = tk.Entry(add_customer_window)
    name_entry.pack()
    
    tk.Label(add_customer_window, text="Firma Adı").pack()
    company_entry = tk.Entry(add_customer_window)
    company_entry.pack()
    
    tk.Label(add_customer_window, text="Adres").pack()
    address_entry = tk.Entry(add_customer_window)
    address_entry.pack()
    
    def submit_customer():
        name = name_entry.get()
        company = company_entry.get()
        address = address_entry.get()
        
        if name:
            add_customer(name, company, address)
            tk.messagebox.showinfo("Başarılı", "Müşteri eklendi!")
        else:
            tk.messagebox.showerror("Hata", "Ad Soyad alanı zorunludur.")
    
    tk.Button(add_customer_window, text="Ekle", command=submit_customer).pack()
    
    add_customer_window.mainloop()

open_add_customer_screen()
