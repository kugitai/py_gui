import PySimpleGUI as sg
import random

layout = [[sg.Text('スロット')],
        [sg.Text(key='out1'),sg.Text(key='out2'),sg.Text(key='out3')],
        [sg.Button('stop1'),sg.Button('stop2'),sg.Button('stop3'),sg.Text(key='e_word')],
        [sg.Button('スタート')]]

window = sg.Window('ルーレット',layout)
#スロットが動作中か否か（falseは停止、trueは動作）
button = [False,False,False] 
#out1~3の初期値(同じ数字にならないようにランダムにしている)
out1 = random.randint(1,7)
out2 = random.randint(1,7)
out3 = random.randint(1,7)
#通常時の最小値
under_number = 1
while True:
    event,value = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'スタート':
        button = [True,True,True]
        window['e_word'].update('')
    
    if button[0]:
        window['out1'].update(random.randint(under_number, 7))
    
    if button[1]:
        window['out2'].update(random.randint(under_number, 7))
    
    if button[2]:
        window['out3'].update(random.randint(under_number, 7))
    

    if event == 'stop1':
        out1 = int(window['out1'].DisplayText)
        button[0] = False
    if event == 'stop2':
        out2 = int(window['out2'].DisplayText)
        button[1] = False
    if event == 'stop3':
        out3 = int(window['out3'].DisplayText)
        button[2] = False
    if not any(button):
        if out1 == out2 == out3:
            window['e_word'].update('大当たり！')
            window['out1'].update(text_color=("red"))
            window['out2'].update(text_color=("red"))
            window['out3'].update(text_color=("red"))
        elif out1 == out2 or out1 == out3 or out2 == out3:
            window['e_word'].update('リーチ')
            under_number = 5 #確率を上げるため１〜７を５〜７にする
            window['out1'].update(text_color=("yellow"))
            window['out2'].update(text_color=("yellow"))
            window['out3'].update(text_color=("yellow"))
        else:
            window['e_word'].update('')
            under_number = 1
            window['out1'].update(text_color=("white"))
            window['out2'].update(text_color=("white"))
            window['out3'].update(text_color=("white"))
    