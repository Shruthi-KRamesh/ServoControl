#------------------------------------i2c - shield-trial 1-----------------------------------------------
import board
import busio
import adafruit_pca9685
import time
import adafruit_motor.servo
import Motor_angles
from analogio import AnalogIn
i2c = busio.I2C(board.SCL, board.SDA)
analoginp=AnalogIn(board.A4)
analoginp=AnalogIn(board.A4)
pcaobj = adafruit_pca9685.PCA9685(i2c)
pcaobj.frequency = 50
servo_channel = pcaobj.channels[0]
servo = adafruit_motor.servo.Servo(servo_channel)
start_angle = 0.0
stop_angle =40.0
motobj=Motor_angles.Speed(start_angle,stop_angle)
li1=motobj.incrDecr()
print ('list is--',li1)
for each in li1:
	servo.angle = each
	print ('Analog voltage is--',(analoginp.value*3.3)/65536)
	time.sleep(0.25)
# while True:
#     servo.angle = start_angle
#     time.sleep(2)
#     servo.angle = stop_angle
#     time.sleep(2)

#---------------------------------------i2c-trial 1 end---------------------------------------------
