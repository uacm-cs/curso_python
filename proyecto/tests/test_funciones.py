from mi_paquete.mis_funciones import func_cuadratica, func_sumatoria

def test_func_cuadratica():
    assert func_cuadratica(3) == 9

def test_func_sumatoria():
    assert func_sumatoria([1,2,3]) == 6
