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
        temp_lines = []  # Temporary storage for current note being checked
        note_found = False  # Flag to indicate if the note to delete has been found
        for line in lines:
            if "Date:" in line:  # Marks the start of a new note
                if note_found:  # If the previous note was marked for deletion, ask for confirmation
                    print(''.join(temp_lines), end='')  # Print the note for review
                    confirm = input("Are you sure you want to delete this note? (y/n): ")
                    if confirm.lower() == 'y':
                        note_found = False  # Note is deleted, so reset the flag and do not add temp_lines to new_lines
                        continue  # Skip adding this note's lines to new_lines
                # If not deleting, add the accumulated lines for the previous note to new_lines
                if not note_found:
                    new_lines.extend(temp_lines)
                temp_lines = [line]  # Start accumulating lines for the new note
            else:
                temp_lines.append(line)
                if search_query.lower() in line.lower() and not note_found:
                    note_found = True  # Mark this note for potential deletion

        # After the loop, check if the last note was marked for deletion and ask for confirmation
        if note_found:  # This handles the case where the last note in the file was marked for deletion
            print(''.join(temp_lines), end='')  # Print the last note
            confirm = input("Are you sure you want to delete this note? (y/n): ")
            if confirm.lower() != 'y':
                new_lines.extend(temp_lines)  # If not deleting, add the last note's lines to new_lines

        with open(self.file_path, 'w') as file:
            file.writelines(new_lines)

        print("Note deleted." if note_found else "No matching note found or deletion cancelled.")

    def append_to_note(self):
        while True:
            search_query = input("Enter search term to find the note to append to: ")
            append_text = input("Enter text to append: ")
            note_found = False
            append_position = None

            with open(self.file_path, 'r+') as file:
                lines = file.readlines()
                file.seek(0)

                for i, line in enumerate(lines):
                    if search_query.lower() in line.lower():
                        note_found = True
                        print(''.join(lines[i:i+3]))  # Adjust according to your note structure
                        confirm = input("Is this the note you want to append to? (y/n): ")
                        if confirm.lower() == 'y':
                            append_position = i  # Mark position to append text
                            break
                        else:
                            print("Let's try again.")
                            break  # Break out to search again based on new input
                
                if not note_found:
                    print("No matching note found. Please try again.")
                    continue  # Continue asking for a new search term
                elif append_position is not None:
                    # Append text to the confirmed note
                    for j, line in enumerate(lines):
                        if j == append_position:
                            lines[j] = line.rstrip('\n') + " " + append_text + "\n"  # Append text to the note line

                    file.seek(0)  # Go back to the start of the file
                    file.truncate(0)  # Clear the file
                    file.writelines(lines)  # Write the modified lines back to the file
                    print("Text appended to note.")
                    break  # Exit the loop if the note to append to has been confirmed


        
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

