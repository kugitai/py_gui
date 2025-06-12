import PySimpleGUI as sg
import random

layout = [[sg.Text('どれぐらいでペカルかな？')],
        [sg.Text(key='result', size=(20, 1))],
        [sg.Text(key='count', size=(20, 1))],
        [sg.Button('Push')],[sg.Button('Reset')]]

window = sg.Window('ペカる', layout)
count = 0
while True:
    event, value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Push':
        result = random.randint(1, 100)
        if result <= 25:  # 10%の確率でペカる
            window['result'].update('ペカった！')
            count = 0
        else:
            window['result'].update('残念、ペカらなかった。')
        count += 1 
    window['count'].update(f'試行回数: {count}')