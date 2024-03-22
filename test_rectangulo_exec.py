import pytest
from rectangulo_exec import calcular_area_rectangulo, RectanguloException

def test_calcula_area_rectangulo():
    # Prueba para calcular el área de un rectángulo con base y altura positivas
    assert calcular_area_rectangulo(5, 4) == 20

def test_calcula_area_rectangulo_base_cero():
    # Prueba para verificar que se genere una excepción cuando la base es cero
    with pytest.raises(RectanguloException):
        calcular_area_rectangulo(0, 4)

def test_calcula_area_rectangulo_base_negativa():
    # Prueba para verificar que se genere una excepción cuando la base es negativa
    with pytest.raises(RectanguloException) as error:
        calcular_area_rectangulo(-5, 4)

    # Además de probar que se genere una excepción cuando la base es negativa, prueba que el mensaje sea como el esperado (expected_msj). 
    print(error)    
    expected_msj = 'La base y la altura deben ser valores positivos.'
    assert str(error.value) == expected_msj
    
