# CS 230
## Spring 24
### Musgrave
#### 60 points

##### Project 1
Build a local note-taking app. The app should manage taking notes locally as a command-line tool. The app should store notes, retrieve them, print the notes, and search the notes. Work with your partners in teams of 2 people. Using Git for tracking changes is required.

///////////////////////////////

Potential features
1. Create different files to contain notes
2. Each note taken should contain the date and time when it was created
3. Create different directories for different subjects, days, etc.
4. A files's contents should be searchable and results should print the corresponding note(s) and their date/time

stretch features:
1. specify filepath
2. Editing previous notes (Dr. Musgrave advises against this)

Frontend: Balti & Kunga
Backend: Drew & Riker

///////////////////////////////

The frontend.py file 

///////////////////////////////

* The backend.py file contains functions for creating and viewing notes from a text file.

* If the file itself is run, it will simply display "Hello World!". It is meant to contain
functions that are called by frontend.py.

* The file consists of a single "note" class, which contains the following:

    * A constructor that initializes empty variables to contain the date, time, notes, and
    filepath of the receiving text file

    * create_note(self), which gets the current system time, asks the user to input a note,
    opens a file (creating one if it didn't already exist), and writing to it.

    * view_notes(self), which prints the text file

    * search_notes(self), which doesn't do anything yet