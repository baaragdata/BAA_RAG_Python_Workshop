from machine import Pin
import time
from machine import UART, PWM
#from serial.serialutil import Timeout

print("Pico Test")

but = Pin(16, Pin.IN, pull=Pin.PULL_UP)
uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), timeout=1)

en = PWM(Pin(15))
fwd = Pin(14, mode=Pin.OUT)
rev = Pin(13, mode=Pin.OUT)

set_speed = 30000

def motor(dir, speed):
    if dir == 'FWD':
        fwd.high()
        rev.low()
    elif dir == 'REV':
        fwd.low()
        rev.high()
    en.duty_u16(speed)

en.freq(500)

while True:
    if but.value() == 0:
        #print("button pressed")
        #uart0.write(b'button pressed\n\r')
        motor('FWD', 30000)
    else:
        pass
        #motor('FWD', 0)
    cmnd = None
    cmnd = uart0.readline()
    if cmnd:
        scmnd = cmnd.decode()
        if '<' in scmnd:
            motor('REV', set_speed)
        elif '>' in scmnd:
            motor('FWD', set_speed)
        elif 'STOP' in scmnd:
            motor('FWD', 0)
        elif 'SPEED' in scmnd:
            speed_val = scmnd.split(',')
            set_speed = int(speed_val[1])
            #print(speed_val)
        #print(cmnd)
    time.sleep(0.1)
