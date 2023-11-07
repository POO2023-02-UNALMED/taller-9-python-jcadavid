from tkinter import Tk, Button, Entry
from tkinter.constants import END
class calculator:
    n1 = ""
    n2 = ""
    operator = ""
    @staticmethod
    def setNumber(value):
        if value.isdigit():
            if calculator.operator == "":
                calculator.n1 = calculator.n1 + value
            else:
                calculator.n2 = calculator.n2 + value
        return calculator.getStringOperacion()

    @staticmethod
    def setOperator(value):
        calculator.operator = value
        return calculator.getStringOperacion()

    @staticmethod
    def calcular():
        n1 = calculator.n1
        n2 = calculator.n2
        operator = calculator.operator
        calculator.limpiar()
        if (operator == "+"):
            return float(n1)+float(n2)
        if (operator == "-"):
            return float(n1)-float(n2)
        if (operator == "*"):
            return float(n1)*float(n2)
        if (operator == "/"):
            return float(n1)+float(n2)

    @staticmethod
    def getStringOperacion():
        return calculator.n1 + " " + calculator.operator + " " + calculator.n2

    @staticmethod
    def limpiar():
        calculator.n1 = ""
        calculator.n2 = ""
        calculator.operator = ""


def set_text(text):
    textStr = str(text)
    pantalla.delete(0, END)
    pantalla.insert(0, textStr)
    return

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=90, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setNumber("1"))).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setNumber("2"))).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setNumber("3"))).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setNumber("4"))).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setNumber("5"))).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setNumber("6"))).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setNumber("7"))).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setNumber("8"))).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setNumber("9"))).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=lambda: set_text(calculator.calcular())).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: set_text(calculator.setNumber(".")) ).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setOperator("+"))).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setOperator("-"))).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setOperator("*"))).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: set_text(calculator.setOperator("/"))).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()

