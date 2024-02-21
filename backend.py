# Riker and Drew
print("Hello world!")

def viewNotes():
    f = open("notes.txt", "r")
    lines = len(f.readlines())
    f.seek(0)
    for line in f:
        print(line)
    f.close()


def clearNotes():
    f = open("notes.txt", "w")
    f.truncate()
    f.close()

def replaceNotes(fileName):
    f = open("notes.txt", "r+")
    InputFile = open(fileName, "r+")
    f.truncate(0)
    lines = InputFile.readlines()
    f.writelines(lines)
    InputFile.close()

