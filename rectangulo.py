
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo"""
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser valores positivos.")
    return base * altura
