def calcular_potencia(a, b):
    resultado = 1
    for _ in range(b):
        resultado *= a
    return resultado

    ''' Aquesta funció pren dos paràmetres, 'a' i 'b', i retorna el resultat de calcular 'a' elevat a la potència 'b'.
    Utilitza un bucle for per multiplicar 'a' 'b' vegades. '''



def main():
    
    contador = 0

    while contador != 6:

        contador += 1

        entrada = str(input())
        a, b = entrada.split(" ")
        a = int(a)
        b = int(b)

        resultado = calcular_potencia(a, b)

        print(resultado)


    ''' Funció principal que coordina l'execució del programa.
    Utilitza un bucle while per iterar fins que el contador arribi a 6.
    A cada iteració, llegeix una entrada de l'usuari, la processa i imprimeix el resultat. '''


main()

help(calcular_potencia)
help(main)