import tkinter as tk
from tkinter import messagebox

#Kullanıcı adı şifre kontrolü
def check_login(username, password):
    if username == "admin" and password == "sifre":
        return True
    else:
        return False

def login():
    username = entry_username.get()
    password = entry_password.get()

    if check_login(username, password):
        messagebox.showinfo("Giriş Başarılı")
        open_main_window()
    else:
        messagebox.showerror("Giriş Başarısız")

def open_main_window():
    login_windows.destrol()
    main_window = tk.TK()
    main_window.title("Ana Ekran")
    main_window.mainloop()

login_window = tk.TK()
login_window.title("Giriş Ekranı")

tk.Label(login_window, text="Kullanıcı Adı").pack()
entry_username = tk.Entry(login_window)
entry_username.pack()

tk.Label(login_window, text="Şifre").pack()
entry_password = tk.Entry(login_window, show="*")
entry_password.pack()

tk.Button(login_window, text="Giriş Yap", command=login).pack()

login_window.mainloop()