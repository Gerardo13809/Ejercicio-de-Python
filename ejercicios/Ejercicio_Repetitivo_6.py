#Visualizar el mayor

mayor = 0;

repeteiciones = int(input("Introduce las veces que se repetira el programa: "));

while repeteiciones != 0:
    numero = int(input("Introduce un numerito: "));

    if numero > mayor:
        mayor = numero;

    repeteiciones -= 1;

print("El numero maximo es",mayor, );