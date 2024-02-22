
# contenido test_ejemplo2.py

def func(x):
    return x + 1


def sumatoria(lista):
    s = 0
    for l in lista:
        s +=l
    return s

def test_respuesta():
    assert func(3) == 5


def test_sumatoria():
    assert sumatoria([1,2,3]) == 6

def test_sumatoria_par(lista, resultado):
    assert sumatoria(lista) == resultado
    