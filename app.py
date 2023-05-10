from tkinter import *
from tkinter import messagebox

# -------------------------
# funciones de la app
# -------------------------

def guardar_registro_academico(nombre, apellido, codigo, carrera, semestre):
    datos = f"Nombre: {nombre}\nApellido: {apellido}\nCódigo: {codigo}\nCarrera: {carrera}\nSemestre: {semestre}\n"

    with open("registros_academicos.txt", "a") as archivo:
        archivo.write(datos) 

def regristrar_toplevel_acedemi():
    global toplevel_academidats
    toplevel_academidats = Toplevel()
    toplevel_academidats.title("REGISTRO ACADÉMICO")
    toplevel_academidats.resizable(0, 0)
    toplevel_academidats.geometry("600x600")
    toplevel_academidats.config(bg="gray64") 



    # etiqueta para valor en centigrados
    lb_nom = Label(toplevel_academidats, text="Nombres: ")
    lb_nom.config(bg="grey", fg="black", font=("Helvetica", 13), bd=2)
    lb_nom.place(x=10, y=100, width=160, height=33)

    entry_nom = Entry(toplevel_academidats)
    entry_nom.config(bg="white", fg="black")
    entry_nom.focus_set()
    entry_nom.place(x=200, y=100)

    lb_ape = Label(toplevel_academidats, text="Apellidos: ")
    lb_ape.config(bg="grey", fg="black", font=("Helvetica", 13), bd=2)
    lb_ape.place(x=10, y=140, width=160, height=33)

    entry_ape = Entry(toplevel_academidats)
    entry_ape.config(bg = "white", fg = "black")
    entry_ape.focus_set()
    entry_ape.place(x = 200, y = 140)

    lb_cod = Label(toplevel_academidats, text="Código: ")
    lb_cod.config(bg="grey", fg="black", font=("Helvetica", 13), bd=2)
    lb_cod.place(x=10, y=180, width=160, height=33)

    entry_cod = Entry(toplevel_academidats)
    entry_cod.config(bg = "white", fg = "black")
    entry_cod.focus_set()
    entry_cod.place(x = 200, y = 180)
    


    lb_car = Label(toplevel_academidats, text="Carrera: ")
    lb_car.config(bg="grey", fg="black", font=("Helvetica", 13), bd=2)
    lb_car.place(x=10, y=221, width=160, height=33)
     
    entry_car = Entry(toplevel_academidats)
    entry_car.config(bg = "white", fg = "black")
    entry_car.focus_set()
    entry_car.place(x = 200, y = 221) 
    
    lb_sem = Label(toplevel_academidats, text="Semestre: ")
    lb_sem.config(bg="grey", fg="black", font=("Helvetica", 13), bd=2)
    lb_sem.place(x=10, y=261, width=160, height=33)

    entry_sem = Entry(toplevel_academidats)
    entry_sem.config(bg = "white", fg = "black",)
    entry_sem.focus_set()
    entry_sem.place(x = 200, y = 261)
    

    lb_resultados = Label(toplevel_academidats)
    lb_resultados.config(bg = "grey", fg = "black", font = ("Helvetica", 13))
    lb_resultados.place(x = 10, y = 380, width = 580, height = 200)

    def guardar_datos():
        nombre_valor = entry_nom.get()
        apellido_valor = entry_ape.get()
        codigo_valor = entry_cod.get()
        carrera_valor = entry_car.get()
        semestre_valor = entry_sem.get()

        guardar_registro_academico(nombre_valor, apellido_valor, codigo_valor, carrera_valor, semestre_valor)
        messagebox.showinfo("Registro exitoso", "Los datos se han guardado correctamente.")

    bt_aceptar = Button(toplevel_academidats, text="Enter", command=guardar_datos)
    bt_aceptar.place(x=450, y=325, width=100, height=30)

#-------------------------------------------------------------------------------------------------------------------

def guardar_registro_medico(nombre, apellido, documento, Eps,sangre ):
    datos = f"Nombre: {nombre}\nApellido: {apellido}\nDocumento: {documento}\nEps: {Eps}\ntipo de sangre: {sangre}\n"
    
    

    with open("registros_médicos.txt", "a") as archivo:
        archivo.write(datos)

def regristrar_toplevel_medic():
    global toplevel_medidats
    toplevel_medidats = Toplevel()
    toplevel_medidats.title("REGISTRO MÉDICO")
    toplevel_medidats.resizable(0, 0)
    toplevel_medidats.geometry("600x600")
    toplevel_medidats.config(bg="gray64")

    barramenu = Menu(toplevel_medidats)
    toplevel_medidats.config(menu = barramenu,  width = 300, height = 300 )
    archivomenu = Menu(barramenu, tearoff = 0)
    archivomenu.add_command(label = "guardar")
    archivomenu.add_separator()
    archivomenu.add_command(label = "cerrar")
    archivomenu.add_separator()
    archivomenu.add_command(label = "salir")
    archivomenu.add_separator()


    archivoedicion = Menu(barramenu, tearoff = 0)
    archivoedicion.add_command(label = "maximizar (+)")
    archivomenu.add_separator()
    archivoedicion.add_command(label = "minimizar (-)")
    archivomenu.add_separator()
    archivoedicion.add_command(label = "peguelo")
    archivomenu.add_separator()

    archivoherraminetas = Menu(barramenu, tearoff = 0)

    archivoayuda = Menu(barramenu, tearoff = 0)
    archivomenu.add_separator()
    archivoayuda.add_command(label = "licencia")
    archivomenu.add_separator()
    archivoayuda.add_command(label = "acerca de ...")
    archivomenu.add_separator()


#----------------------------barra menú----------------------

    barramenu.add_cascade(label = "archivo", menu = archivomenu)
    barramenu.add_cascade(label = "edicion", menu = archivoedicion)
    barramenu.add_cascade(label = "herramientas", menu = archivoherraminetas)
    barramenu.add_cascade(label = "ayuda", menu = archivoayuda)




    # etiqueta para valor en centigrados
    lb_nom = Label(toplevel_medidats, text="Nombres: ")
    lb_nom.config(bg="grey", fg="black", font=("Helvetica", 13), bd=2)
    lb_nom.place(x=10, y=100, width=160, height=33)

    entry_nom = Entry(toplevel_medidats)
    entry_nom.config(bg="white", fg="black")
    entry_nom.focus_set()
    entry_nom.place(x=200, y=100)

    lb_ape = Label(toplevel_medidats, text="Apellidos: ")
    lb_ape.config(bg="grey", fg="black", font=("Helvetica", 13), bd=2)
    lb_ape.place(x=10, y=140, width=160, height=33)

    entry_ape = Entry(toplevel_medidats)
    entry_ape.config(bg = "white", fg = "black")
    entry_ape.focus_set()
    entry_ape.place(x = 200, y = 140)

    lb_cod = Label(toplevel_medidats, text="Tipo de documento: ")
    lb_cod.config(bg="grey", fg="black", font=("Helvetica", 13), bd=2)
    lb_cod.place(x=10, y=180, width=160, height=33)

    entry_cod = Entry(toplevel_medidats)
    entry_cod.config(bg = "white", fg = "black")
    entry_cod.focus_set()
    entry_cod.place(x = 200, y = 180)

    lb_car = Label(toplevel_medidats, text="Eps: ")
    lb_car.config(bg="grey", fg="black", font=("Helvetica", 13), bd=2)
    lb_car.place(x=10, y=221, width=160, height=33)
     
    entry_car = Entry(toplevel_medidats)
    entry_car.config(bg = "white", fg = "black")
    entry_car.focus_set()
    entry_car.place(x = 200, y = 221) 
    
    lb_sem = Label(toplevel_medidats, text="Tipo de sangre: ")
    lb_sem.config(bg="grey", fg="black", font=("Helvetica", 13), bd=2)
    lb_sem.place(x=10, y=261, width=160, height=33)

    entry_sem = Entry(toplevel_medidats)
    entry_sem.config(bg = "white", fg = "black",)
    entry_sem.focus_set()
    entry_sem.place(x = 200, y = 261)
    

    lb_resultados = Label(toplevel_medidats)
    lb_resultados.config(bg = "grey", fg = "black", font = ("Helvetica", 13))
    lb_resultados.place(x = 10, y = 380, width = 580, height = 200)   
    

    bt_aceptar = Button(toplevel_medidats, text="Enter")
    bt_aceptar.place(x=450, y=325, width=100, height=30)

    def guardar_datos():
        nombre_valor = entry_nom.get()
        apellido_valor = entry_ape.get()
        doc_valor = entry_cod.get()
        Eps_valor = entry_car.get()
        sangre_valor = entry_sem.get()

        guardar_registro_medico(nombre_valor, apellido_valor, doc_valor, Eps_valor, sangre_valor)
        messagebox.showinfo("Registro exitoso", "Los datos se han guardado correctamente.")

    bt_aceptar = Button(toplevel_medidats, text="Enter", command=guardar_datos)
    bt_aceptar.place(x=450, y=325, width=100, height=30)


ventana_principal = Tk()

ventana_principal.title("Registros.com")


ventana_principal.geometry("500x500")

ventana_principal.resizable(0,0)
ventana_principal.config(bg="grey")

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=70)
frame_entrada.place(x=10, y=10)

datos_academicos = Entry(frame_entrada)
datos_academicos.config()

titulo = Label(frame_entrada, text="DATOS  ACADÉMICOS Y MÉDICOS")
titulo.config(bg="white", fg="black", font=("arial", 12))
titulo.place(x=100, y=30)

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=520)
frame_operaciones.place(x=10, y=90)



bt_iniciar = Button(frame_operaciones, text="REGISTRO ACADÉMICO", command=regristrar_toplevel_acedemi)
bt_iniciar.place(x=25, y=30, width=200)


bt_iniciar2 = Button(frame_operaciones, text="REGISTRO MÉDICO", command = regristrar_toplevel_medic)
bt_iniciar2.place(x=250, y=30, width=200)


ventana_principal.mainloop() #crea un registro dentro de cada toplevel que lleve nombre apeelido codigo carrera y semestre de tal modo que al digitar los datos y dar enter queden guardados en un doc

