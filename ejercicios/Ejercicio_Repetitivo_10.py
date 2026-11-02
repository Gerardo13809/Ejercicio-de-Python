#La Suma N-Esima

acumulador = 0;

n = int(input("Introduce un numerito para realizar la suma enesima: "));

n += 1;

for i in range(1,n):

    acumulador = acumulador + i;

print(acumulador);