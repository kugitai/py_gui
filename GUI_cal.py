import PySimpleGUI as sg
layout = [[sg.Text(key='output')],
          [sg.Button('AC')],
          [sg.Text('一つ目の数字は？')],
          [sg.Input(key=('num1'))],
          [sg.Text('二つ目の数字は？')],
          [sg.Input(key=('num2'))],
          [sg.Text('+,-,*,/を選んでください')],
          [sg.Button('+'),sg.Button('-'),sg.Button('×'),sg.Button('÷')]]
window = sg.Window('計算機',layout)
while True:
    try:
        event,value = window.read()
        d = 0
        if event == '+':
            d = (float(value['num1'])+float(value['num2']))
        elif event == '-':
            d = (float(value['num1'])-float(value['num2']))
        elif event == '×':
            d = (float(value['num1'])*float(value['num2']))
        elif event == '÷':
            d = (float(value['num1'])/float(value['num2']))
        window['output'].update(f'答えは{d}です')
        if event == 'AC':
            window['num1'].update('')
            window['num2'].update('')
        if event == sg.WINDOW_CLOSED:
            break
    except ZeroDivisionError:
        window['output'].update('0では割れません')
    except ValueError:
        window['output'].update('数字を入力してください')