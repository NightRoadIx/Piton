# import modules
from tkinter import *
import os

# Para la ventana de registro
def register():
    # Generar una variable global
    global register_screen
    # Hacer que la ventana de registro sea de alto nivel
    register_screen = Toplevel(main_screen)
    # Título de la ventana
    register_screen.title("Registro")
    # Geometría de la ventana
    register_screen.geometry("300x250")

    # Variables globales
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Ingrese los datos para darse de alta", bg="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Nombre de usuario * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Contraseña * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Registro", width=10, height=1, bg="white", command=register_user).pack()

# Ventana para dar de alta
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Ingrese los datos para ingresar").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Nombre de usuario * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Contraseña * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Ingresar", width=10, height=1, command=login_verify).pack()

# Implementar el evento al registrar el botón
def register_user():
    username_info = username.get()
    password_info = password.get()

    # Abrir un archivo
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registro exitoso", fg="green", font=("calibri", 11)).pack()

# Implementar el evento en caso de dar clic en el botón Ingresar
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

# Diseñar la ventana para cuando se logra el ingreso
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Ingreso exitoso")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Ingreso exitoso").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Diseñar la ventana para cuando falla el ingreso
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Ingreso fallido")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Contraseña inválida").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Diseñar la ventana para usuario no hallado
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Usuario no encontrado")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Usuario no encontrado").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Para eliminar las ventanas
def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# Diseñar la ventana principal
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Ingreso a cuenta")
    Label(text="Seleccione", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Ingresar", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Registrar", height="2", width="30", command=register).pack()

    # Ventana principal
    main_screen.mainloop()

# Lanzar la ventana principal
main_account_screen()
