import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def my_callback(channel):
    print(channel)

for i in [4,17]:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(i, GPIO.RISING, callback=my_callback, bouncetime=2000)
    print(i,"done")

while True:
    time.sleep(1)
