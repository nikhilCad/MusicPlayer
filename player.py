#import pysimplegui
#do magical stuff
#profit

import PySimpleGUI as sg
import os


layout = [
            [sg.T("")],
            [
                sg.Text("Choose a folder: "), 
                sg.Input(key="-IN2-" ,change_submits=True), 
                sg.FolderBrowse(key="-IN-")
            ],
            [sg.Button("Submit")
            ]
        ]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,150))

#.m4a .webm . mp3
musicPaths = [".m4a", ".mp3", ".webm"]

def play(path):
    #We have the folder now do something with it
    
    print(path)

    for file in os.listdir(path):
        for extension in musicPaths:
            if file.endswith(extension):
                print(os.path.join(path, file))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        play(values["-IN-"])
    
window.close()