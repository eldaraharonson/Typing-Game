import os

class TypingFile:
    def __init__(self, file_object):
        self.file_object = file_object
        self.pointer_on_file = 0

    def structure_text(self):
        pass

    def get_next_piece_of_text(self):
        text = ""
        for i in range(300):
            text += self.file_object.read(1)
        return text
