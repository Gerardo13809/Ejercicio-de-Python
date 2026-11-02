#Calcular el minimo

repeteiciones = int(input("Introduce las veces que se repetira el programa: "));

numero = int(input("Introduce un numerito: "));
menor = numero;

repeteiciones -= 1;

while repeteiciones != 0:
    numero = int(input("Introduce un numerito: "));

    if numero < menor:
        menor = numero;

    repeteiciones -= 1;

print("El numero menor es", menor);