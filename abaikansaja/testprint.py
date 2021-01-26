import PySimpleGUI as sg
import time


layout = [
    [sg.Text('Information:', size=(40, 1))],
    [sg.Output(key='atas', size=(88, 20))],
    [sg.Output(key='bawah', size=(88, 20))],
    [sg.Text('Input:', size=(15, 1)), sg.InputText(key='inputan'), sg.Button('Run', bind_return_key=True)],
    [sg.Button('EXIT')]
]

window = sg.Window('testing', layout)

# ---===--- Loop taking in user input and using it to call scripts --- #

while True:
    (event, value) = window.Read()
    if event == 'EXIT' or event is None:
        break  # exit button clicked
    # if event == 'Run':
    window['atas'].update(value['inputan'])
    window['bawah'].update(value['inputan'])

window.Close()
