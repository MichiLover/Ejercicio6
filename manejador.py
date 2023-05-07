from Viajero import ViajeroFrecuente

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []
   
    def cargarViajero(self,num,dni,nom,ap,millas):
 
        newViajero = ViajeroFrecuente(num, dni, nom, ap, int(millas))
        self.__lista.append(newViajero)

        
    #Muestro todos los viajeros
    def showViajeros(self):
        print("Viajero con mayor cantidad de millas ")
        print('{} {} {} {} {}'.format('Numero','Documento','Nombre','Apellido','Millas'))
        for ViajeroFrecuente in self.__lista:
            num = ViajeroFrecuente.getNumero()
            dni = ViajeroFrecuente.getDocumento()
            nom = ViajeroFrecuente.getNombre()
            ap = ViajeroFrecuente.getApellido()
            millas= ViajeroFrecuente.getMillas()
            
        print ('{} {} {} {} {}'.format(num,dni,nom,ap,millas))


    #Ordena a los viajeros en orden descendente por numero de millas acumuladas.
    def ordenarViajeros(self):

        self.__lista.sort(reverse=False) #En orden descendente

    def sumar_millas(self):
        acum=0
        for ViajeroFrecuente in self.__lista:

            acum +=ViajeroFrecuente.getMillas()

        print("Acumulador total de millas es: {}".format(acum))


    def canjearMillas(self,canje):
    
        total= ViajeroFrecuente.getMillas() - canje
        return total

    def compara(self,num,dni,nom,ap,millas,xnumero):

        self.__numero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millas = int(millas)

        i=0
        encontrado = False

        while i < len(self.__lista) and not encontrado:
            if self.__lista[i] == xnumero:
                encontrado=True
            else:
                i+=1
        pos = i    
        return pos

    def canjear_millas(self, millas_a_canjear):
        millas_actuales = self.__millas
        if millas_a_canjear <= millas_actuales:
            self.__millas -= int(millas_a_canjear)
            print(f"{self.__millas} millas canjeadas correctamente. Millas restantes: {millas_a_canjear}.")
        else:
            print("No hay suficientes millas disponibles para canjear.")
        return self


