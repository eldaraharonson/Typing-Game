from tkinter import *
import keyboard
import UI.login
from easygui import fileopenbox
import time


letter_of_index = 0


def start_game():
    # UI.login.create_login_window()
    welcome_window = Tk()
    define_window_style(welcome_window)


    add_pick_file_widgets(welcome_window)
    list_of_letter_labels = add_text_for_typing(welcome_window)
    welcome_window.bind("<KeyPress-Shift_L>", lambda event: analyze_shift_press(event, list_of_letter_labels))
    welcome_window.bind("<KeyPress-Shift_R>", lambda event: analyze_shift_press(event, list_of_letter_labels))
    welcome_window.bind("<Key>", lambda event: analyze_key_press(event, list_of_letter_labels))

    welcome_window.mainloop()
    # start_typing(welcome_window, list_of_letter_labels)


def define_window_style(welcome_window):
    welcome_window.rowconfigure((0, 1, 2, 3, 4), weight=1)
    welcome_window.columnconfigure((0, 1, 2, 3, 4), weight=1)
    welcome_window.title("Type Master")
    welcome_window.geometry("1000x500")
    welcome_window["bg"] = "light blue"
    Label(welcome_window, text="Type!", bg="light blue", font=("Helvetica", 30)).place(x=440, y=0)


def analyze_shift_press(event, letter_labels):
    while keyboard.is_pressed("shift"):
        if keyboard.read_key():
            break


def analyze_key_press(event, letter_labels):
    global letter_of_index
    if event.char == letter_labels[letter_of_index].cget("text"):
        letter_labels[letter_of_index]["bg"] = "lawn green"
    else:
        letter_labels[letter_of_index]["bg"] = "tomato"
    letter_of_index += 1


def add_pick_file_widgets(welcome_window):
    pick_file_label = Label(welcome_window, text="Pick a text file to practice typing from", bg=welcome_window["bg"], font=("Helvetica", 15))
    pick_file_label.place(relx=0.05, rely=0.3)
    pick_file_button = Button(welcome_window, text="Choose Text File", command=lambda: pick_file(welcome_window))
    pick_file_button.place(relx=0.4, rely=0.305)


def pick_file(welcome_window):
    # file_name = fileopenbox()

    file_name = "at_your_age.txt"
    for widget in welcome_window.winfo_children():
        widget.destroy()
    Label(welcome_window, text="Start typing!", bg=welcome_window["bg"], font=("Helvetica", 25)).pack()


    with open(file_name) as file_to_type:
        pass


def add_text_for_typing(welcome_window):
    frame = Frame(welcome_window, width=950, height=430, bg="light blue")
    frame.grid(row=1, column=0)
    text = "Hello my name is Eldar, and this is my typing game. I hope you enjoy it."
    list_of_letter_labels = []
    for letter in text:
        label_of_letter = Label(frame, text=letter, bg=welcome_window["bg"], font=("Helvetica", 18))
        list_of_letter_labels.append(label_of_letter)
    current_column = 0
    current_row = 1
    for i, label_letter in enumerate(list_of_letter_labels):
        if current_column >= 25 and list_of_letter_labels[i - 1].cget("text") == ' ':
            current_row += 1
            current_column = 0
        label_letter.grid(row=current_row, column=current_column)
        current_column += 1
    return list_of_letter_labels











