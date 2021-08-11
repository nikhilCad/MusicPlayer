#import pysimplegui
#do magical stuff
#profit

import PySimpleGUI as sg

layout = [
[sg.T("Hello"*10)]

]

window = sg.Window("Window layout", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()