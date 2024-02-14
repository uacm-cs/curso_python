
def f_cuadratica(x):
    return x*x

def calcula_suma(x, y):
    return x+y

class Animal:
    def __init__(self, name):
        self.name = name
    
    @property
    def nombre(self):
        return self.name
    
    @nombre.setter
    def nombre(self, name):
        self.name = name

