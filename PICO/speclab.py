''' Test how Pico can 
    sample VLF for use with
    SpectrumLab
'''

from machine import UART, Pin
import machine
import utime

sig = machine.ADC(26)

sl = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1), timeout=1)

print("SpectrumLab Test Program")

while True:
    val = sig.read_u16()
    sl.write(b"\xFF{}\n".format(str(val)))
    #utime.sleep(0.1)

