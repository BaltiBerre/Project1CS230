# CS 230
## Spring 24 | Project 1
##### Balti, Andrew, Riker, Kunga

Project Instructions

Build a local note-taking app. The app should manage taking notes locally as a command-line tool. The app should store notes, retrieve them, print the notes, and search the notes. Work with your partners in teams of 2 people. Using Git for tracking changes is required.

Frontend : Balti, Kunga
Backend : Andrew, Riker

---
#### How to use

1. **Setup Environment**: Make sure Python is installed on your machine.

2. **Run** **`backend.py`** :  Navigate to the project's directory in your terminal or command prompt and execute the script by running:


    ```
    python backend.py
    ```

---
#### Features 

The frontend.py file contains a menu where you select an option and enter in parameters if
necessary. 

The program will then call the corresponding function in the backend.py file. The backend.py file contains functions for creating and viewing notes from a text file.

* The file consists of a single "note" class, which contains the following:
    * A constructor that initializes empty variables to contain the date, time, notes, and file path of the receiving text file
    * 12 options with 11 associated functions:
        1. Create a new note (Drew)
	        - If no prior notes exists, creates a new notes.txt file in current directory and adds the new note.
	        - Adds new note to the notes.txt.
        2. View notes (Drew)
			- Displays all notes, along with the data and time the notes were created at. 
        3. Search notes (Balti)
	         - Prompts user for a search query and displays the desired note.
	         - Displays an error if no similar note is found in notes.txt
        4. Clear notes (Riker)
			- Erases all notes.
        5. Replace notes (Riker)
	        - Takes in a note file and overwrites it onto the current note file.
        6. Edit a note (Balti)
	        - Prompts user for a search query, and takes in input for texts to replace it.
        7. Delete a specific note (Balti)
			-  Prompts user for a search query, displays the desired note and prompts the user asking them if they want to delete it or not.
        8. Append to an existing note (Balti)
	        - Prompts user for a search query, and takes in input for texts to append at the end.
        9. Export notes (Balti)
		    - Exports the content of notes to any other text file specified in the directory.
        10. Import notes (Balti)
	        - Imports the content of notes from any other text file specified in the directory.
        11. Help (Drew)
	        - Provides explanation to each function.
        12. Exit (No associated function)
		    - Exits the program
        * Additional functionality for functions 5, 9 & 10 by Riker
        * Additional research and assistance by Kunga