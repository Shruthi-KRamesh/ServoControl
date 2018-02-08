#------------------------------------i2c - shield-trial 1-----------------------------------------------
import board
import busio
import adafruit_pca9685
import time
import adafruit_motor.servo
import Motor_angles
from analogio import AnalogIn
#i2c communication
i2c = busio.I2C(board.SCL, board.SDA)
#when motor shaft is connected to Potentiometer, the value is read using analog pin A4 on Trinket
analoginp=AnalogIn(board.A4)#comment if not required
pcaobj = adafruit_pca9685.PCA9685(i2c) # creating object for pca9685 library
pcaobj.frequency = 50 # set frequency
servo_channel = pcaobj.channels[0] #select channel on pca9685 over which PWM must be generated
servo = adafruit_motor.servo.Servo(servo_channel)#createing object for servo library
start_angle = 0.0#start position of motor
stop_angle =40.0# stop position of motor
motobj=Motor_angles.Speed(start_angle,stop_angle)#creating object for motor_angles
li1=motobj.incrDecr()#returns a list of angles with the difference varying in fibonacci series manner
# print ('list is--',li1)
for each in li1:
	servo.angle = each
	#display Pot value. comment if Pot is not used
	print ('Analog value from Pot is--',(analoginp.value*3.3)/65536)#3.3V of Trinket in connect to Pot
	time.sleep(0.25)
#Uncomment, for continuously moving servo between start and stop positions
# while True:
#     servo.angle = start_angle
#     time.sleep(2)
#     servo.angle = stop_angle
#     time.sleep(2)

#---------------------------------------i2c-trial 1 end---------------------------------------------
