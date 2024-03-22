import pytest

class Mi_Excepcion(Exception):
    """Excepción que se quiere personalizar"""

def func_mi_exception():
    raise Mi_Excepcion("Excepción lanzada")

def test_func_mi_exception():
    with pytest.raises(Mi_Excepcion) as execinfo:
        func_mi_exception()
    print(execinfo)
    assert str(execinfo.value) == "Excepción lanzada"