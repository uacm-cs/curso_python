#__all__ = ['Person']
class Persona:
    def __init__(self, name, age):
        self.__private_attribute = 'Atributo privado.'
        self.name = name
        self.age = age
    
    def public_method(self):
        return "método público"

    def __private_method(self):
        return "método pseudo-privado"
