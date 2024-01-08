# Descripció del Codi

Aquest programa en Python que realitza dues funcions diferents. Cada funció té la seva pròpia estructura llegible.

## Potència

La primera funció calcula la potència d'un nombre, donat una base (a) i un exponent (b). La funció `calcular_potencia` és responsable d'aquesta tasca i és modular per ser reutilitzada en altres parts del codi.

```python
def calcular_potencia(a, b):
    """
    Aquesta funció pren dos paràmetres, 'a' i 'b', i retorna el resultat de calcular 'a' elevat a la potència 'b'.
    Utilitza un bucle for per multiplicar 'a' 'b' vegades.
    """
    resultat = 1
    for _ in range(b):
        resultat *= a
    return resultat
