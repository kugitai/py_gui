import PySimpleGUI as sg
import random

layout = [[sg.Text('スロット')],
        [sg.Text(key='out1'),sg.Text(key='out2'),sg.Text(key='out3')],
        [sg.Button('stop1'),sg.Button('stop2'),sg.Button('stop3'),sg.Text(key='e_word')],
        [sg.Button('スタート')]]

window = sg.Window('ルーレット',layout)
start = [False,False,False]
out1 = 0
out2 = 0
out3 = 0
under_number = 1
while True:
    event,value = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'スタート':
        start = [True,True,True]
        window['e_word'].update('')
    
    if start[0]:
        window['out1'].update(random.randint(under_number, 7))
    if start[1]:
        window['out2'].update(random.randint(under_number, 7))
    if start[2]:
        window['out3'].update(random.randint(under_number, 7))

    if event == 'stop1':
        out1 = int(window['out1'].DisplayText)
        start[0] = False
    if event == 'stop2':
        out2 = int(window['out2'].DisplayText)
        start[1] = False
    if event == 'stop3':
        out3 = int(window['out3'].DisplayText)
        start[2] = False
    if not any(start):
        if out1 == out2 == out3:
            window['e_word'].update('大当たり！')
        elif out1 == out2 or out1 == out3 or out2 == out3:
            window['e_word'].update('リーチ')
            under_number = 5
        else:
            window['e_word'].update('')
            under_number = 1
    