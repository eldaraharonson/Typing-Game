from tkinter import *
import UI.play_window
import UI.login
from easygui import fileopenbox
import time


letter_of_index = 0


def start_game():
    UI.play_window.initialize_play_window()
    # UI.login.create_login_window()
    #welcome_window = Tk()
    #define_window_style(welcome_window)
    # add_pick_file_widgets(welcome_window)
    #welcome_window.mainloop()


def define_window_style(welcome_window):
    pass



#
#
# def add_pick_file_widgets(welcome_window):
#     pick_file_label = Label(welcome_window, text="Pick a text file to practice typing from", bg=welcome_window["bg"], font=("Helvetica", 15))
#     pick_file_label.place(relx=0.05, rely=0.3)
#     pick_file_button = Button(welcome_window, text="Choose Text File", command=lambda: pick_file(welcome_window))
#     pick_file_button.place(relx=0.4, rely=0.305)


def pick_file(welcome_window):
    # file_name = fileopenbox()

    file_name = "at_your_age.txt"
    for widget in welcome_window.winfo_children():
        widget.destroy()
    Label(welcome_window, text="Start typing!", bg=welcome_window["bg"], font=("Helvetica", 25)).pack()


    with open(file_name) as file_to_type:
        pass














