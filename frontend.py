#frontend.py
import os
from backend import Note

current_dir = os.path.dirname(os.path.abspath(__file__))
# Constructs the path to the text file, assuming it's in the same directory
replace_test_path = os.path.join(current_dir, 'replace_test.txt')


class NoteTakingApp:
    def __init__(self):
        self.notes = []  # Placeholder for notes storage

    def display_menu(self):
        print("Welcome to the Note-Taking App")
        print("1. Create a new note")
        print("2. View notes")
        print("3. Search notes")
        print("4. Clear notes")
        print("5. Replace notes")
        print("6. Edit a note")
        print("7. Delete a specific note")
        print("8. Append to an existing note")
        print("9. Export notes")
        print("10. Import notes")
        print("11. Help")
        print("12. Exit")
        choice = input("Enter your choice: ")
        return choice

    def run(self):
        note1 = Note()
        while True:
            choice = self.display_menu()
            if choice == '1':
                note1.create_note()
            elif choice == '2':
                note1.view_notes()
            elif choice == '3':
                note1.search_notes()
            elif choice == '4':
                note1.clearNotes()
            elif choice == '5':
                fileName = input("Enter the file name to replace notes with: (enter ``Cancel`` to exit)")
                note1.replaceNotes(fileName)
            elif choice == '6':
                note1.edit_note()
            elif choice == '7':
                note1.delete_note()
            elif choice == '8':
                note1.append_to_note()
            elif choice == '9':
                export_file_name = input("Enter the file name to export notes to: (enter ``Cancel`` to exit)")
                note1.export_notes(export_file_name)
            elif choice == '10':
                import_file_name = input("Enter the file name to import notes from: (enter ``Cancel`` to exit)")
                note1.import_notes(import_file_name)
            elif choice == '11':
                Hchoice = input("Which option do you need help with?\n")
                note1.help(Hchoice)
            elif choice == '12':
                print("Thank you for using the Note-Taking App.")
                break
            else:
                print("Invalid choice. Please try again.")

# To run the application
if __name__ == "__main__":
    app = NoteTakingApp()
    app.run()
