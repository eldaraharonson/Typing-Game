from tkinter import *
import keyboard

letter_of_index = 0


def initialize_play_window():
    play_window = Tk()
    define_window_style(play_window)
    list_of_letter_labels = add_text_for_typing(play_window)
    config_typing_actions(play_window, list_of_letter_labels)
    play_window.mainloop()


def define_window_style(play_window):
    play_window.rowconfigure((0, 1, 2, 3, 4), weight=1)
    play_window.columnconfigure((0, 1, 2, 3, 4), weight=1)
    play_window.title("Type Master")
    play_window.geometry("1000x500")
    play_window["bg"] = "light blue"
    Label(play_window, text="Type!", bg="light blue", font=("Helvetica", 30)).place(x=440, y=0)


def config_typing_actions(play_window, list_of_letter_labels):
    play_window.bind("<KeyPress-Shift_L>", lambda event: analyze_shift_press(event, list_of_letter_labels))
    play_window.bind("<KeyPress-Shift_R>", lambda event: analyze_shift_press(event, list_of_letter_labels))
    play_window.bind("<Key>", lambda event: analyze_key_press(event, list_of_letter_labels))


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


def add_text_for_typing(play_window):
    frame = Frame(play_window, width=950, height=430, bg="light blue")
    frame.grid(row=1, column=0)
    text = "Hello my name is Eldar, and this is my typing game. I hope you enjoy it."
    list_of_letter_labels = []
    for letter in text:
        label_of_letter = Label(frame, text=letter, bg=play_window["bg"], font=("Helvetica", 18))
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

