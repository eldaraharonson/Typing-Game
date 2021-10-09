from tkinter import *
import mysql.connector
import database_managment.logic as db_logic

login_window = Tk()
username_text = Entry(login_window, width=25)
password_text = Entry(login_window, width=25)
var = IntVar()
new_user_selection = Radiobutton(login_window, text="New User", variable=var, value=1, bg="light blue").place(x=400, y=100)
new_user_selection = Radiobutton(login_window, text="Login", variable=var, value=2, bg="light blue").place(x=400, y=120)
var.set(2)

def create_login_window():
    # connect_to_database()
    global login_window
    define_window_style(login_window)
    add_labels(login_window)
    define_login_button(login_window)
    add_user_and_password_text_box(login_window)
    login_window.mainloop()


# I already created an empty database named typing_game_database
def connect_to_database():
    db = mysql.connector.connect(host="localhost", user="root", password="prince1995",
                                 database="typing_game_database")
    my_cursor = db.cursor()
    # my_cursor.execute("CREATE TABLE Player (ID INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(50), "
    #                   "average_typing_speed FLOAT(6, 2), average_errors_per_300_chars FLOAT(4, 1), A INT, B INT, C INT, "
    #                   "D INT, E INT, F INT, G INT, H INT, I INT, J INT, K INT, L INT, M INT, N INT, O INT, P INT,"
    #                   " Q INT, R INT, S INT, T INT, U INT, V INT, W INT, X INT, Y INT, Z INT)")
    my_cursor.execute("DESCRIBE Player")
    for x in my_cursor:
        print(x)


def define_window_style(login_window):
    login_window.title("Login")
    login_window.geometry("550x300")
    login_window["bg"] = "light blue"


# if user already in db then login, if not create new user with the password
def add_labels(login_window):
    Label(text="Welcome to Speed Typing!!", font=("Arial", 18), bg=login_window["bg"]).place(x=100, y=10)
    Label(text="If you don't have a user a new one will be created for you with your password",
          font=("Arial", 12), bg=login_window["bg"]).place(x=10, y=200)


def define_login_button(login_window):
    login_button = Button(login_window, width=8, text="Login", command=lambda: destroy_window(login_window))
    # login_button = Button(login_window, width=8, text="Login", command=lambda: db_logic.check_user_credentials(login_window))
    login_button.place(x=450, y=250)


def add_user_and_password_text_box(login_window):
    username_label = Label(login_window, text="Username", bg=login_window["bg"], font=("Arial", 13))
    username_label.place(x=35, y=80)
    global username_text
    username_text.place(x=120, y=80)
    password_label = Label(login_window, text="Password", bg=login_window["bg"], font=("Arial", 13))
    password_label.place(x=35, y=120)
    global password_text
    password_text.place(x=120, y=120)


# login or create new user
def destroy_window(login_window):
    # db = mysql.connector.connect(host="localhost", user="root", password="prince1995",
    #                              database="typing_game_database")
    # my_cursor = db.cursor()
    # my_cursor.execute("SELECT * FROM Player")
    # for x in my_cursor:
    #     print(x)

    global username_text
    global password_text
    global var
    print(username_text.get())

    if var.get() == 1:
        db_logic.add_new_user(username_text.get(), password_text.get())
    else:
        db_logic.check_user_credentials(username_text.get(), password_text.get())
    # login_window.destroy()


