import PySimpleGUI as sg

layout = [[sg.Text('test')]]

window = sg.Window('roulette',layout)

while True:
    event,value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
