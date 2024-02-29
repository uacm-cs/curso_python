# en el archivo test_calcular.py

import pytest

# Definir la función que queremos probar
def calcular(a, b):
    return a * b

# Definir una fixture para proporcionar datos de prueba
@pytest.fixture
def input_values():
    a = 5
    b = 3
    return a, b

# Definir el caso de prueba que utiliza la fixture
def test_calcular(input_values):
    a, b = input_values
    result = calcular(a, b)
    assert result == 15  # Verificar que el resultado es el esperado