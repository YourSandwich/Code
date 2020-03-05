from tkinter import *
from tkinter import filedialog ##ermöglicht die abfrage von daten
from PIL import Image  
import PIL  

## Definiert die Funktion
def black_white():
    average = 382.5
    for x in range(image.width()):
        for y in range(image.height()):
            c = image.get(x,y) ## c bekommt die werte von den image also zumbeispiel 0,0
            brightness = int(c[0]) + int(c[1]) + int(c[2]) ## die Brightness wird mit der position von image addiert bestimmt.
            if brightness < average:                        ##wenn die Brighntes gröser als der average ist dan soll in das Bild bei der (x,y) schwarz eingefügt werden.
                image.put("black", (x,y))
            else:
                 image.put("white",(x,y))


Fenster = Tk() ## benutzt das modul von Tkinter das für die gui zuständig ist und setzt die Funktion ins Fenster
Fenster.title("Black&White")
Fenster.minsize(200,50)
image = PhotoImage(file=filedialog.askopenfilenames()) ## Die Variable image bekommt die Funktion PhotoImage die Gif lesen kann. 
btn_BW = Button(master=Fenster, command=black_white, text="Change") ## Hier wird ein Button erstellt der die funktion black_white ausführt
btn_Open = Button(master=Fenster, command=filedialog.askopenfilenames, text="Open")
btn_save = Button(master=Fenster, command=filedialog.asksaveasfile, text="Save")
label_image = Label(master=Fenster, image=image) ##  Es wird ein Label erstellt der zum Fenster gehört und das bild der variable bild hat.
label_image.pack() ## der Label wird angezeigt
btn_Open.pack(fill=X)
btn_BW.pack(fill=X) ## Der Knopf wird angezeigt.
btn_save.pack(fill=X)
Fenster.mainloop()   