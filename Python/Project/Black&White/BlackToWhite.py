from tkinter import *

def black_white():
    average = 382.5
    for x in range(image.width()):
        for y in range(image.height()):
            c = image.get(x,y)
            brightness = int(c[0]) + int(c[1]) + int(c[2])
            if brightness < average:
                image.put("black", (x,y))
            else:
                 image.put("white",(x,y))

Fenster = Tk()
image = PhotoImage(file="D:\Müll\Code\Python\Programs\Black&White\giphy.gif")
btn_BW = Button(master=Fenster, command=black_white, text="Change")
label_image = Label(master=Fenster, image=image)
label_image.pack()
btn_BW.pack(fill=X)
Fenster.mainloop()   