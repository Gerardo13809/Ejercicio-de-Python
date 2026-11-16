#Notas positivas y lo que sea

acumulador = 0;
contador = 0;
media = 0;
aprovados = 0;
suspensos = 0;

notas = int(input("Introduce un numerito: "));

while notas >= 0:
    contador += 1;
    if notas >= 5:
            aprovados += 1;
    
    if notas <= 4:
            suspensos += 1;
    
    acumulador = acumulador + notas;

    notas = int(input("Introduce un numerito: "));
    
    media = acumulador / contador;

print("La media de las notas es",media, );
print("Hay",aprovados, "aprobados" );
print("Hay",suspensos, "suspensos" );