class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
    
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
        if self.peso > 8:
            print("Guau, Guau")
        else:
            print("guau, guau")

class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso > 8:
            print("Guau, Guau")
        else:
            print("guau, guau")
    
    def __str__(self):
        return "Perro: {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)
    
    
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
        #super().__init__(nombre, edad, peso)
        
    def __str__(self):
        return "Perro de Asistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{} ayudo a mi dueño, {} a pasear".format(self.nombre, self.amo))
        
    def ladrar(self):
        if self.__trabajando:
            print("Ssshhhh, estoy trabajando, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self,valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor