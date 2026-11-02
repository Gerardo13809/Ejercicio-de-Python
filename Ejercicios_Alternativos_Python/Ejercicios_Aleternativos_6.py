#Hace una ecuacion de segundo grado

import math

a= int(input("Introduce el valorcito a: "));
b= int(input("Introduce el valorcito b: "));
c= int(input("Introduce el valorcito c: "));

d= b**2 - 4 * a * c;

if d >= 0:

    x1= (-b + math.sqrt(d)) / (2 * a);
    x2= (-b - math.sqrt(d)) / (2 * a);

    print("El resultado de la primera ecuacion es", x1);
    print("El resultado de la segunda ecuacion es", x2);

else:

    print("No hay raices reales");
