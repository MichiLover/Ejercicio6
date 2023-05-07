class ViajeroFrecuente:
    __numero=''
    __dni=''
    __nombre=''
    __apellido=''
    __millas=0

    def __init__(self,numero,dni,nombre, apellido,millas):
        self.__numero = numero
        self.__dni= dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas = int(millas)

        print("Numero del viajero: {}".format(self.__numero))
        print("Documento del viajero: {}".format(self.__dni))
        print("Nombre del viajero: {}".format(self.__nombre))
        print("Apellido del viajero: {}".format(self.__apellido))
        print("Millas del viajero: {}".format(self.__millas))

    def getNumero(self):
        return self.__numero

    def getDocumento(self):
        return self.__dni

    def getNombre(self) :
        return self.__nombre

    def getApellido(self) :
        return self.__apellido

    def getMillas(self):
        return self.__millas


    #Determinar el/los viajero/s con mayor cantidad de millas acumuladas.
    #gt= Greather than
    def __gt__ (self,otro):
        if type (otro) == ViajeroFrecuente:
            return (self.__millas > otro.getMillas())
        elif type (otro) == int:
            return (self.__millas > otro)
        else :
            return None

    #Acumulador
    def __add__(self,otro):
        return self.__millas + otro.getMillas()


    def __sub__(self, millas_a_canjear):
        self.__millas -= int(millas_a_canjear)
        return self.__millas
