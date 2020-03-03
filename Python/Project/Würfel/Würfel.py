from tkinter import *
from random import randint


fenster = Tk()
fenster.title("Würfel")
fenster.iconbitmap('@/mnt/DEDC8D3CDC8D1047/Müll/Code/Python/Project/Würfel/calculator.xbm')
fenster.geometry("210x180+800+350")
fenster.minsize(220, 180)
fenster.maxsize(220, 180)

def Zufall():
    zufallszahl = randint(text.get(), text2.get())
    lab.config(text=zufallszahl)


text = IntVar()
text2 = IntVar()

platz= Label(fenster)
platz.grid(row=0)

lab = Label(fenster, font=("Arial",50), text="?", width = 3)
lab.grid(row=1, column=1)


von = Entry(fenster, textvariable=text)
von.grid(row=2, column=1)

bis = Entry(fenster, textvariable=text2)
bis.grid(row=3, column=1)

Label(fenster, text="von").grid(row=2)
Label(fenster, text="bis").grid(row=3)


knopf = Button(fenster, text = "Drück mich!" , command=Zufall)
knopf.grid(row=4, column=1)

fenster.mainloop()