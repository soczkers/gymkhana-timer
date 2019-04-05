import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def my_callback(channel):
    print(channel)

for i in [4,17]:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(i, GPIO.RISING)
    GPIO.add_event_callback(channel, my_callback, bouncetime=2000)
    print(i,"done")
