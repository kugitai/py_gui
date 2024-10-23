import PySimpleGUI as sg
import datetime
layout = [[sg.Text('ここに年齢が出ます',key='output')],
          [sg.Text('生年月日をお願いします')],
          [sg.Input(key='berthyear',size=('4','16')),sg.I(key='berthmonth',size=('1','4')),sg.I(key='berthday',size=('1','4'))],
          [sg.Button('年齢確認')]]
window = sg.Window('年齢',layout)
now_year = datetime.datetime.now().year
now_month = datetime.datetime.now().month
now_day = datetime.datetime.now().day
print(now_year,now_month,now_day)
while True:
    event,value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if value['berthyear'] == '' or len(value['berthyear']) < 3:
        window['output'].update('生まれた年を「西暦」で入力して下さい')
        continue
    if int(value['berthyear']) <= 0:
        window['output'].update('正の値をいれてください')
        continue
    old = now_year - int(value['berthyear'])
    if int(value['berthmonth']) > now_month:
        old-=1
    if int(value['berthmonth']) == now_month and int(value['berthday']) > now_day:
        old-=1
    if old < 0:
        window['output'].update('現在の年数を超える数値は入れないでください')
        continue
    window['output'].update(f'年齢は{old}歳です')
