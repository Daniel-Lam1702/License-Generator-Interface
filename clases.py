#Elaborado por Daniel Eduardo Lam He
#Fecha de creación: 06/06/2021 1:28 pm
#Última fecha de modificación: 06/06/2021 5:00 pm
#Versión:3.9.5

#Definición de clase
class Conductores:
    """
        Método constructor = Crea la estructura de la clase Bebidas
        Método que se llama al instanciar
    """
    def __init__(self,pCedula,pNombre,pFechaNacimiento,pFechaExpedicion,pFechaVenc,pLicencia,pSangre,pDonador,pSede,pPuntaje,pCorreo):
        self.cedula=pCedula
        self.nombre=pNombre
        self.fechaNacimiento=pFechaNacimiento
        self.fechaExpedicion=pFechaExpedicion
        self.fechaVencimiento=pFechaVenc
        self.tipoLicencia=pLicencia
        self.tipoSangre=pSangre
        self.donador=pDonador
        self.sede=pSede
        self.puntaje=pPuntaje
        self.correo=pCorreo
        return
    def setCedula(self,pCedula):
        """
        F: Asigna la cedula de le conductor
        E: cedula del conductor (str)
        S: Asigna un numero al atributo cedula
        """ 
        self.cedula=pCedula
        return
    def getCedula(self):
        """
        F: Obtiene el la cedula del conductor
        E: NA
        S: cedula
        """
        return self.cedula
    def setNombre(self,pNombre):
        """
        F: Asigna el un nombre al conductor
        E: nombre del conductor (str)
        S: Asigna un nombre al atributo nombre del conductor
        """ 
        self.nombre=pNombre
        return
    def getNombre(self):
        """
        F: Obtiene el nombre 
        E: NA
        S: nombre del/ la conductora
        """
        return self.nombre
    def setFechaNacimiento(self,pFechaNacimiento):
        """
        F: Asigna el una fecha de nacimiento
        E: fecha de nacimiento (str)
        S: Asigna una fecha al atributo fecha de nacimiento
        """ 
        self.fechaNacimiento=pFechaNacimiento
        return
    def getFechaNacimiento(self):
        """
        F: Obtiene la fecha de nacimiento
        E: NA
        S: fecha de nacimiento del/ la conductora
        """
        return self.fechaNacimiento
    def setFechaExpedicion(self,pFechaExpedicion):
        """
        F: Asigna una fecha de expedicion
        E: fecha de expedicion de la licencia (str)
        S: Asigna una fecha al atributo fecha de expedicion
        """ 
        self.fechaExpedicion=pFechaExpedicion
        return
    def getFechaExpedicion(self):
        """
        F: Obtiene la fecha de expedicion
        E: NA
        S: fecha de expedicion de la licencia
        """
        return self.fechaExpedicion
    def setFechaVencimiento(self,pFechaVenc):
        """
        F: Asigna una fecha de vencimiento
        E: fecha de vencimiento (str)
        S: Asigna una fecha al atributo fecha de vencimiento
        """ 
        self.fechaVencimiento=pFechaVenc
        return
    def getFechaVencimiento(self):
        """
        F: Obtiene la fecha de venciminto
        E: NA
        S: fecha de vencimiento de la licencia
        """
        return self.fechaVencimiento
    def setTipoLicencia(self,pLicencia):
        """
        F: El tipo de licencia
        E: tipo de licencia (str)
        S: Asigna un codigo al atributo tipo de licencia
        """ 
        self.tipoLicencia=pLicencia
        return
    def getTipoLicencia(self):
        """
        F: Obtiene el tipo de licencia
        E: NA
        S: tipo de licencia
        """
        return self.tipoLicencia
    def setTipoSangre(self,pSangre):
        """
        F: Asigna el codigo al tipo de sangre
        E: tipo de sangre (str)
        S: Asigna un codigo al atributo tipo de sangre
        """ 
        self.tipoSangre=pSangre
        return
    def getTipoSangre(self):
        """
        F: Obtiene el tipo de sangre
        E: NA
        S: tipo de sangre
        """
        return self.tipoSangre
    def setDonador(self,pDonador):
        """
        F: Asigna los donadores
        E: donador (bool)
        S: Asigna un valor al atributo donador
        """ 
        self.donador=pDonador
        return
    def getDonador(self):
        """
        F: Obtiene si el conductor es donador
        E: NA
        S: donador
        """
        return self.donador
    def setSede(self,pSede):
        """
        F: Asigna el la sede
        E: sede del conductor (str)
        S: Asigna una sede al atributo sede
        """ 
        self.sede=pSede
        return
    def getSede(self):
        """
        F: Obtiene la sede
        E: NA
        S: sede de la licencia
        """
        return self.sede
    def setPuntaje(self,pPuntaje):
        """
        F: Asigna el puntaje
        E: puntaje (int)
        S: Asigna un codigo al atributo puntaje
        """ 
        self.puntaje=pPuntaje
        return
    def getPuntaje(self):
        """
        F: Obtiene el puntaje de la licencia
        E: NA
        S: puntaje de la licencia
        """
        return self.puntaje
    def setCorreo(self,pCorreo):
        """
        F: Asigna el correo del conductor
        E: correo del conductor (str)
        S: Asigna un codigo al atributo correo del conductor
        """ 
        self.correo=pCorreo
        return
    def getCorreo(self):
        """
        F: Obtiene el correo del o la conductora
        E: NA
        S: correo del o la conductora
        """
        return self.correo
    def mostrarTodo(self):
        """
        Funcionamiento:Obtiene todos los datos de los conductores
        Entradas:NA
        Salidas:Datos del o la conductora
        """
        return [self.cedula,self.nombre,self.fechaNacimiento,self.fechaExpedicion,
        self.fechaVencimiento,self.tipoLicencia,self.tipoSangre,self.donador,self.sede,
        self.puntaje,self.correo]