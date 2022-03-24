from tkinter import *
import tkinter.ttk
#Artjom Vinogradov
#IT-21
#22.03.22
#ülesanne 6


#akna seaded
aken = Tk()
aken.title('Joonistamine')


#lõuendi loomine
louend = Canvas(aken, width=1000, height=1000)
louend.pack()

#kujundite loomine
louend.create_rectangle(0, 0, 350, 100, fill='#02b2f2', outline='#993333', width=0)
louend.create_rectangle(0, 100, 350, 120, fill="#ffffff", outline="#000000")
louend.create_rectangle(0, 160, 350, 120, fill="#000000", outline="#ffffff")
louend.create_rectangle(0, 180, 350, 100, outline="#ffffff")
louend.create_rectangle(0, 180, 350, 280, fill="#02b2f2", outline="#ffffff")


silt = Label(aken, text="Botswana flag")
silt.place(x=140, y=280)

#minu pilt
minu_pilt = PhotoImage(file='pilt.gif')

louend.create_image(100, 400, anchor=NW, image=minu_pilt)







aken.mainloop()