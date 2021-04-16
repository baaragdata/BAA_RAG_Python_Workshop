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
    logFile = open('vals.txt', 'a')
    for i in range(101):
        speed = potentiometer.read_u16()
        logFile.write(str(speed) + '\n')
        logFile.flush()
        motorPos = angle.read_u16()
        pwm.duty_u16(speed)
        print("Speed", speed, "Angle", motorPos)
        utime.sleep(0.1)
        
    logFile.close()
    space = uos.statvfs('/')
    total_space = space[0] * space[2]
    free_space = space[1] * space[3]
    used = total_space - free_space
    used_percentage = used / total_space * 100
    print('Total = {}\r\nFree  = {}\r\nUsed  = {} = {:.1f}%'.format(total_space, free_space, total_space - free_space, used_percentage))
    
input("Press ENTER to start...")
#print("Speed", 0, "Drive", 65535)
run()