import tkinter as tk
from tkinter import *;

# pantalla principal
root = Tk()
root.title("GESTOR +")
root.resizable(0,0)
root.config(bd=80)
root.iconbitmap('seta.ico')

# DEFINIR PANTALLAS
pantallaInicio = Frame(root)
pantallaAltas = Frame(root) 
pantallaBuscar = Frame(root)
pantallaFichero = Frame(root)
pantallaInforme = Frame(root)

# LLAMAR PANTALLA PRINCIPAL
def mostrarPantallaInicio():
    ocultarTodasPantallas()
    pantallaInicio.pack()

# LLAMAR PANTALLA ALTAS
def mostrarPantallaAltas():
    ocultarTodasPantallas()
    pantallaAltas.pack()

# LLAMAR PANTALLA BUSCAR
def mostrarPantallaBuscar():
    ocultarTodasPantallas()
    pantallaBuscar.pack()

# LLAMAR PANTALLA FICHERO
def mostrarPantallaFichero():
    ocultarTodasPantallas()
    pantallaFichero.pack()

# LLAMAR PANTALLA INFORME
def mostrarPantallaInforme():
    ocultarTodasPantallas()
    pantallaInforme.pack()

def ocultarTodasPantallas():
    pantallaInicio.pack_forget()
    pantallaAltas.pack_forget()
    pantallaBuscar.pack_forget()
    pantallaFichero.pack_forget()
    pantallaInforme.pack_forget()

# INICIAR APLICACION EN PANTALLA PRINCIPAL
mostrarPantallaInicio()

# PANTALLA PRINCIPAL
Label(pantallaInicio, text="GESTOR +", font=("Arial", 30)).grid(row=0, column=0, columnspan=2, pady=10)
image = tk.PhotoImage(file="seta.png")
Label(pantallaInicio, image = image).grid(columnspan=6, row=1, column=0, pady=10, sticky=EW)
def boton(texto, fila, columna, pantallaDestino):
    Button(pantallaInicio, text=texto, width=10, height=2, command=pantallaDestino).grid(row=fila, column=columna, padx=20, pady=10, sticky=EW)
boton("ALTAS", 2, 0, mostrarPantallaAltas)
boton("BUSCAR", 2, 1, mostrarPantallaBuscar)
boton("FICHERO", 3, 0, mostrarPantallaFichero)
boton("INFORME", 3, 1, mostrarPantallaInforme)

# PANTALLA ALTAS
Label(pantallaAltas, text="ALTAS", font=("Arial", 30))
Entry(pantallaAltas, text="Nombre y apellidos").grid(row=0, column=0, columnspan=3, pady=10, sticky=EW)
Entry(pantallaAltas, text="Fecha Inicio").grid(row=1, column=0, columnspan=1, pady=10)
Entry(pantallaAltas, text="Fecha Nacimiento").grid(row=1, column=1, columnspan=1, pady=10)
Entry(pantallaAltas, text="Dirección").grid(row=1, column=2, columnspan=2, pady=10)
Entry(pantallaAltas, text="NIF").grid(row=2, column=0, columnspan=1, pady=10)
Entry(pantallaAltas, text="Número de afiliación SS").grid(row=2, column=1, columnspan=1, pady=10)











root.mainloop()