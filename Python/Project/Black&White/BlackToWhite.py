from tkinter import *

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
image = PhotoImage(file="D:\Müll\Code\Python\Project\Black&White\giphy.gif") ## Die Variable image bekommt die Funktion PhotoImage die Gif lesen kann. 
btn_BW = Button(master=Fenster, command=black_white, text="Change") ## Hier wird ein Button erstellt der die funktion black_white ausführt
label_image = Label(master=Fenster, image=image) ##  Es wird ein Label erstellt der zum Fenster gehört und das bild der variable bild hat.
label_image.pack() ## der Label wird angezeigt
btn_BW.pack(fill=X) ## Der Knopf wird angezeigt.
Fenster.mainloop()   