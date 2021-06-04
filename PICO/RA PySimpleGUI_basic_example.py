import PySimpleGUI as sg

layout = [[sg.Text('Enter a Number')],
          [sg.Input()],
          [sg.OK()] ]

window = sg.Window('Enter a number example', layout)

event, values = window.read()

window.close()

sg.Popup(event, values[0])