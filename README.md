# CS 230
## Spring 24
### Musgrave
#### 60 points

##### Project 1
Build a local note-taking app. The app should manage taking notes locally as a command-line tool. The app should store notes, retrieve them, print the notes, and search the notes. Work with your partners in teams of 2 people. Using Git for tracking changes is required.

///////////////////////////////

The frontend.py file contains a menu where you select an option and enter in parameters if
necessary. The program will then call the corresponding function in the backend.py file.

///////////////////////////////

* The backend.py file contains functions for creating and viewing notes from a text file.
* If the file itself is run, it will simply display "Hello World!". It is meant to contain
functions that are called by frontend.py.
* The file consists of a single "note" class, which contains the following:
    * A constructor that initializes empty variables to contain the date, time, notes, and
    filepath of the receiving text file
    * 12 options with 11 associated functions:
        1. Create a new note (Drew)
        2. View notes (Drew)
        3. Search notes (Balti)
        4. Clear notes (Riker)
        5. Replace notes (Riker)
        6. Edit a note (Balti)
        7. Delete a specific note (Balti)
        8. Append to an existing note (Balti)
        9. Export notes (Balti)
        10. Import notes (Balti)
        11. Help (Drew)
        12. Exit (No associated function)

        * Additional functionality for functions 5, 9 & 10 by Riker
        * Additional research and assistance by Kunga