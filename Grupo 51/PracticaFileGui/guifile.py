from tkinter import*

gui = Tk()
gui.title("Practica Clase")
gui.geometry("500x400")
textActividad = Entry(gui)
textTiempo = Entry(gui)
def menu1():
    frameBotones = Frame(gui)
    B1 = Button(frameBotones,text="Preguntar",command=preguntar).grid(row=0,column=0) 
    B2 = Button(frameBotones,text="Reporte",command=Reporte).grid(row=0,column=1) 
    B3 = Button(frameBotones,text="Borrar").grid(row=0,column=2) 
    B4 = Button(frameBotones,text="Leer encuesta").grid(row=0,column=3)
    B5 = Button(frameBotones,text="Otro menú",command=menu2).grid(row=0,column=4)
    frameBotones.place(x=60, y=20, width=400, height=24)
    gui.update()
    
def menu2():
    labelBorrar = Label(gui,text="")
    labelBorrar.place(x=60, y=40, width=400, height=300)
    frameBotones2 = Frame(gui)
    B12 = Button(frameBotones2,text="2 Preguntar").grid(row=0,column=0) 
    B22 = Button(frameBotones2,text="2 Reporte").grid(row=0,column=1) 
    B32 = Button(frameBotones2,text="2 Borrar").grid(row=0,column=2) 
    B42 = Button(frameBotones2,text="2 Leer encuesta").grid(row=0,column=3)
    B52 = Button(frameBotones2,text="2 Otro menú",command=menu1).grid(row=0,column=4) 
    frameBotones2.place(x=60, y=20, width=400, height=24)
    gui.update()    

def error():
    labelBorrar = Label(gui,text="")
    labelBorrar.place(x=60, y=40, width=400, height=300)
    labelError = Label(text="Error en el ingreso de los datos",fg="white", bg="red")
    labelError.place(x=60, y=80, width=400, height=25)
    gui.update()

def updateEncuesta(nuevalinea):
    print("Actualizando encuesta")
    arrayLineas=[]
    with open('encuesta.txt','r',encoding="UTF-8") as f:
        for linea in f:
            arrayLineas.append(linea[:-1:])
    f.close
    f = open('encuesta.txt','w',encoding="UTF-8")

def ingresarEncuesta():
    tiempo = int(textTiempo.get())
    actividad = int(textActividad.get())
    print("Se ingresan los datos")
    print("Tiempo ->",tiempo)
    print("Actividad ->",actividad)
    if tiempo >0 and tiempo <5 and actividad >0 and actividad <6:
        nuevalinea=str(tiempo)+"-"+str(actividad)+"-"
        updateEncuesta(nuevalinea)
        print("Se guarda en el txt")
    else:
        error()

def preguntar():
    global textActividad
    global textTiempo
    labelBorrar = Label(gui,text="")
    labelBorrar.place(x=60, y=40, width=400, height=260)
    labelTiempo = Label(gui,text="Tiempo libre \n (1) Menos de 3 horas \n (2) Entre 3 y 6 horas \n (3) Entre 6 y 9 horas \n (4) Más de 9 horas")
    labelTiempo.place(x=60, y=80, width=150, height=80)
    textTiempo = Entry(gui)
    textTiempo.place(x=220, y=100, width=60, height=60)
    labelActividad = Label(gui,text="Actividad principal \n (1) Leer \n (2) Ver TV \n (3) Deporte \n (4) Dormir \n (5) Otra")
    labelActividad.place(x=60, y=170, width=150, height=90)
    textActividad = Entry(gui)
    textActividad.place(x=220, y=190, width=60, height=60)
    BotonPreguntar = Button(gui, text="Ingresar",command=ingresarEncuesta)
    BotonPreguntar.place(x=180, y=280)
    gui.update()
    
def Reporte():
    labelBorrar = Label(gui,text="")
    labelBorrar.place(x=60, y=40, width=400, height=300)
    labelBorrar = Label(gui,text="")
    labelBorrar.place(x=60, y=40, width=400, height=260)
    labelReporte = Label(gui,text="Reporte")
    labelReporte.place(x=60, y=80, width=150, height=80)
    gui.update()

menu1()
gui.mainloop()
