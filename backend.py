# Riker and Drew
print("Hello world!")

def viewNotes():
    f = open("notes.txt", "r")
    lines = len(f.readlines())
    f.seek(0)
    for line in f:
        print(line)

viewNotes()