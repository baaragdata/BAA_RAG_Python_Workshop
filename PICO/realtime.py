import PySimpleGUI as sg

# Make a form, but don't use context manager
form = sg.FlexForm('Robotics Remote Control', auto_size_text=True)

form_rows = [[sg.Text('Robotics Remote Control')],
             [sg.T(' '  * 10), sg.RealtimeButton('Forward')],
             [sg.RealtimeButton('Left'), sg.T(' '  * 15), sg.RealtimeButton('Right')],
             [sg.T(' '  * 10), sg.RealtimeButton('Reverse')],
             [sg.T('')],
             [sg.Quit(button_color=('black', 'orange'))]
             ]

form.LayoutAndRead(form_rows, non_blocking=True)

#
# Some place later in your code...
# You need to perform a ReadNonBlocking on your form every now and then or
# else it won't refresh.
#
# your program's main loop
while (True):
    # This is the code that reads and updates your window
    button, values = form.ReadNonBlocking()
    if button is not None:
        print(button)
    if button == 'Quit'  or values is None:
        break

form.CloseNonBlockingForm()