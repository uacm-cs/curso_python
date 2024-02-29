# contenido test_clase_ejemplo1.py

import pytest 

class TestEjemplo1:
    def test_ejem1(self):
        x = "hola"
        assert "h" in x 

    def test_ejem2(self):
        x = "hello"
        assert isinstance(x, str) # revisa si el objeto es instancia de el tipo de dato str (string)

    def test_ejem3(self):
        x = "hello"
        assert isinstance(x, int) # revisa si el objeto es instancia de el tipo de dato str (string)