from tkinter import *
from random import randint


fenster = Tk()
fenster.title("Würfel")
fenster.geometry("300x300+500+500")

def Zufall():
    zufallszahl = randint(1,6)
    lab.config(text=zufallszahl)


lab = Label(fenster, font=("Arial",50), text="?", width = 3)
lab.pack()

knopf = Button(fenster, text = "Drück mich!" , command=Zufall)
knopf.pack()

fenster.mainloop()