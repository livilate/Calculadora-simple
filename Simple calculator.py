from tkinter import  *

root = Tk()
root.title('Calculator by Enzo V.')

#Pantalla para ver operaciones en la calculadora

pantalla = Entry(root, width=40, borderwidth=5)

#Def para las operaciones

def click(numero):
    #hago que el boton que clickeo se muestre en pantalla, defino una variable y le sumo el numero que
    #pongo luego para que no me quede lo de la pantalla alrevez, si queria escribir 801 me salia 108
    current = pantalla.get()
    pantalla.delete(0, END)
    pantalla.insert(0, str(current) + str(numero))

def borrar():
    pantalla.delete(0, END)

#definicion de las operaciones, todas tienen definida una variable global para que al hacer click en igual sepa que operacion estoy realizando


def suma():
    number_1 = pantalla.get()
    global numero_1
    global operacion
    operacion = 'sumando'
    numero_1 = int(number_1)
    pantalla.delete(0, END)

def resta():
    number_1 = pantalla.get()
    global numero_1
    global operacion
    numero_1 = int(number_1)
    operacion = 'restando'
    pantalla.delete(0, END)

def division():
    number_1 = pantalla.get()
    global numero_1
    global operacion
    operacion = 'dividiendo'
    numero_1 = int(number_1)
    pantalla.delete(0, END)

def multiplicacion():
    number_1 = pantalla.get()
    global numero_1
    global operacion
    operacion = 'multiplicando'
    numero_1 = int(number_1)
    pantalla.delete(0, END)

def igual():
    number_2 = pantalla.get()
    pantalla.delete(0, END)
    #uso un if statment para que al hacer click en igual sepa que operacion realizar.
    if operacion == 'sumando':
        pantalla.insert(0, str(int(numero_1) + int(number_2)))

    if operacion == 'restando':
        pantalla.insert(0, str(int(numero_1) - int(number_2)))

    if operacion == 'dividiendo':
        pantalla.insert(0, str(int(numero_1) // int(number_2)))

    if operacion == 'multiplicando':
        pantalla.insert(0, str(int(numero_1) * int(number_2)))

#botones calculadora

button0 = Button(root, text='0', padx=20, pady=20, command=lambda: click(0))
button1 = Button(root, text='1', padx=20, pady=20, command=lambda: click(1))
button2 = Button(root, text='2', padx=20, pady=20, command=lambda: click(2))
button3 = Button(root, text='3', padx=20, pady=20, command=lambda: click(3))
button4 = Button(root, text='4', padx=20, pady=20, command=lambda: click(4))
button5 = Button(root, text='5', padx=20, pady=20, command=lambda: click(5))
button6 = Button(root, text='6', padx=20, pady=20, command=lambda: click(6))
button7 = Button(root, text='7', padx=20, pady=20, command=lambda: click(7))
button8 = Button(root, text='8', padx=20, pady=20, command=lambda: click(8))
button9 = Button(root, text='9', padx=20, pady=20, command=lambda: click(9))
button_mas = Button(root, text='+', padx=20, pady=50, command=suma)
button_menos = Button(root, text='-', padx=20, pady=50, command=resta)
button_multiplicacion = Button(root, text='*', padx=20, pady=20, command=multiplicacion)
button_division = Button(root, text='/', padx=20, pady=20, command=division)
button_igual = Button(root, text='=', padx=50, pady=20, command=igual)
button_borrar = Button(root, text='Clear', padx=50, pady=20, command=borrar)

#Donde esta en pantalla cada boton

pantalla.grid(row=0, column=0, columnspan=10, pady=10, padx=5)

button_borrar.grid(row=1, column=2, columnspan=2, padx=1, pady=1)
button_division.grid(row=1, column=0, padx=1, pady=1)
button_multiplicacion.grid(row=1, column=1, padx=1, pady=1)

button7.grid(row=2, column=0, padx=1, pady=1)
button8.grid(row=2, column=1, padx=1, pady=1)
button9.grid(row=2, column=2, padx=1, pady=1)

button4.grid(row=3, column=0, padx=1, pady=1)
button5.grid(row=3, column=1, padx=1, pady=1)
button6.grid(row=3, column=2, padx=1, pady=1)

button1.grid(row=4, column=0, padx=1, pady=1)
button2.grid(row=4, column=1, padx=1, pady=1)
button3.grid(row=4, column=2, padx=1, pady=1)


button0.grid(row=5, column=0, padx=1, pady=1)
button_igual.grid(row=5, column=1, columnspan=2, padx=1, pady=1)

button_mas.grid(row=2, column=3, rowspan=2, padx=1, pady=1)
button_menos.grid(row=4, column=3, rowspan=2, padx=1, pady=1)



root.mainloop()