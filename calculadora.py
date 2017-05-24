global operador
def numero(n):
        operador = n
        print(n)

def suma():
        sum = operador + operador
        print(suma)
from tkinter import*

tk_numero= Tk()
tk_numero.title("CALCULADORA")
btn1 = Button(tk_numero, text = "1", command = lambda:numero(1))
btn1.pack()
btn2 = Button(tk_numero, text = "2", command = lambda:numero(2))
btn2.pack()

