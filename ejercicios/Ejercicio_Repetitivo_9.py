#Calcular medias de trimestres

acumulador = 0;
media= 0;

for i in range(1,9):
    nota = int(input("Introduce tus notas del trimestre: "));

    acumulador = acumulador + nota;
    media = acumulador / 8;

print("La media de tu trimestre es",media, );