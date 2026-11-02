#Calcualar la raiz cuadrada
import math

numero = int(input("Introduce un numerito para su raiz: "));

while numero < 0:

    numero = int(input("Introduce un numerito para su raiz: "));
    
print(math.sqrt(numero));