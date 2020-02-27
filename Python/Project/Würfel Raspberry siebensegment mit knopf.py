from Tkinter import *
from random import randint
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def Zufall():
    zufallszahl = randint(1,6)

    if zufallszahl == 1:
        eins()
    if zufallszahl == 2:
        zwei()
    if zufallszahl == 3:
        drei()
    if zufallszahl == 4:
        vier()
    if zufallszahl == 5:
        funf()
    if zufallszahl == 6:
        sechs()


def eins():
        GPIO.output(2,GPIO.LOW)
        GPIO.output(3,GPIO.LOW)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(9,GPIO.LOW)


def zwei():
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(9,GPIO.HIGH)


def drei():
        GPIO.output(2,GPIO.LOW)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(9,GPIO.HIGH)


def vier():
        GPIO.output(2,GPIO.LOW)
        GPIO.output(3,GPIO.LOW)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(9,GPIO.HIGH)


def funf():
        GPIO.output(2,GPIO.LOW)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(9,GPIO.HIGH)


while True:
     if GPIO.input(10):
         Zufall()


fenster.mainloop()