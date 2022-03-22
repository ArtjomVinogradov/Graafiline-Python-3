from tkinter import *
import tkinter.ttk

#Artjom Vinogradov
#IT-21
#22.03.22
#ülesanne 5




#aken
aken = Tk()
aken.title('Nupud')
aken.geometry("600x300")

#silt
silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0, column=0)

silt1 = Label(aken, text="Käibemaksumäär:")
silt1.grid(row=1, column=0)

silt2=Label(aken, text="______________________________________________________________________________")
silt2.grid(row=3, columnspan=2)

silt3 = Label(aken, text="Käibemaks:")
silt3.grid(row=4, column=0)

silt4 = Label(aken, text="Hind käibemaksuga:")
silt4.grid(row=5, column=0)



#procent
pro = IntVar()
proc = Radiobutton(aken,text="9%", variable=pro, value=1)
proc.grid(row=1, column= 1)
proc = Radiobutton(aken,text="20%", variable=pro, value=2)
proc.grid(row=2, column= 1)


#valjund
valjund = Entry(aken)
valjund.grid(row=0,column=1)

def arv():
    proc = pro.get()
    p = valjund.get()
    if proc == 1:
        arv = float(p)*0.09
    else:
        arv = float(p)*0.2
        
    Käbimaks = float(arv) + float(p)
    silt =Label(aken, text=arv)
    silt.grid(row=4, column=1)
    
    silt1 =Label(aken, text=Käbimaks)
    silt1.grid(row=5, column=1)    
    
    print(pro.get())
    print(valjund.get())



#nupp
nupp = Button(aken, text="Lets go mees", width=10, command=arv)
nupp.grid(row=6, column=1)

silt =Label(aken, text=0.00)
silt.grid(row=4, column=1)

silt1 =Label(aken, text=0.00)
silt1.grid(row=5, column=1)

aken.mainloop()