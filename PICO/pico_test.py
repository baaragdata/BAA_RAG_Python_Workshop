import machine
import utime
print("ADC Test")


start = utime.time()

for i in range(10000):
    reading = []
    sensor_temp = machine.ADC(4)
    reading.append(sensor_temp.read_u16())

end = utime.time()

print("Finished in {}".format(end-start))