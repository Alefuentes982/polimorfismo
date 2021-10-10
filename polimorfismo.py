class Perro():
    def hablar(self):
        print("Guau!")

class Gato():
    def hablar(self):
        print("Miau!")


def hablarMascota(animal):
    animal.hablar()

if __name__ == '__main__':
    gato =Gato()
    perro = Perro()
    hablarMascota(gato)
    hablarMascota(perro)
 

    

