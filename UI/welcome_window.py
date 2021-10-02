from tkinter import *
from UI.TypingFile import *
import UI.play_window
import UI.login
from easygui import fileopenbox
import time


letter_of_index = 0

# entry point
def start_game():
    # UI.login.create_login_window()
    welcome_window = Tk()
    define_window_style(welcome_window)
    add_pick_file_widgets(welcome_window)
    # UI.play_window.initialize_play_window()
    welcome_window.mainloop()


def define_window_style(welcome_window):
    welcome_window.title("Login")
    welcome_window.geometry("600x300")
    welcome_window["bg"] = "light blue"
    Label(welcome_window, text="Welcome to Typing Game!", bg="light blue", font=("Helvetica", 25)).place(x=120, y=0)


def add_pick_file_widgets(welcome_window):
    pick_file_label = Label(welcome_window, text="Pick a text file from your file explorer to practice typing from",
                            bg=welcome_window["bg"], font=("Helvetica", 15))
    pick_file_label.place(x=40, y=100)
    pick_file_button = Button(welcome_window, text="Choose Text File", font=("Helvetica", 10),
                              command=lambda: pick_file(welcome_window))
    pick_file_button.place(x=250, y=250)


def pick_file(welcome_window):
    # file_name = fileopenbox()

    file_name = "songs/Brain Damage.txt"

    with open(file_name) as file_to_type:
        typing_file = TypingFile(file_to_type)
        UI.play_window.initialize_play_window(typing_file, welcome_window)















