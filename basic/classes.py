
class Mensch:

    __counter = 0
    
    def __init__(this, alter=None, name=None):  #Konstruktor
        this.alter = alter
        this.name = name
        type(this).__counter += 1

    @staticmethod
    def anzahlMenschen():
        print(Mensch.__counter)
        return Mensch.__counter

    def sayHi(this):    
        print("Hi") 

    def __del__(this):                                      #Destruktor
        type(this).__counter -= 1

Mikko = Mensch()
Mikko.sayHi()
Mikko.anzahlMenschen()                              #möglich mit Mikko, da anzahlMenschen eine staticmethod ist
del Mikko
Mensch.anzahlMenschen()

# Usefulness of Classmethods

class Pet:
    _class_info = "Hasutiere"

    @classmethod                                        
    def about(cls):
        print("Diese Klasse ist über " + cls._class_info + "!")   
    

class Dog(Pet):                                             # Dog erbt von Pet
    _class_info = "Menschens besten Freund"

class Cat(Pet):
    _class_info = "alle Katzenarten"

Pet.about()
Dog.about()
Cat.about()


        
