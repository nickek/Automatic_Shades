from time import sleep
import RPi.GPIO as GPIO
import time, board, busio, math, glob
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import ADS1x15


## ------ Light sensor ------
# Create I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC obj using I2C bus
ads = ADS.ADS1115(i2c)
voltageMax = 3.3

# Create single ended input on channels
chan0 = AnalogIn(ads, ADS.P0)


sleep_time = 1

## ------ Temp sensor ------
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Waiting for initialization..")

base_dir = "/sys/bus/w1/devices/"

while True:
    try:
        device_folder = glob.glob(base_dir + '28*')[0]
        break
    except IndexError as e:
        print(e)
        sleep(0.5)
        continue

device_file = device_folder + '/w1_slave'

def TempMessung():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

TempMessung()

def TempAuswertung():
    lines = TempMessung()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = TempMessung()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string)/1000.0
        return temp_c

def sensorValues():
    try:
        #print("------------------------------")
        tempc = TempAuswertung()
        tempf = ((tempc*9)/5) + 32
        #print("Temperature", tempc, "degC", tempf, "degF")
       
        #print("------------------------------")
        resistance = chan0.voltage / (voltageMax - chan0.voltage) * 10000
        lux = (1000000/resistance)
        #print("P0 Voltage value: ", '%.2f' % chan0.voltage, "V, restiance: ", '%.2f' % resistance, 'I(C)')
        #print("P0 Lux value: ", '%.2f' % lux )
        
        light_data = {"resistance": resistance,
                      "lux": lux}
        
        temperature_data = {"tempf": tempf,
                            "tempc": tempc}
        
        return light_data, temperature_data
        
    except KeyboardInterrupt:
        GPIO.cleanup()
    
    


