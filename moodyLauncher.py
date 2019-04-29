from subprocess import Popen
import os
import sys
import re

def listAllFiles():
    files = [f for f in os.listdir(os.curdir) if (
        os.path.isfile(f) and f.endswith(".txt"))]
    return files

def take_user_inputs():
    print('0. Stop')
    print('1. Create new mood')
    for file in enumerate(listAllFiles()):
        print(str(file[0]+2) + ". " + file[1])
    var = str(input('\nEnter your input: '))
    if (var == '0'):
        print("Script terminated")
        sys.exit()
    elif (var == '1'):
        createNewMood()
    else:
        openPrograms(listAllFiles()[int(var) - 2])


def openPrograms(fileName):
    apps = open(str(fileName), "r").readlines()
    for app in apps:
        if app:
            app = app.replace("\n", "")
            Popen(app.encode('string-escape'))

    print("Script terminated")
    sys.exit()

def createNewMood():
    fileName = raw_input('Enter new mood name(Example: Web Development):')
    strs = ""

    while True:
        print('Your inputs:\n'+strs)
        program = str(raw_input('Drag executable file or input 0 to stop:\n'))
        if (program == '0'):
            file = open(str(fileName) + '.txt', "w+")
            file.write(strs)
            print('Saved ' + str(fileName) + ' mood')
            file.close()
            break
        else:
            strs = strs + program.replace('\"', "") + '\n'
    print('\n')
    take_user_inputs()


# starts from here
take_user_inputs()
