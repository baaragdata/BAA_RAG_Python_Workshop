# Raspberry Pi Pico Analog Input Test
# and logging to file
 
# POT - Pico GPIO 26 ADC0 - Pin 32
 
# Testing for BAA RAG
 
 
import machine
import utime
import uos

pwm = machine.PWM(machine.Pin(16))
pwm.freq(10000)

potentiometer = machine.ADC(26)
angle = machine.ADC(27)

def run():
    try:
        logFile = open('vals.txt', 'a')
    except OSError:
        logFile = open('vals.txt', 'w')                
    for i in range(10):
        speed = potentiometer.read_u16()
        tmtpl = utime.gmtime()
        logFile.write("{}:{}:{},{}".format(tmtpl[3], tmtpl[4], tmtpl[5], str(speed) + '\n'))
        logFile.flush()
        #motorPos = angle.read_u16()
        #pwm.duty_u16(speed)
        print(utime.gmtime()[5], "Speed", speed)
        utime.sleep(1)
        
    logFile.close()
    
    space = uos.statvfs('/')
    total_space = space[0] * space[2]
    free_space = space[1] * space[3]
    used = total_space - free_space
    used_percentage = used / total_space * 100
    print('Total = {}\r\nFree  = {}\r\nUsed  = {} = {:.1f}%'.format(total_space, free_space, total_space - free_space, used_percentage))
    
input("Press ENTER to start...")
run()