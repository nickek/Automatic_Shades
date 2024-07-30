import RPi.GPIO as GPIO
import l293d, time
from time import sleep
from ultrasonic_sensor import Ultrasonic

class Motor():
    def __init__(self, enb1, inp1, inp2):
        self.enb1 = enb1
        self.inp1 = inp1
        self.inp2 = inp2
        self.motor1 = l293d.DC(enb1, inp1, inp2, force_selection=True)
        self.u = Ultrasonic(18,25)
        self.dist = 100
        self.top_dist = 0
        self.bot_dist = 0
        
    def incrementC(self):
        print("incrementing C")
        self.motor1.clockwise()
        time.sleep(1)
        self.motor1.stop()
        GPIO.output(self.inp1, GPIO.LOW)
        
    def incrementCC(self):
        print("incrementing CC")
        self.motor1.anticlockwise()
        time.sleep(1)
        self.motor1.stop()
        GPIO.output(self.inp2, GPIO.LOW)
        
        
    def spinC(self):
        self.motor1.clockwise()
        
        while self.u.distance() <= self.dist:
            print(self.u.distance())
            time.sleep(1)
            pass
        
        
        self.motor1.stop()
        GPIO.output(self.inp1, GPIO.LOW)
        self.top_dist = self.u.distance()
        
    def spinCC(self):
        self.motor1.anticlockwise()
        
        self.dist = self.u.distance()
        while self.u.distance() > 10:
            print(self.u.distance())
            time.sleep(1)
            pass
        
        self.motor1.stop()
        GPIO.output(self.inp2, GPIO.LOW)
        self.bot_dist = self.u.distance()

#m = Motor(17, 27, 22)
#m.spinCC()