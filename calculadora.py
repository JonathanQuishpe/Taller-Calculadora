def Suma():
   n1 = float(box1.get())
   n2 = float(box2.get())
   suma = n1 + n2
   box1.delete(0,20)
   box2.delete(0,20)
   print (suma)
   
def Resta():
   n1 = float(box1.get())
   n2 = float(box2.get())
   resta = n1 - n2
   box1.delete(0,20)
   box2.delete(0,20)
   print (resta)
def Division():
   n1 = float(box1.get())
   n2 = float(box2.get())
   division = n1 / n2
   box1.delete(0,20)
   box2.delete(0,20)
   print (division)
   
def Multiplicacion():
   n1 = float(box1.get())
   n2 = float(box2.get())
   mult = n1 * n2
   box1.delete(0,20)
   box2.delete(0,20)
   print (mult)

from tkinter import*

tk = Tk()


numero1=StringVar()
box1=Entry(tk,bd=2,textvariable=numero1)
box1.pack()

numero2=StringVar()
box2=Entry(tk,bd=2,textvariable=numero2)
box2.pack()


btn_1 = Button (tk, text = 'Suma', command = Suma, width=15)
btn_1.pack()

btn_2 = Button (tk, text = 'Resta', command = Resta, width=15)
btn_2.pack()

btn_3 = Button (tk, text = 'Multiplicación', command = Multiplicacion, width=15)
btn_3.pack()

btn_4 = Button (tk, text = 'División', command =Division, width=15)
btn_4.pack()

tk.mainloop()


