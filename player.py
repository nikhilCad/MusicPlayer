#import pysimplegui
#do magical stuff
#profit

import PySimpleGUI as sg
import os
import playsound


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
filePaths = []
def play(path):
    #We have the folder now do something with it
    
    print(path)

    for file in os.listdir(path):
        for extension in musicPaths:
            if file.endswith(extension):
                filePaths.append(os.path.join(path, file))
    
    for i in filePaths:
        playsound(i)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        play(values["-IN-"])
    
window.close()