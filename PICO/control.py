import PySimpleGUI as sg
import time
import serial

layout = [[sg.Text('Motor Control'), sg.Text('', key='-OUTPUT-')],
        [sg.RealtimeButton('<', size=(10,5), ), sg.RealtimeButton('STOP', size=(10,5)), sg.RealtimeButton('>', size=(10,5))],
        [sg.Slider((0,65535), key='SLIDER', orientation='h', enable_events=True, disable_number_display=False), sg.Button("SET SPEED")],
        [sg.Button('Exit')]]

window = sg.Window('Remote Motor Control', layout)

pi = serial.Serial('COM6', 9600)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '<':
        #sg.popup(f'The slider value = {values["-SLIDER-"]}')
        pi.write(b'<\r\n')
    elif event == '>':
        pi.write(b'>\r\n')
    elif event == 'STOP':
        pi.write(b'STOP\r\n')
    elif event == 'SET SPEED':
        pi.write('SPEED,{:.0f}\r\n'.format(abs(values['SLIDER'])).encode())

window.close()