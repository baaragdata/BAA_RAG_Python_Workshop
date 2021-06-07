''' RA GUI COntrol '''

import PySimpleGUI as sg

import serial

pi = serial.Serial('COM6', 9600)

layout = [ [sg.Text('Motor Control'), sg.Text('', key='-OUTPUT-')],
            [sg.RealtimeButton('<', size=(10,5)), sg.RealtimeButton('STOP', size=(10,5)), sg.RealtimeButton('>', size=(10,5))],
            [sg.Slider((22000,65535), key='SLIDER', orientation='h', enable_events=True, disable_number_display=False), sg.Button("SET SPEED")],
            [sg.Button('Exit')]
            ]

window = sg.Window('Remote Motor Control', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == '<':
        pi.write(b'<\r\n')
    elif event == '>':
        pi.write(b'>\r\n')
    elif event == 'STOP':
        pi.write(b'STOP\r\n')
    elif event == 'SET SPEED':
        pi.write('SPEED,{:.0f}\r\n'.format(abs(values['SLIDER'])).encode())


window.close()