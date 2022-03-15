from tkinter import *

#akna seaded
aken = Tk()
aken.title('My name is Van')

aken.geometry("200x200")

aken.option_add("*font", ('tahoma', 12))



Label(aken, text="Format your pc please", font="Tahoma 11 bold italic").grid(row=0, column=0)
#nupud
nupp1 = Button(aken, text="7", width=4)
nupp1.grid(row=1, column=0, columnspan=5)
nupp2 = Button(aken, text="8", width=4)
nupp2.grid(row=1, column=1)
nupp3 = Button(aken, text="9", width=4)
nupp3.grid(row=1, column=2)
nupp4 = Button(aken, text="4", width=4)
nupp4.grid(row=2, column=0, columnspan=5)
nupp5 = Button(aken, text="5", width=4)
nupp5.grid(row=2, column=1)


nupp6 = Button(aken, text="6", width=4)
nupp6.grid(row=2, column=2)
nupp7 = Button(aken, text="1", width=4)
nupp7.grid(row=3, column=0, columnspan=5)
nupp8 = Button(aken, text="2", width=4)
nupp8.grid(row=3, column=1)
nupp9 = Button(aken, text="3", width=4)
nupp9.grid(row=3, column=2)
nupp10 = Button(aken, text="0", width=4)
nupp10.grid(row=4, column=0, columnspan=5)
nupp11 = Button(aken, text=",", width=4)
nupp11.grid(row=4, column=1)
nupp11 = Button(aken, text="=", width=4)
nupp11.grid(row=4, column=2)
nupp11 = Button(aken, text="+", width=4)
nupp11.grid(row=4, column=3)
nupp12 = Button(aken, text="/", width=4)
nupp12.grid(row=1, column=3)
nupp13 = Button(aken, text="*", width=4)
nupp13.grid(row=2, column=3)
nupp14 = Button(aken, text="-", width=4)
nupp14.grid(row=3, column=3)



aken.mainloop()