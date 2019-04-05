import time
import requests
import RPi.GPIO as GPIO
TARGET = "http://localhost:9090"
TARGET = "http://requestbin.fullcontact.com/1blz63q1"
SENSOR = {4:"start", 17:"meta"}
GPIO.setmode(GPIO.BCM)

def my_callback(channel):
    payload = {'channel': SENSOR[channel], 'time': time.time()}
    print(requests.post(TARGET, data=payload))

for i in [4,17]:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(i, GPIO.RISING, callback=my_callback, bouncetime=2000)
    print(i,"done")

while True:
    time.sleep(1)
