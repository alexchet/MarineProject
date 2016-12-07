import Adafruit_BBIO.PWM as PWM
from time import sleep
motorPin="P9_14"
PWM.start(motorPin,7.5,50)
sleep(4)
while(1):
    dutyCycle=input("What duty cycle: ")
    PWM.set_duty_cycle(motorPin,dutyCycle)