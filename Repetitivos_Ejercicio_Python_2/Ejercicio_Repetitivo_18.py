# Notas de Lengua

acumulador_grupo = 0;
contador = 0;

numero_lista = int(input("Introduce el número de lista: "));

while numero_lista != 0:

    nota1 = int(input("Introduce la nota de la 1ª evaluación: "));
    nota2 = int(input("Introduce la nota de la 2ª evaluación: "));
    nota3 = int(input("Introduce la nota de la 3ª evaluación: "));

    media = (nota1 + nota2 + nota3) / 3;

    print(f"El alumno con número de lista {numero_lista} tiene un {media} de nota media.");

    acumulador_grupo = acumulador_grupo + media;
    contador += 1;

    numero_lista = int(input("Introduce el número de lista: "));

if contador > 0:
    media_grupo = acumulador_grupo / contador;
    print(f"La media del grupo en lengua es {media_grupo}.");
else:
    print("No se han introducido alumnos.");
