import time
import requests
import RPi.GPIO as GPIO
#TARGET="http://localhost:9090"
TARGET="https://httpbin.org/post"

GPIO.setmode(GPIO.BCM)

def my_callback(channel):
    payload = {'channel': channel, 'time': time.time()}
    print(requests.post(TARGET, data=payload).text)

for i in [4,17]:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(i, GPIO.RISING, callback=my_callback, bouncetime=2000)

while True:
    time.sleep(1)
