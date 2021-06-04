# Raspberry Pi Pico Analog Input Test
# and logging to file
 
# POT - Pico GPIO 26 ADC0 - Pin 32
 
# Testing for BAA RAG
 
print("Analog sampling proram for Pico")

import machine

import utime
import uos

potentiometer = machine.ADC(machine.Pin(26))

def run():
    try:
        logfile = open('vals.txt', 'a')
    except:
        logfile = open('vals.txt', 'w')

    for i in range(10):
        val = potentiometer.read_u16()
        tmptime = utime.gmtime()
        logfile.write("{}:{}:{}, {}\r\n".format(tmptime[3], tmptime[4], tmptime[5], val))
        utime.sleep(0.5)
        print(i, val)
    logfile.close()

run()


