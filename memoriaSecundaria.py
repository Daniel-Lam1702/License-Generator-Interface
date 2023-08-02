#Elaborado por Daniel Eduardo Lam He y Miguel Brenes
#Fecha de creación: 06/06/2021 1:17 pm
#Última fecha de modificación: 06/06/2021 1:25 pm
#Versión 3.9.5
#Importación de librería
import pickle
#Llamada de funciones
def leer(nomArch):
    """
    Funcionamiento: Graba la informacion en la base de datos
    Entradas:
    -nomArch(nombre del archivo) a leer
    Salida:NA
    """
    lista=[]
    try:
        archivo=open(nomArch,"rb")
        lista=pickle.load(archivo)
        archivo.close()
    except:
        print()
    return lista
def grabar(nomArch,estructura):
    """
    Funcionamiento: guarda una lista a la memoria secundaria
    Entradas: 
    -nomArch: el nombre de archivo en donde se va guardar
    Estructura: estructura que se va a guardar
    Salida: NA
    """
    try:
        archivo=open(nomArch,"wb")
        pickle.dump(estructura,archivo)
        archivo.close()
    except:
        print()
    return
