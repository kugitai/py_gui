import PySimpleGUI as sg
layout = [[sg.Text(' パスワードを設定してください')],
          [sg.Input(key='inputps')],
          [sg.Text('パスワードを入力してください')],
          [sg.Input(key='ps')],
          [sg.Button('OK')],
          [sg.Text(key='output')]]
window = sg.Window('password',layout)
while True:
    event,value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'OK':
        if value['inputps'] == value['ps']:
            window['output'].update('認証されました')
        else:
            window['output'].update('パスワードが異なります')

    
