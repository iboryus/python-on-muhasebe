import tkinter as tk
from tkinter import messagebox
from transaction_screen import open_transaction_screen
from balance_sheet import open_balance_sheet
from customer_balance import open_customer_balance
from add_customer_screen import open_add_customer_screen

# Kullanıcı Girişi ve Ana Ekran kodları burada

def open_main_window():
    main_window = tk.Tk()
    main_window.title("Ana Ekran")
    
    tk.Button(main_window, text="İşlem Ekranı", command=open_transaction_screen).pack()
    tk.Button(main_window, text="Bilanço", command=open_balance_sheet).pack()
    tk.Button(main_window, text="Müşteri Bilançosu", command=open_customer_balance).pack()
    tk.Button(main_window, text="Müşteri Ekle", command=open_add_customer_screen).pack()
    
    main_window.mainloop()
open_main_window()