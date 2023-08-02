#Elaborado por Daniel Eduardo Lam He y Miguel Aguilar Brenes
#Fecha de creación: 06/06/2021 2:56 pm
#Fecha de modificación: 21/06/2021 6:24 pm
#Versión: 3.9.5
#Llamada de librerías
from tkinter import *
from tkinter import messagebox
from clases import *
from funciones import *
from tkinter.font import Font
import re
from tkinter import ttk
#Definición de funciones
#Limpiar texto
"""
Funcionamiento:Encargado de limpiar lo que se introduzca en el menu
Entradas:pLista(Lista) que se va a limpiar
Salidas:NA
"""
def limpiar(pLista):
    for i in pLista:
        i.delete(0,END)
    return
#---------------------------------Generar XML-------------------------------------------------
def generarXMLAux():
    """
    Funcionamiento:Informa sobre el estado de la creacion del XML
    Entradas:NA
    Salidas:NA
    """
    
    try:
        if webScrapping():
            messagebox.showinfo("Generado","Se ha generado el XML correctamente")
        else:
            messagebox.showerror("Error","No se ha generado el XML")
    except:
        messagebox.showerror("Error","Se generó un error")
#---------------------------------Generar licencias----------------------------------------------------------------
def generarLicenciasAux(pCantidad,pVentanaGenerar):
    """
    Funcionamiento:Validar el numero de personas a generar
    Entradas:
    -pCantidad(int)cantidad de personas
    -pVentanaGenerar(ventana)
    Salidas:Valores booleanos
    """
    try:
        if int(pCantidad)>250 or int(pCantidad)<1:
            messagebox.showerror("Error","Debe ingresar una cantidad de personas entre 1 y 250",parent=pVentanaGenerar)
            return False
        return True
    except:
        messagebox.showerror("Error","Debe ingresar una cantidad numérica entera",parent=pVentanaGenerar)
        return False
def intermediarioGenerarLicencias(pCantidad,pVentanaGenerar):
    """
    Funcionamiento:Informa sobre el estado de la creacion de licencias
    Entradas:
    pCantidad(int)cantidad de personas a generar
    pVentanaGenerar(ventana)
    Salidas:NA
    """
    try:
        if generarLicenciasAux(pCantidad,pVentanaGenerar):
            generado=generarLicencias(int(pCantidad))
            if generado == True:
                messagebox.showinfo("Generado","Se generaron las licencias correctamente",parent=pVentanaGenerar) #Incluir una condicional para ver si true significa que se generaron y si false no se generaron
            elif generado=="Error":
                messagebox.showerror("Error","No se generaron las licencias. Debe generar el XML primero",parent=pVentanaGenerar)
            else:
                messagebox.showerror("Error","No se logró generar las licencias",parent=pVentanaGenerar)
        return
    except:
        messagebox.showerror("Error","Se generó un error al generar las licencias",parent=pVentanaGenerar)
        return
def opcionGenerarLicencias():
    """
    Funcionamiento:Interfaz para generar licencias
    Entradas:NA
    Salidas:NA
    """
    ventanaGenerar=Toplevel()
    ventanaGenerar.title("Generar Licencias")
    ventanaGenerar.geometry("800x800")
#Generar widgets
    Label(ventanaGenerar,text="Crear licencias").grid(column=0,row=0,columnspan=2,sticky="nswe")
    Label(ventanaGenerar,text="¿Para cuántas personas desea crear licencias?").grid(column=0,row=3,sticky="e")
    cantidad=Entry(ventanaGenerar,width=20)
    cantidad.grid(column=1,row=3,sticky="w")
#Generar Botones
    Button(ventanaGenerar,text="Generar",activebackground="lightblue",command=lambda:intermediarioGenerarLicencias(cantidad.get(),ventanaGenerar),pady=20,padx=31).grid(column=0,row=6,columnspan=2)
    Button(ventanaGenerar,text="Limpiar",activebackground="lightblue",command=lambda:limpiar([cantidad]),pady=20,padx=31).grid(column=0,row=7,columnspan=2)
    Button(ventanaGenerar,text="Regresar",activebackground="lightblue",command=ventanaGenerar.destroy,pady=20,padx=29).grid(column=0,row=8,columnspan=2)
#Organizar los widgets y botones
    for fila in range(9):
        Grid.rowconfigure(ventanaGenerar, fila, weight = 1)
    Grid.columnconfigure(ventanaGenerar, 0, weight = 1)
    Grid.columnconfigure(ventanaGenerar, 1, weight = 1)
#---------------------------Renovar licencia------------------------------------------------
def renovarLicenciaAux(pCedula,pVentana):
    """
    Funcionamiento:Valida el numero de cedula y el puntaje
    Entradas:
    pCedula:(str)Numero de cedula de la persona
    pVentana(ventana)
    Salidas:NA
    """
    objetos=leer("conductores")
    if re.match("^\d{9}$",pCedula)==None:
        messagebox.showerror("Error","Debe ingresar una cédula de 9 dígitos.",parent=pVentana)
        return False
    for objeto in objetos:
        if objeto.getCedula() == pCedula:
            if objeto.getPuntaje()>6:
                return True
            elif objeto.getPuntaje()>0:
                messagebox.showinfo("Renovar","El conductor con la cédula "+pCedula+" debe volver a hacer el examen teórico para renovar la licencia",parent=pVentana)
                return False
            else:
                messagebox.showinfo("Renovar","La licencia del conductor con la cédula "+pCedula+" ha sido retirada permanentemente. No podrá renovar la licencia.",parent=pVentana)
                return False
    messagebox.showerror("Error","La cédula "+pCedula+" que usted registró no se encuentra en la base de datos.",parent=pVentana)
    return False
def intermediarioRenovarLicencia(pCedula,pVentana):
    """
    Funcionamiento:Informa sobre el estado de renovar de licencias y sirve de intermediario
    pCedula:(str)Numero de cedula de la persona
    pVentana(ventana)
    Salidas:NA
    """
    try:
        if renovarLicenciaAux(pCedula,pVentana):
            if renovarLicencia(pCedula):
                messagebox.showinfo("Renovado","Se ha renovado la licencia de la cédula "+pCedula,parent=pVentana)
            else:
                messagebox.showerror("Error","No se logró renovar la licencia de la cédula "+pCedula,parent=pVentana)
        return
    except:
        messagebox.showerror("Error","Se generó un error.",parent=pVentana)
def opcionRenovarLicencia():
    """
    Funcionamiento:interfaz para renovar licencias
    Entradas:NA
    Salidas:NA
    """
    ventanaRenovar=Toplevel()
    ventanaRenovar.title("Renovar licencia")
    ventanaRenovar.geometry("720x720")
    Label(ventanaRenovar,text="Renovar licencia").grid(column=0,row=0,columnspan=2,sticky="nswe")
    Label(ventanaRenovar,text="Ingrese el número de la cédula que desea renovar").grid(column=0,row=3,sticky="e")
    cedula=Entry(ventanaRenovar,width=40)
    cedula.grid(column=1,row=3,sticky="w")
    Button(ventanaRenovar,text="Renovar",activebackground="lightblue",command=lambda:intermediarioRenovarLicencia(cedula.get(),ventanaRenovar),pady=20,padx=31).grid(column=0,row=6,columnspan=2)
    Button(ventanaRenovar,text="Limpiar",activebackground="lightblue",command=lambda:limpiar([cedula]),pady=20,padx=31).grid(column=0,row=7,columnspan=2)
    Button(ventanaRenovar,text="Regresar",activebackground="lightblue",command=ventanaRenovar.destroy,pady=20,padx=29).grid(column=0,row=8,columnspan=2)
    for fila in range(9):
        Grid.rowconfigure(ventanaRenovar, fila, weight = 1)
    Grid.columnconfigure(ventanaRenovar, 0, weight = 1)
    Grid.columnconfigure(ventanaRenovar, 1, weight = 1)
#############################Generar PDF######################
def generarPdfAux(pCedula,pVentana):
    """
    Funcionamiento:Validar el numero de cedula
    Entradas:
    pCedula:(str)Numero de cedula de la persona
    pVentana(ventana)
    Salidas:Valores boleanos
    """
    clases=leer("conductores")
    if re.match("^\d{9}$",pCedula)==None:
        messagebox.showerror("Error","La cédula debe contener 9 dígitos.",parent=pVentana)
        return False
    for objeto in clases:
        if objeto.getCedula() == pCedula:
            return True
    else:
        messagebox.showinfo("Error","No se puede generar el PDF del conductor con la cédula "+pCedula+". No se encontró en la base de datos.",parent=pVentana)
        return False
def intermediarioGenerarPdf(pCedula,pVentana):
    """
    Funcionamiento:Informa sobre el estado de generar PDF y sirve de intermediario
    Entradas:
    pCedula:(str)Numero de cedula de la persona
    pVentana(ventana)
    Salidas:NA
    """
    try:
        if generarPdfAux(pCedula,pVentana):
            if generarPdf(pCedula):
                messagebox.showinfo("Generado","Se ha generado el PDF de la cédula "+pCedula,parent=pVentana)
            else:
                messagebox.showerror("Error","No se logró crear el PDF de la cédula "+pCedula,parent=pVentana)
        return 
    except:
        messagebox.showerror("Error","Se generó un error.",parent=pVentana)
def opcionGenerarPDF():
    """
    Funcionamiento:Interfaz sobre generar PDF
    Entradas:NA
    Salidas:NA
    """
    ventanaPDF=Toplevel()
    ventanaPDF.title("Generar PDF")
    ventanaPDF.geometry("720x720")
    Label(ventanaPDF,text="Generar PDF").grid(column=0,row=0,columnspan=2,sticky="nswe")
    Label(ventanaPDF,text="Ingrese el número de la cédula para el que desea generar el pdf").grid(column=0,row=3,sticky="e")
    cedula=Entry(ventanaPDF,width=40)
    cedula.grid(column=1,row=3,sticky="w")
    Button(ventanaPDF,text="Generar",activebackground="lightblue",command=lambda:intermediarioGenerarPdf(cedula.get(),ventanaPDF),pady=20,padx=31).grid(column=0,row=6,columnspan=2)
    Button(ventanaPDF,text="Limpiar",activebackground="lightblue",command=lambda:limpiar([cedula]),pady=20,padx=31).grid(column=0,row=7,columnspan=2)
    Button(ventanaPDF,text="Regresar",activebackground="lightblue",command=ventanaPDF.destroy,pady=20,padx=29).grid(column=0,row=8,columnspan=2)
    for fila in range(9):
        Grid.rowconfigure(ventanaPDF, fila, weight = 1)
    Grid.columnconfigure(ventanaPDF, 0, weight = 1)
    Grid.columnconfigure(ventanaPDF, 1, weight = 1)
#--------------------------------Acerca de-----------------------------------
def acercaDe():
    """
    Funcionamiento:Muestra los datos sobre los programadores
    Entradas:NA
    Salidas:NA
    """
    ventanaAcerca=Toplevel()
    ventanaAcerca.geometry("720x720")
    ventanaAcerca.title("Sobre nosotros")
    Label(ventanaAcerca,text="Contáctenos",font=Font(weight="bold")).grid(column=0,row=0)
    Label(ventanaAcerca,text="Miguel Aguilar Brenes",font=Font(weight="bold")).grid(column=0,row=1)
    Label(ventanaAcerca,text="Número de teléfono: 8453 7698").grid(column=0,row=2)
    Label(ventanaAcerca,text="Correo: mig.aguilar01@gmail.com").grid(column=0,row=3)
    Label(ventanaAcerca,text="Daniel Eduardo Lam He",font=Font(weight="bold")).grid(column=0,row=4)
    Label(ventanaAcerca,text="Número de teléfono: 7213 7264").grid(column=0,row=5)
    Label(ventanaAcerca,text="Correo: danieleduardolamhe@gmail.com").grid(column=0,row=6)
    Button(ventanaAcerca,text="Salir",command=ventanaAcerca.destroy).grid(column=0,row=7)
    for fila in range(8):
        Grid.rowconfigure(ventanaAcerca, fila, weight = 1)
    Grid.columnconfigure(ventanaAcerca, 0, weight = 1)
#--------------------------Reportes-----------------------------------
#--------------------------Reportes licencia-----------------------------------
def opcionReporteLicencias(pVentana):
    """
    Funcionamiento:Informa sobre el estado de generar el reporte de licencias
    Entradas:pVentana(ventana)
    Salidas:NA
    """
    if generarReporteLicencia():
        messagebox.showinfo("Generado","Se ha generado el reporte correctamente.",parent=pVentana)
    else:
        messagebox.showerror("No generado","No se ha generado el reporte correctamente.",parent=pVentana)
    return
#------------------ReporteTipoLicencia----------
def intermediarioTipoLicencia(pTipo,pVentana):
    """
    Funcionamiento:Informa sobre el estado del reporte tipo de licencia y sirve de intermediario
    Entradas:
    pTipo (str)tipo de licencia
    pVentana(Ventana)a mostrar
    Salidas:NA
    """
    if reporteTipoLicencia(pTipo):
        messagebox.showinfo("Generado","Se ha generado el reporte correctamente.",parent=pVentana)
    else:
        messagebox.showerror("Error","No se ha generado el reporte correctamente.",parent=pVentana)
#...................Reporte por Tipo de cédula..........................
def opcionReportePorTipoLicencia():
    """
    Funcionamiento:Interfaz que muestra los tiposd de licencia para el reporte
    Entradas:NA
    Salidas:NA
    """
    VentanaTipo=Toplevel()
    VentanaTipo.title("Reporte por Tipo Licencia")
    VentanaTipo.geometry("720x720")
    Label(VentanaTipo,text="Reporte por Tipo").grid(column=0,row=0)
    Label(VentanaTipo,text="Seleccione el tipo de licencia").grid(column=0,row=1)
    tipo= ttk.Combobox(VentanaTipo, value= ["A","B","C","D","E"],state="readonly",width=50)
    tipo.current(0)
    tipo.grid(row=3,column=0)
    Button(VentanaTipo,text="Generar",padx=38,pady=20,command=lambda: intermediarioTipoLicencia(tipo.get(),VentanaTipo)).grid(row=5,column=0)
    Button(VentanaTipo,text="Salir",padx=48,pady=20,command=VentanaTipo.destroy).grid(column=0,row=6)
    for fila in range(7):
        Grid.rowconfigure(VentanaTipo, fila, weight = 1)
    Grid.columnconfigure(VentanaTipo, 0, weight = 1)
    return 
#Reporte examen++++++++++++++++++++++++++++++++++++++++++++++++++++++
def opcionReporteExamen(pVentana):
    """
    Funcionamiento:Informa y sirve de intermediario con reporte de examen
    Entradas:pVentana(ventana) a mostrar
    Salidas:NA
    """
    if examenPorSancion():
        messagebox.showinfo("Generado","Se ha generado el reporte correctamente.",parent=pVentana)
    else:
        messagebox.showerror("No generado","No se ha generado el reporte correctamente.",parent=pVentana)
    return
#-------------------------Opcion por donantes------------------------
def opcionReporteDonantesOrganos(pVentana):
    """
    Funcionamiento:Informa y sirve de intermediario con reporte donantes de organos
    Entradas:pVentana(ventana) a mostrar
    Salidas:NA
    """
    if generarListaDonantesOrganos():
        messagebox.showinfo("Generado","Se ha generado el reporte correctamente.",parent=pVentana)
    else:
        messagebox.showerror("No generado","No se ha generado el reporte correctamente.",parent=pVentana)
    return
#--------------------------Opcion por anulado--------------------------------------
def opcionReporteAnulados(pVentana):
    """
    Funcionamiento:Informa y sirve de intermediario con los conductores anulados
    Entradas:pVentana(ventana)
    Salidas:NA
    """
    if generarListaAnulados():
        messagebox.showinfo("Generado","Se ha generado el reporte correctamente.",parent=pVentana)
    else:
        messagebox.showerror("No generado","No se ha generado el reporte correctamente.",parent=pVentana)
    return   
#--------------------------Opción por Sede---------------------------------------------
def intermediarioGenerarReportePorSede(pSede,pVentana):
    """
    Funcionamiento:Informa y sirve de intermediario con reporte de sede
    Entradas:pSede:(str) le tipo de sede
    pVentana(ventana)
    Salidas:NA
    """
    if generarListaPorSede(pSede):
        messagebox.showinfo("Generado","Se ha generado el reporte correctamente.",parent=pVentana)
    else:
        messagebox.showerror("No generado","No se ha generado el reporte correctamente.",parent=pVentana)
def opcionReportePorSede():
    """
    Funcionamiento:Interfaz para el reporte por sede
    Entradas:NA
    Salidas:NA
    """
    VentanaSede=Toplevel()
    VentanaSede.title("Reporte por sede")
    VentanaSede.geometry("720x720")
    Label(VentanaSede,text="Reporte por sede").grid(column=0,row=0)
    Label(VentanaSede,text="¿De cuál sede desea obtener las licencias?").grid(column=0,row=1)
    sede= ttk.Combobox(VentanaSede, value= ["San Sebastián","Pérez Zeledón","Montecillos Alajuela","Tránsito San Ramón","San Carlos",
    "Tránsito Cartago","Barva de Heredia","Liberia","Nicoya","Chacarita Puntarenas","Río Claro de Golfito",
    "Guápiles","Terminal de contenedores de SELDECA Limón"],state="readonly",width=50)
    sede.current(0)
    sede.grid(row=3,column=0)
    Button(VentanaSede,text="Generar",padx=38,pady=20,command=lambda: intermediarioGenerarReportePorSede(sede.get(),VentanaSede)).grid(row=5,column=0)
    Button(VentanaSede,text="Salir",padx=48,pady=20,command=VentanaSede.destroy).grid(column=0,row=6)
    for fila in range(7):
        Grid.rowconfigure(VentanaSede, fila, weight = 1)
    Grid.columnconfigure(VentanaSede, 0, weight = 1)
    return  
def boton5():
    """
    funcionamiento: Ventanas y botones para generar los reportes
    Entrada: NA
    Salida: NA
    """
    ventana_5 = Toplevel()
    ventana_5.title("Reportes")
    ventana_5.geometry("720x720")
    Label(ventana_5,text="Seleccione el tipo de reporte a crear",font=Font(weight="bold")).grid(row=0,column=0)
    Button(ventana_5,text="Totalidad de licencias", activebackground="lightblue",command=lambda:opcionReporteLicencias(ventana_5),padx=60,pady=22).grid(row=1,column=0)
    Button(ventana_5,text="Por tipo de licencia", activebackground="lightblue",command=opcionReportePorTipoLicencia,padx=47,pady=22).grid(row=2,column=0)
    Button(ventana_5,text="Examen por sanción", activebackground="lightblue",command=lambda:opcionReporteExamen(ventana_5),padx=47,pady=22).grid(row=3,column=0)
    Button(ventana_5,text="Los donantes de órganos", activebackground="lightblue",command= lambda: opcionReporteDonantesOrganos(ventana_5),padx=47,pady=22).grid(row=4,column=0)
    Button(ventana_5,text="Licencia anulada", activebackground="lightblue",command= lambda: opcionReporteAnulados(ventana_5),padx=68,pady=22).grid(row=5,column=0)
    Button(ventana_5,text="Licencias por sede", activebackground="lightblue",command= opcionReportePorSede,padx=63,pady=22).grid(row=6,column=0)
    Button(ventana_5,text="Salir", activebackground="lightblue",command= ventana_5.destroy,padx=100,pady=22).grid(row=7,column=0)
#Organizacion de widgets
    for i in range(8):
        Grid.rowconfigure(ventana_5, i, weight = 1)
    Grid.columnconfigure(ventana_5, 0, weight = 1)
    return
#--------------------------------Salir---------------------------------------
def salir():
    """
    Funcionamiento:Opcion para salir
    Entradas:NA
    Salidas:NA
    """
    respuesta = messagebox.askyesno("Salida","¿Desea salir?")
    if respuesta:
        messagebox.showinfo("Salir","No olvides gestionar pronto tu licencia")
        ventanaPrincipal.destroy()
    return
#Menu
def menu():
    """
    Funcionamiento:muestra el menu principal
    Entradas:NA
    Salidas:NA
    """
    global ventanaPrincipal
    ventanaPrincipal = Tk()
    ventanaPrincipal.title("Ventana Principal")
    ventanaPrincipal.geometry("1080x1080")
    Label(ventanaPrincipal,text="Licencias de Conducir de Costa Rica\n¿Qué desea realizar?",font=Font(weight="bold"),pady = 20).grid(row = 0,column = 0,sticky = "nsew")
    Button(ventanaPrincipal, text="Crear XML", command = generarXMLAux,pady = 25, padx = 105, activebackground="lightblue").grid(row = 1 ,column = 0)
    Button(ventanaPrincipal, text="Crear licencias", command = opcionGenerarLicencias,pady = 25, padx = 95, activebackground="lightblue").grid(row = 2 ,column = 0)
    Button(ventanaPrincipal, text="Renovar licencias", command = opcionRenovarLicencia,pady = 25, padx = 90, activebackground="lightblue").grid(row = 3 ,column = 0)
    Button(ventanaPrincipal, text="Generar PDF", command = opcionGenerarPDF,pady = 25, padx = 105, activebackground="lightblue").grid(row = 4 ,column = 0)
    Button(ventanaPrincipal, text="Reportes de Excel", command = boton5,pady = 25, padx = 95, activebackground="lightblue").grid(row = 5 ,column = 0)
    Button(ventanaPrincipal, text="Acerca de", command = acercaDe,pady = 25, padx = 118, activebackground="lightblue").grid(row = 6 ,column = 0)
    Button(ventanaPrincipal, text="Salir", command = salir,pady = 25, padx = 135, activebackground="lightblue").grid(row = 7 ,column = 0)
    for i in range(8):
        Grid.rowconfigure(ventanaPrincipal, i, weight = 1)
    Grid.columnconfigure(ventanaPrincipal, 0, weight = 1)
    #Se abre la ventana
    ventanaPrincipal.mainloop()
    return
#Programa principal
menu()