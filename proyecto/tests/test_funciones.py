from mi_paquete.mis_funciones import func_cuadratica, func_sumatoria
import pytest 

def test_func_cuadratica():
    assert func_cuadratica(3) == 9
    
    assert func_cuadratica(0.2) == pytest.approx(0.04)



def test_func_sumatoria():
    assert func_sumatoria([1,2,3]) == 6
