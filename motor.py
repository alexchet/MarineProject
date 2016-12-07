import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import logging
import sys
import time

from Adafruit_BNO055 import BNO055

bno = BNO055.BNO055(busnum=2, rst='P9_12')

# Enable verbose debug logging if -v is passed as a parameter.
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

# Initialize the BNO055 and stop if something went wrong.
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Print system status and self test result.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

print('Reading BNO055 data, press Ctrl-C to quit...')

print('Init GPIO')

motorPin="P9_14"
PWM.start(motorPin,4,50)

time.sleep(2)

while True:
    heading, roll, pitch = bno.read_euler()
    rollMirrorPositive = 90 - abs(roll)
    p = (rollMirrorPositive / 90)    
    
    if p <= 0.2:
        PWM.set_duty_cycle(motorPin,5)
    elif p > 0.2 and p <= 0.4:
        PWM.set_duty_cycle(motorPin,7)
    elif p > 0.4 and p <= 0.6:
        PWM.set_duty_cycle(motorPin,9)
    else:
        PWM.set_duty_cycle(motorPin,11)
	
