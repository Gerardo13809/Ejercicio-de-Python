#Calcular el positivo negativo o nulo con whilu

repeteiciones = int(input("Introduce las veces que se repetira el programa: "));

while repeteiciones != 0:
    numero = int(input("Introduce un numerito: "));

    if numero > 0:
        print("Positivo");

    elif numero < 0:
        print("Negativo");

    else:
        print("Nulo");

    repeteiciones -= 1;