#backend.py
print("Hello world!")

import os
import datetime

class Note:
    def __init__(self, file_path=None):
        self.date = None
        self.time = None
        self.notes = None
        if file_path is None:
            pwd = os.getcwd()
            self.file_path = os.path.join(pwd, "notes.txt")
        else:
            self.file_path = file_path
    def create_note(self):
        self.date = datetime.datetime.now()
        self.notes = input("Input note: ")

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
        search_query = input("Enter search query: ").strip()
        
        # Handling empty search query
        if not search_query:
            print("Search query cannot be empty.")
            return

        with open(self.file_path, 'r') as file:
            notes = file.read().split("[End of note]\n")
            found_notes = False

        for note in notes:
            if search_query.lower() in note.lower():
                print(note.strip() + "\n[End of note]")
                found_notes = True
                # Continue to search through all notes instead of breaking after the first match
        
        if not found_notes:
            print("No notes found matching the query.")


    def clearNotes(self):
        f = open(self.file_path, "w")
        f.truncate()
        f.close()

    def replaceNotes(self, fileName):
            # Ensure the file is opened and closed properly using with statement
            with open(self.file_path, "r+") as f:
                with open(fileName, "r+") as inputFile:
                    f.truncate(0)  # Clear the file
                    lines = inputFile.readlines()
                    f.writelines(lines)

    
    def edit_note(self):
        search_query = input("Enter search term to find the note to edit: ")
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if search_query.lower() in line.lower():
                print(f"Found note: {line.strip()}")
                new_note = input("Enter the new note: ")
                lines[i] = f"{new_note}\n[End of note]\n"
                with open(self.file_path, 'w') as file:
                    file.writelines(lines)
                print("Note updated.")
                return
        print("No matching note found.")

    def delete_note(self):
        search_query = input("Enter search term to delete the note: ")
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        new_lines = []
        note_found = False
        skip_lines = False
        temp_lines = []

        for line in lines:
            if "Date:" in line:  # Start of a new note
                if note_found:  # If the previous note was the one to delete
                    print(''.join(temp_lines))  # Display the note
                    confirm = input("Are you sure you want to delete this note? (y/n): ")
                    if confirm.lower() == 'y':
                        skip_lines = True  # Confirm deletion
                        note_found = False  # Reset flag
                    else:
                        new_lines.extend(temp_lines)  # Keep the note
                        skip_lines = False  # Do not skip this note
                elif not skip_lines:  # If it's not the note to delete
                    new_lines.extend(temp_lines)
                temp_lines = [line]  # Start collecting lines for the new note
            elif search_query.lower() in line.lower() and not note_found:
                note_found = True  # Mark the note for potential deletion
            else:
                temp_lines.append(line)  # Add lines to the current note

        if note_found:  # Check the last note
            print(''.join(temp_lines))  # Display the note
            confirm = input("Are you sure you want to delete this note? (y/n): ")
            if confirm.lower() != 'y':
                new_lines.extend(temp_lines)  # Keep the note if not confirmed for deletion

        with open(self.file_path, 'w') as file:
            file.writelines(new_lines)

        print("Note deleted." if skip_lines else "No matching note found or deletion cancelled.")

    def append_to_note(self):
        search_query = input("Enter search term to find the note to append to: ")
        append_text = input("Enter text to append: ")
        with open(self.file_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                file.write(line)
                if search_query.lower() in line.lower():
                    file.write(f"{append_text}\n")
            print("Text appended to note.")

    def export_notes(self, export_file_name):
        with open(self.file_path, 'r') as file:
            notes = file.read()
        with open(export_file_name, 'w') as export_file:
            export_file.write(notes)
        print(f"Notes exported to {export_file_name}.")

    def import_notes(self, import_file_name):
        with open(import_file_name, 'r') as import_file:
            notes_to_import = import_file.read()
        with open(self.file_path, 'a') as file:
            file.write(notes_to_import)
        print(f"Notes imported from {import_file_name}.")

