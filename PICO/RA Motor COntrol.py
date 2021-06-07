''' RA Motor control '''

from machine import PWM, Pin
import time
from machine import UART, PWM

print("Pico Motor Control")

but = Pin(16, Pin.IN, pull=Pin.PULL_UP)
uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), timeout=1)

en = PWM(Pin(15))
fwd = Pin(14, mode=Pin.OUT)
rev = Pin(13, mode=Pin.OUT)

set_speed = 30000

en.freq(500)

def motor(dir, speed):
    ''' Controls the motor
        FWD = Forward
        REV = Reverse
        Speed = 0-65535
    '''
    if dir == 'FWD':
        fwd.high()
        rev.low()
    elif dir == 'REV':
        fwd.low()
        rev.high()
    en.duty_u16(speed)

motor

while True:
    if but.value() == 0:
        #print("Button Pressed")
        motor('FWD', 30000)
    else:
        #motor('FWD', 0)
        pass
    
    cmnd = None
    cmnd = uart0.readline()
    

    if cmnd:
        print(type(cmnd))
        scmnd = cmnd.decode()
        print(type(scmnd))
        if '<' in scmnd:
            motor('REV', set_speed)
        elif '>' in scmnd:
            motor('FWD', set_speed)
        elif 'STOP' in scmnd:
            motor('FWD', 0)
        elif 'SPEED' in scmnd:
            speed_val = scmnd.split(',')
            set_speed = int(speed_val[1])
 
    time.sleep(0.1)
    
    