# Riker and Drew
print("Hello world!")

import os

class note:
    def __init__(self, date, time, notes):
        self.date = date
        self.time = time
        self.notes = notes

    def save_info(self):
        # Check if the file exists. If not, create it.
        if not os.path.exists(self.file_path):
            open(self.file_path, 'w').close()  # This creates the file if it doesn't exist.

        with open(self.file_path, 'a') as file:
            file.write(f"Date: {self.name}\n")
            file.write(f"Last Name: {self.lName}\n")
            file.write(f"Birthday: {self.birthday}\n")
            file.write(f"Major: {self.major}\n")
            file.write(f"Favorite Colour: {self.favoriteColor}\n")
            file.write(f"Movie: {self.movies}\n\n")
    
    def create_note():
        print("hello world")