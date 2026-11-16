#Suma N

acumulador = 0;

n = int(input("Introduce un numerito: "));

for i in range(1, 1+n):
    acumulador = acumulador + (1 / i);

print(f"El resultado de la suma es {acumulador}");