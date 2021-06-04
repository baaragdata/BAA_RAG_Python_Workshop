# Raspberry Pi Pico Analog Input Test
# and logging to file
 
# POT - Pico GPIO 26 ADC0 - Pin 32
 
# Testing for BAA RAG
 
 
import machine
import utime
import uos

potentiometer = machine.ADC(26)

def run():
    try:
        logFile = open('vals.txt', 'a')
    except OSError:
        logFile = open('vals.txt', 'w')                
    for i in range(10):
        value = potentiometer.read_u16()
        timeNow = utime.gmtime()
        logFile.write("{}:{}:{},{}".format(timeNow[3], timeNow[4], timeNow[5], str(value) + '\n'))
        logFile.flush()
        print(timeNow[5], "Value =", value)
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