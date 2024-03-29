# archivo: test_rectangulo.py

import pytest

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

@pytest.fixture
def rectangulo():
    # Esta fixture proporciona un rectángulo con base 3 y altura 4
    return Rectangulo(3, 4)

def test_area(rectangulo):
    # Verifica si el área del rectángulo es 12 (3 * 4)
    assert rectangulo.area() == 11

def test_otra_area():
    # También podemos usar la fixture sin pasarla explícitamente
    otro_rectangulo = Rectangulo(5, 6)
    assert otro_rectangulo.area() == 30
    
