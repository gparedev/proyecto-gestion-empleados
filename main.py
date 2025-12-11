import tkinter as tk
from tkinter import *
import sqlite3
from datetime import datetime

# pantalla principal
root = Tk()
root.title("GESTOR +")
root.resizable(0,0)
root.config(bd=80)
root.iconbitmap('seta.ico')

# conexión base de datos
# conexión base de datos
def conexion_db():
    conexion = sqlite3.connect("empleados.db")
    return conexion

# crear tabla empleados si no existe, la llamamos al iniciar la app
def crear_tabla_empleados():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo          INTEGER UNIQUE,
        apellidos_nombre TEXT,
        fecha_inicio     TEXT,   -- 'YYYY-MM-DD'
        fecha_nacimiento TEXT,   -- 'YYYY-MM-DD'
        direccion        TEXT,
        nif              TEXT,
        naf              TEXT,   -- nº afiliación SS
        genero           TEXT,   -- 'M' / 'F'
        departamento     TEXT,
        puesto           TEXT,
        telefono         TEXT,
        salario_mensual  REAL,
        email            TEXT,
        num_pagas        INTEGER,  -- 12 + pagas extra
        fecha_baja       TEXT      -- NULL si está en alta
    );
    """)
    conexion.commit()
    conexion.close()
crear_tabla_empleados()

# DEFINIR PANTALLAS
pantallaInicio = Frame(root)
pantallaAltas = Frame(root) 
pantallaBuscar = Frame(root)
pantallaFichero = Frame(root)
pantallaInforme = Frame(root)

# LLAMAR PANTALLA PRINCIPAL
def mostrar_pantalla_inicio():
    ocultar_todas_pantallas()
    pantallaInicio.pack()

# LLAMAR PANTALLA ALTAS
def mostrar_pantalla_altas():
    ocultar_todas_pantallas()
    pantallaAltas.pack()

# LLAMAR PANTALLA BUSCAR
def mostrar_pantalla_buscar():
    ocultar_todas_pantallas()
    pantallaBuscar.pack()

# LLAMAR PANTALLA FICHERO
def mostrar_pantalla_fichero():
    ocultar_todas_pantallas()
    pantallaFichero.pack()

# LLAMAR PANTALLA INFORME
def mostrar_pantalla_informe():
    ocultar_todas_pantallas()
    pantallaInforme.pack()

def ocultar_todas_pantallas():
    pantallaInicio.pack_forget()
    pantallaAltas.pack_forget()
    pantallaBuscar.pack_forget()
    pantallaFichero.pack_forget()
    pantallaInforme.pack_forget()

# INICIAR APLICACION EN PANTALLA PRINCIPAL
mostrar_pantalla_inicio()

# PANTALLA PRINCIPAL
Label(pantallaInicio, text="GESTOR +", font=("Arial", 30)).grid(row=0, column=0, columnspan=2, pady=10)
#image = tk.PhotoImage(file="seta.png")
#Label(pantallaInicio, image = image).grid(columnspan=6, row=1, column=0, pady=10, sticky=EW)
Label(pantallaInicio).grid(columnspan=6, row=1, column=0, pady=10, sticky=EW)
def boton(texto, fila, columna, pantallaDestino):
    Button(pantallaInicio, text=texto, width=10, height=2, command=pantallaDestino).grid(row=fila, column=columna, padx=20, pady=10, sticky=EW)
boton("ALTAS", 2, 0, mostrar_pantalla_altas)
boton("BUSCAR", 2, 1, mostrar_pantalla_buscar)
boton("FICHERO", 3, 0, mostrar_pantalla_fichero)
boton("INFORME", 3, 1, mostrar_pantalla_informe)

# PANTALLA ALTAS
Label(pantallaAltas, text="Nombre y apellidos").grid(row=0, column=0, columnspan=6, pady=10, sticky=W)
nombre_apellidos = tk.Entry(pantallaAltas)
nombre_apellidos.grid(row=1, column=0, columnspan=6, pady=10, sticky=EW)

Label(pantallaAltas, text="Fecha Inicio").grid(row=2, column=0, columnspan=1, pady=10, sticky=W)
fecha_inicio = tk.Entry(pantallaAltas)
fecha_inicio.grid(row=3, column=0, columnspan=1, pady=10, sticky=EW)

Label(pantallaAltas, text="Fecha Nacimiento").grid(row=2, column=1, columnspan=1, pady=10, sticky=W)
fecha_nacimiento = tk.Entry(pantallaAltas)
fecha_nacimiento.grid(row=3, column=1, columnspan=1, pady=10, sticky=EW)

Label(pantallaAltas, text="Dirección").grid(row=2, column=2, columnspan=4, pady=10, sticky=W)
direccion = tk.Entry(pantallaAltas)
direccion.grid(row=3, column=2, columnspan=4, pady=10, sticky=EW)

Label(pantallaAltas, text="NIF").grid(row=4, column=0, columnspan=2, pady=10, sticky=W)
nif = tk.Entry(pantallaAltas)
nif.grid(row=5, column=0, columnspan=2, pady=10, sticky=EW)

Label(pantallaAltas, text="Número de afiliación SS").grid(row=4, column=2, columnspan=4, pady=10, sticky=W)
num_afiliacion_ss = tk.Entry(pantallaAltas)
num_afiliacion_ss.grid(row=5, column=2, columnspan=4, pady=10, sticky=EW)

Label(pantallaAltas, text="Género").grid(row=6, column=0, columnspan=1, pady=10, sticky=W)
genero = tk.Entry(pantallaAltas)
genero.grid(row=7, column=0, columnspan=1, pady=10, sticky=EW)

Label(pantallaAltas, text="Departamento").grid(row=6, column=1, columnspan=3, pady=10, sticky=W)
departamento = tk.Entry(pantallaAltas)
departamento.grid(row=7, column=1, columnspan=3, pady=10, sticky=EW)

Label(pantallaAltas, text="Puesto").grid(row=6, column=4, columnspan=2, pady=10, sticky=W)
puesto = tk.Entry(pantallaAltas)
puesto.grid(row=7, column=4, columnspan=2, pady=10, sticky=EW)

Label(pantallaAltas, text="Teléfono").grid(row=8, column=0, columnspan=1, pady=10, sticky=W)
telefono = tk.Entry(pantallaAltas)
telefono.grid(row=8, column=1, columnspan=1, pady=10, sticky=EW)

Label(pantallaAltas, text="Email").grid(row=9, column=0, columnspan=1, pady=10, sticky=W)
email = tk.Entry(pantallaAltas)
email.grid(row=9, column=1, columnspan=1, pady=10, sticky=EW)

Label(pantallaAltas, text="Salario mensual").grid(row=8, column=2, columnspan=1, pady=10, sticky=W)
salario_mensual = tk.Entry(pantallaAltas)
salario_mensual.grid(row=8, column=3, columnspan=3, pady=10, sticky=EW)

Label(pantallaAltas, text="Pagas extra").grid(row=9, column=2, columnspan=1, pady=10, sticky=W)
pagas_extra = tk.Entry(pantallaAltas)
pagas_extra.grid(row=9, column=3, columnspan=3, pady=10, sticky=EW)

txt_validacion_altas = tk.Text(pantallaAltas, height=3, state='disabled')
txt_validacion_altas.grid(row=12, column=0, columnspan=4, sticky=NSEW, pady=(10, 0))
btn_insertar_altas = tk.Button(pantallaAltas, text="INSERTAR")
btn_insertar_altas.grid(row=12, column=4, columnspan=2, sticky=NSEW, padx=(10, 0), pady=(10, 0))

# PANTALLA BUSCAR
Label(pantallaBuscar, text="Código empleado").grid(row=0, column=0, columnspan=1, pady=10, sticky=W)
codigo_empleado = Entry(pantallaBuscar).grid(row=0, column=1, columnspan=1, pady=10, sticky=EW)
Label(pantallaBuscar, text="Fecha baja").grid(row=0, column=2, columnspan=1, pady=10, sticky=W)
fecha_baja = Entry(pantallaBuscar).grid(row=0, column=3, columnspan=1, pady=10, sticky=EW)

Label(pantallaBuscar, text="Fecha inicio").grid(row=1, column=0, columnspan=1, pady=10, sticky=W)
Entry(pantallaBuscar).grid(row=2, column=0, columnspan=1, pady=10, sticky=EW)
Label(pantallaBuscar, text="Fecha fin").grid(row=1, column=1, columnspan=1, pady=10, sticky=W)
Entry(pantallaBuscar).grid(row=2, column=1, columnspan=1, pady=10, sticky=EW)
Label(pantallaBuscar, text="Apellidos y nombre").grid(row=1, column=2, columnspan=2, pady=10, sticky=W)
Entry(pantallaBuscar).grid(row=2, column=2, columnspan=2, pady=10, sticky=EW)

Label(pantallaBuscar, text="NIF").grid(row=3, column=0, columnspan=2, pady=10, sticky=W)
Entry(pantallaBuscar).grid(row=4, column=0, columnspan=2, pady=10, sticky=EW)
Label(pantallaBuscar, text="Número de afiliación SS").grid(row=3, column=2, columnspan=2, pady=10, sticky=W)
Entry(pantallaBuscar).grid(row=4, column=2, columnspan=2, pady=10, sticky=EW)

Label(pantallaBuscar, text="Salario bruto mes").grid(row=5, column=0, columnspan=1, pady=10, sticky=W)
Entry(pantallaBuscar).grid(row=5, column=1, columnspan=1, pady=10, sticky=EW)
Label(pantallaBuscar, text="Número pagas").grid(row=5, column=2, columnspan=1, pady=10, sticky=W)
Entry(pantallaBuscar).grid(row=5, column=3, columnspan=1, pady=10, sticky=EW)

Label(pantallaBuscar, text="Salario anual").grid(row=6, column=0, columnspan=1, pady=10, sticky=W)
Entry(pantallaBuscar).grid(row=6, column=1, columnspan=1, pady=10, sticky=EW)
Label(pantallaBuscar, text="Prorrata pagas").grid(row=7, column=0, columnspan=1, pady=10, sticky=W)
Entry(pantallaBuscar).grid(row=7, column=1, columnspan=1, pady=10, sticky=EW)

txt_validacion_buscar = tk.Text(pantallaBuscar, height=3)
txt_validacion_buscar.grid(row=6, column=2, columnspan=2, rowspan=2, sticky=NSEW, pady=(10, 0))
btn_insertar_buscar = tk.Button(pantallaBuscar, text="INSERTAR FECHA BAJA")
btn_insertar_buscar.grid(row=8, column=0, columnspan=2, sticky=NSEW, padx=(10, 0), pady=(10, 0))
btn_carga_buscar = tk.Button(pantallaBuscar, text="CARGA EMPLEADO")
btn_carga_buscar.grid(row=8, column=2, columnspan=2, sticky=NSEW, padx=(10, 0), pady=(10, 0))

# PANTALLA INFORME
Label(pantallaInforme, text="Empleados").grid(row=0, column=0, columnspan=1, pady=10, sticky=W)
txt_empleados = tk.Text(pantallaInforme, height=3)
txt_empleados.grid(row=1, column=0, columnspan=1, rowspan=2, sticky=NSEW, pady=(10, 0))

Label(pantallaInforme, text="Media edades").grid(row=0, column=1, columnspan=1, pady=10, sticky=W)
txt_media_edades = tk.Text(pantallaInforme, height=3)
txt_media_edades.grid(row=1, column=1, columnspan=1, rowspan=2, sticky=NSEW, pady=(10, 0))

Label(pantallaInforme, text="Retribución media").grid(row=0, column=2, columnspan=1, pady=10, sticky=W)
txt_retribucion_media = tk.Text(pantallaInforme, height=3)
txt_retribucion_media.grid(row=1, column=2, columnspan=1, rowspan=2, sticky=NSEW, pady=(10, 0))

Label(pantallaInforme, text="% Mujeres").grid(row=3, column=0, columnspan=1, pady=10, sticky=W)
txt_porcentaje_mujeres = tk.Text(pantallaInforme, height=3)
txt_porcentaje_mujeres.grid(row=4, column=0, columnspan=1, rowspan=2, sticky=NSEW, pady=(10, 0))
Label(pantallaInforme, text="Mujeres").grid(row=3, column=1, columnspan=1, pady=10, sticky=W)
txt_edad_media_mujeres = tk.Text(pantallaInforme, height=3)
txt_edad_media_mujeres.grid(row=4, column=1, columnspan=1, rowspan=2, sticky=NSEW, pady=(10, 0))

Label(pantallaInforme, text="Mujeres").grid(row=3, column=2, columnspan=1, pady=10, sticky=W)
txt_retribucion_media_mujeres = tk.Text(pantallaInforme, height=3)
txt_retribucion_media_mujeres.grid(row=4, column=2, columnspan=1, rowspan=2, sticky=NSEW, pady=(10, 0))

Label(pantallaInforme, text="% Hombres").grid(row=6, column=0, columnspan=1, pady=10, sticky=W)
txt_porcentaje_hombres = tk.Text(pantallaInforme, height=3)
txt_porcentaje_hombres.grid(row=7, column=0, columnspan=1, rowspan=2, sticky=NSEW, pady=(10, 0))

Label(pantallaInforme, text="Hombres").grid(row=6, column=1, columnspan=1, pady=10, sticky=W)
txt_edad_media_hombres = tk.Text(pantallaInforme, height=3)
txt_edad_media_hombres.grid(row=7, column=1, columnspan=1, rowspan=2, sticky=NSEW, pady=(10, 0))

Label(pantallaInforme, text="Hombres").grid(row=6, column=2, columnspan=1, pady=10, sticky=W)
txt_retribucion_media_hombres = tk.Text(pantallaInforme, height=3)
txt_retribucion_media_hombres.grid(row=7, column=2, columnspan=1, rowspan=2, sticky=NSEW, pady=(10, 0))

# LÓGICA
def insertar_empleado_consulta(datos):
    conexion = conexion_db()
    cursor = conexion.cursor()
    print(datos)

    cursor.execute(""" INSERT INTO empleados
            (codigo, apellidos_nombre, fecha_inicio, fecha_nacimiento, direccion, nif, naf, genero, departamento, puesto, telefono, salario_mensual, email, num_pagas, fecha_baja)
            VALUES
            (:codigo, :apellidos_nombre, :fecha_inicio, :fecha_nacimiento, :direccion, :nif, :naf, :genero, :departamento, :puesto, :telefono, :salario_mensual, :email, :num_pagas, NULL)
            """, datos)
    conexion.commit()
    conexion.close()

def insertar_empleado_relleno():
    # limpiar mensaje
    txt_validacion_altas.delete("1.0", tk.END)

    genero_validado = genero.get().strip().lower()
    salario_validado = salario_mensual.get().strip()
    pagas_extra_validado = pagas_extra.get().strip()

    errores_insertar = []

    if genero_validado not in ['hombre', 'mujer']:
        errores_insertar.append("Género debe ser 'hombre' o 'mujer'.")
    
    try:
        salario_validado = float(salario_validado)
    except ValueError:
        errores_insertar.append("Salario mensual debe ser un número válido.")

    if errores_insertar:
        txt_validacion_altas.insert(tk.END, "Errores al insertar:\n" + "\n".join(errores_insertar))
        return

    datos = {
        "codigo": generar_codigo(),
        "apellidos_nombre": nombre_apellidos.get(),
        "fecha_inicio": fecha_inicio.get(),
        "fecha_nacimiento": fecha_nacimiento.get(),
        "direccion": direccion.get(),
        "nif": nif.get(),
        "naf": num_afiliacion_ss.get(),
        "genero": genero.get(),
        "departamento": departamento.get(),
        "puesto": puesto.get(),
        "telefono": telefono.get(),
        "salario_mensual": salario_mensual.get(),
        "email": email.get(),
        "num_pagas": pagas_extra.get(),
    }

    try:
        insertar_empleado_consulta(datos)
        txt_validacion_altas.insert(
            tk.END,
            f"Empleado insertado correctamente.\nCódigo asignado: {datos['codigo']}"
        )
    except Exception as e:
        txt_validacion_altas.insert(tk.END, f"ERROR al insertar: {e}")

btn_insertar_altas.config(command=insertar_empleado_relleno)

def generar_codigo():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT MAX(codigo) FROM empleados")
    resultado = cursor.fetchone()
    conexion.close()
    if resultado[0] is None:
        return 1
    else:
        return resultado[0] + 1

def buscar_empleado(codigo): # busvar empleado por código
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleados WHERE codigo = ?", (codigo,))
    fila = cursor.fetchone()
    conexion.close()
    return fila

def calcular_salario(salario_mensual, num_pagas): # calcular salario anual y prorrata pagas
    salario_anual = salario_mensual * num_pagas
    prorrata = salario_mensual * (num_pagas - 12) / 12
    return salario_anual, prorrata

# de la pantalla informe
def numero_empleados():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM empleados")
    total = cursor.fetchone()[0]
    conexion.close()
    return total

def edad_media():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT AVG((julianday('now') - julianday(fecha_nacimiento)) / 365.25) FROM empleados")
    media = cursor.fetchone()[0]
    conexion.close()
    return media

def retribucion_media():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT AVG(salario_mensual * num_pagas) FROM empleados")
    media = cursor.fetchone()[0]
    conexion.close()
    return media

def porcentaje_mujeres():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM empleados WHERE genero = 'F'")
    mujeres = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM empleados")
    total = cursor.fetchone()[0]
    porcentaje = (mujeres / total) * 100 if total > 0 else 0
    conexion.close()
    return porcentaje

def numero_mujeres():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM empleados WHERE genero = 'F'")
    mujeres = cursor.fetchone()[0]
    conexion.close()
    return mujeres

def retribucion_media_mujeres():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT AVG(salario_mensual * num_pagas) FROM empleados WHERE genero = 'F'")
    media = cursor.fetchone()[0]
    conexion.close()
    return media

def porcentaje_hombres():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM empleados WHERE genero = 'M'")
    hombres = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM empleados")
    total = cursor.fetchone()[0]
    porcentaje = (hombres / total) * 100 if total > 0 else 0
    conexion.close()
    return porcentaje

def numero_hombres():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM empleados WHERE genero = 'M'")
    hombres = cursor.fetchone()[0]
    conexion.close()
    return hombres

def retribucion_media_hombres():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT AVG(salario_mensual * num_pagas) FROM empleados WHERE genero = 'M'")
    media = cursor.fetchone()[0]
    conexion.close()
    return media



root.mainloop()