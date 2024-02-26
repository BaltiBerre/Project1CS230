# Riker and Drew
print("Hello world!")

import os
import datetime

class note:
    def __init__(self):
        self.date = None
        self.time = None
        self.notes = None
        #self.file_path = "C:\\Users\\atbfi\\Development\\Project1CS230\\notes.txt"
        self.file_path = None
    
    def create_note(self):
        self.date = datetime.datetime.now()
        self.notes = input("Input note: ")
        f = open("notes.txt", "a")
        f.close()

        #self.file_path = Path.cwd()
        self.file_path = os.path.abspath(notes.txt)

        # Check if the file exists. If not, create it.
        if not os.path.exists(self.file_path):
            open(self.file_path, 'w').close()  # This creates the file if it doesn't exist.

        with open(self.file_path, 'a') as file:
            file.write(f"Date: {self.date.month}/{self.date.day}/{self.date.year}\n")
            file.write(f"Time: {self.date.hour}:{self.date.minute}\n")
            file.write(f"{self.notes}\n")
            file.write(f"[End of note]\n")

    def view_notes(self):
        print("Viewing all notes:\n")
        with open(self.file_path, 'r') as file:
            file.seek(0)
            for line in file:
                print(line)

    def search_notes(self):
        print("Function unavailable")
