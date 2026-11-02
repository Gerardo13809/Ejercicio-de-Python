#Visualizar cuales son las 5 mayores
mayor = 0;

for i in range(1,6):
    edad = int(input("Introduce una edad: "));

    if edad >= 18:
        mayor += 1;

print ("Hay",mayor, "mayores de edad");