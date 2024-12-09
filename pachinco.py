import PySimpleGUI as sg
import random
import time;

layout = [[sg.Text('P NIT Light'),sg.Text(key = 'count'),sg.Text(key='hit_count'),sg.Text(key='hit_intv')],
          [sg.Text(key='out1'),sg.Text(key='out2'),sg.Text(key='out3')],
          [sg.Text(key='e_word')],
          ]

window = sg.Window('P NIT Light',layout,size=(200,100))
count = 0 #現在の回転数
prev_hit_count = 0  # 前回の大当たり時の回転数
hit_count = 0 # 最後の大当たり時の回転数
hit_intv = 0 #大当たりの間隔
hit_num = random.randint(1,99) 
#あたりの数(テスト時以外はランダム)

while True:
    event,value = window.read(timeout=500)
    rand_num =  random.randint(1,99) #これがあたりの数に合致すれば大当たり
    if event == sg.WINDOW_CLOSED:
        break
    #大当たり時の処理
    if (hit_num == rand_num):
        window['out1'].update('7')
        window['out2'].update('7')
        window['out3'].update('7')
        prev_hit_count = hit_count  # 現在の大当たり回転数を前回値に保存
        hit_count = count  # 現在の回転数を最後の大当たり回転数に更新
        hit_intv = hit_count - prev_hit_count  # 大当たり間隔を計算
    else:
        window['out1'].update(random.randint(1,3))
        window['out2'].update(random.randint(4,6))
        window['out3'].update(random.randint(7,9))

    window['count'].update(count)
    window['hit_count'].update(hit_count)
    window['hit_intv'].update(hit_intv)
    count +=1