import machine
import utime
print("ADC Example")

ADCValue = machine.ADC(4)

reading = []
for i in range(20):
    reading.append(ADCValue.read_u16())
    print(i, reading[i])
    utime.sleep(0.1)

sum = sum(reading)
num = len(reading)
ave = sum/num

print("Max", max(reading), "Min", min(reading), "Ave", ave)
print("Finished ADC")

