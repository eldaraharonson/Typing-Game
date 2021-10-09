import mysql.connector

from tkinter import *
from tkinter import messagebox


def connect_to_database():
    db = mysql.connector.connect(host="localhost", user="root", password="prince1995",
                                 database="typing_game_database")
    my_cursor = db.cursor()
    return my_cursor


def add_new_user(username_text, password_text):
    db = mysql.connector.connect(host="localhost", user="root", password="prince1995",
                                 database="typing_game_database")
    my_cursor = db.cursor()
    query = "INSERT INTO Player (name, password) VALUES (%s, %s)"
    args = (username_text, password_text)
    my_cursor.execute(query, args)
    db.commit()


def check_user_credentials(username, password):
    db = mysql.connector.connect(host="localhost", user="root", password="prince1995",
                                 database="typing_game_database")
    my_cursor = db.cursor()
    my_cursor.execute("SELECT name FROM Player")
    for name in my_cursor:
        if name[0] == username:
            my_cursor.execute("SELECT password FROM Player WHERE name = '" + username + "'")
            if my_cursor != password:
                messagebox.showerror(message="Wrong Password")
            else:
                # login to that user
                pass
            return

    messagebox.showerror(message="Username doesn't exist in database")


