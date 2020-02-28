#!/usr/bin/python3
from tkinter import *

inhalt = "" 

def drucken(num): 

	global inhalt 
	inhalt = inhalt + str(num) 
	zusammen.set(inhalt) 

def istgleich(): 

	try: 
		global inhalt 
		total = str(eval(inhalt)) 
		zusammen.set(total) 
	
		inhalt = "" 

	except: 
		zusammen.set(" error ") 
		inhalt = "" 


def löschen(): 
	global inhalt 
	inhalt = "" 
	zusammen.set("") 


if __name__ == "__main__": 

	Fenster = Tk() 
	Fenster.configure(background="#ababab")
	Fenster.title("Mein kleiner Taschenrechner") 
	Fenster.geometry("265x245") 
	Fenster.minsize(265, 245)
	Fenster.maxsize(265, 245)

	zusammen = StringVar() 


	inhalt_feld = Entry(Fenster, textvariable=zusammen) 
	inhalt_feld.grid(columnspan=4, ipadx=70, ipady=10) 

	zusammen.set('Hier tippen') 


	button1 = Button(Fenster, text=' 1 ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(1), height=2, width=7) 
	button1.grid(row=6, column=0) 

	button2 = Button(Fenster, text=' 2 ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(2), height=2, width=7) 
	button2.grid(row=6, column=1) 

	button3 = Button(Fenster, text=' 3 ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(3), height=2, width=7) 
	button3.grid(row=6, column=2) 

	button4 = Button(Fenster, text=' 4 ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(4), height=2, width=7) 
	button4.grid(row=5, column=0) 

	button5 = Button(Fenster, text=' 5 ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(5), height=2, width=7) 
	button5.grid(row=5, column=1) 

	button6 = Button(Fenster, text=' 6 ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(6), height=2, width=7) 
	button6.grid(row=5, column=2) 

	button7 = Button(Fenster, text=' 7 ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(7), height=2, width=7) 
	button7.grid(row=4, column=0) 

	button8 = Button(Fenster, text=' 8 ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(8), height=2, width=7) 
	button8.grid(row=4, column=1) 

	button9 = Button(Fenster, text=' 9 ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(9), height=2, width=7) 
	button9.grid(row=4, column=2) 

	button0 = Button(Fenster, text=' 0 ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(0), height=2, width=7) 
	button0.grid(row=7, column=1) 

	komma = Button(Fenster, text=' , ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken(','), height=2, width=7) 
	komma.grid(row=7, column=2)

	plus2minus = Button(Fenster, text=' +/- ', fg='#ffffff', bg='#000000', 
					 height=2, width=7) 
	plus2minus.grid(row=7, column=0)  

	plus = Button(Fenster, text=' + ', fg='#ffffff', bg='#000000', 
				command=lambda: drucken("+"), height=2, width=7) 
	plus.grid(row=6, column=3) 

	minus = Button(Fenster, text=' - ', fg='#ffffff', bg='#000000', 
				command=lambda: drucken("-"), height=2, width=7) 
	minus.grid(row=5, column=3) 

	mall = Button(Fenster, text=' * ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken("*"), height=2, width=7) 
	mall.grid(row=4, column=3) 

	dividieren = Button(Fenster, text=' / ', fg='#ffffff', bg='#000000', 
					command=lambda: drucken("/"), height=2, width=7) 
	dividieren.grid(row=3, column=3) 

	istgleich = Button(Fenster, text=' = ', fg='#ffffff', bg='#000000', 
				command=istgleich, height=2, width=7) 
	istgleich.grid(row=7, column=3) 

	löschen = Button(Fenster, text='löschen', fg='#ffffff', bg='#000000', 
				command=löschen, height=2, width=7) 
	löschen.grid(row=3, column=2) 

	C = Button(Fenster, text='C', fg='#ffffff', bg='#000000', 
				command=löschen, height=2, width=7) 
	C.grid(row=3, column=1)

	CE = Button(Fenster, text='CE', fg='#ffffff', bg='#000000', 
				command=löschen, height=2, width=7) 
	CE.grid(row=3, column=0)

    
	Fenster.mainloop() 