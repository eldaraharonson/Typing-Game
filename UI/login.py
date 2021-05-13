from tkinter import *
import mysql.connector

def create_login_window():
    # connect_to_database()
    # login_window = Tk()
    # define_window_style(login_window)
    # add_labels(login_window)
    # add_user_and_password_text_box(login_window)
    # define_login_button(login_window)
    # login_window.mainloop()
    pass

# I already created an empty database named typing_game_database
def connect_to_database():
    db = mysql.connector.connect(host="localhost", user="root", password="prince1995",
                                 database="typing_game_database")
    my_cursor = db.cursor()


def define_window_style(login_window):
    login_window.title("Login")
    login_window.geometry("500x300")
    login_window["bg"] = "light blue"


# if user already in db then login, if not create new user with the password
def add_labels(login_window):
    Label(text="Welcome to Speed Typing!!", font=("Arial", 18), bg=login_window["bg"]).place(x=100, y=10)


def define_login_button(login_window):
    login_button = Button(login_window, width=8, text="Login", command=lambda: destroy_window(login_window))
    login_button.place(x=400, y=250)


def add_user_and_password_text_box(login_window):
    username_label = Label(login_window, text="Username", bg=login_window["bg"], font=("Arial", 13))
    username_label.place(x=35, y=80)
    username_text = Text(login_window, height=1, width=20)
    username_text.place(x=120, y=80)
    password_label = Label(login_window, text="Password", bg=login_window["bg"], font=("Arial", 13))
    password_label.place(x=35, y=120)
    password_text = Text(login_window, height=1, width=20)
    password_text.place(x=120, y=120)


def destroy_window(login_window):
    login_window.destroy()