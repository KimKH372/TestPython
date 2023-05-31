from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "ch5/cat3.gif")
photo2 = PhotoImage(file = "ch5/cat4.gif")



label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT);
label2.pack();

window.mainloop()
