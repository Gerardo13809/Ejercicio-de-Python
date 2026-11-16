#Positivas y media de mayor de edad

acumulador = 0;
contador = 0;

edad = int(input("Introduce tu edad: "));

while edad >= 0:
    contador=contador + 1;
    acumulador=acumulador + edad;
    edad = int(input("Introduce tu edad: "));

media=acumulador / contador;
    
if media >= 18:
    print("Eres mayor de edad");

else:

    print("Eres menor de edad");