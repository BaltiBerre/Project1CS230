from backend import note

class NoteTakingApp:
    def __init__(self):
        self.notes = []  # Placeholder for notes storage

    def display_menu(self):
        print("Welcome to the Note-Taking App")
        print("1. Create a new note")
        print("2. View notes")
        print("3. Search notes")
        print("4. Exit")
        choice = input("Enter your choice: ")
        return choice

    def run(self):
        while True:
            note1 = note()

            choice = self.display_menu()
            if choice == '1':
                note1.create_note()
            elif choice == '2':
                note1.view_notes()
            elif choice == '3':
                note1.search_notes()
            elif choice == '4':
                print("Thank you for using the Note-Taking App.")
                break
            else:
                print("Invalid choice. Please try again.")

# To run the application
if __name__ == "__main__":
    app = NoteTakingApp()
    app.run()
