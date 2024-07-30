import RPi.GPIO as GPIO
from time import time

def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(10, GPIO.OUT)  # Set the pin as an output
    
def binary_acquire(pin, duration):
    # acquires data as quickly as possible
    t0 = time()
    results = []
    while (time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results

def on_ir_receive(pinNo, bouncetime=150):
    # when edge detect is called (which requires less CPU than constant
    # data acquisition), we acquire data as quickly as possible
    data = binary_acquire(pinNo, bouncetime / 1000.0)
    if len(data) < bouncetime:
        return None
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    # detect run lengths using the acquisition rate to turn the times into microseconds
    for i in range(1, len(data)):
        if (data[i] != data[i - 1]) or (i == len(data) - 1):
            pulses.append((data[i - 1], int((i - i_break) / rate * 1e6)))
            i_break = i

    # decode (< 1 ms "1" pulse is a 0, 1-2 ms "1" pulse is a 1, longer than 2 ms pulse is something else)
    # does not decode channel, which may be a piece of the information after the long 1 pulse in the middle
    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 <= us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None

def destroy():
    GPIO.cleanup()


setup()
try:
    print("Starting IR Listener")
    while True:
        GPIO.output(10, GPIO.HIGH)  # Turn on the LASER
        #time.sleep(1)  # Delay for one second
        print("Waiting for signal")
        GPIO.wait_for_edge(16, GPIO.FALLING)
        code = on_ir_receive(16)
        GPIO.output(10, GPIO.LOW)  # Turn off the LASER
        #time.sleep(1)  # Delay for one second
        if code:
            print(str(hex(code)))
        else:
            print("Invalid code")
            
except KeyboardInterrupt:
    pass

except RuntimeError as e:
    print(e)
    # this gets thrown when control C gets pressed
    # because wait_for_edge doesn't properly pass this on
    pass

print("Quitting")
destroy()
