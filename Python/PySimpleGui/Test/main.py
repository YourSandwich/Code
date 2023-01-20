import PySimpleGUI as sg

layout = [
        [sg.Text('Test Application')],
        [sg.Button('Calculate', key = 'Button1')],
        [sg.Input()],
]

window = sg.Window('lol', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Button1':
        print('Button Pressed')

window.close()
