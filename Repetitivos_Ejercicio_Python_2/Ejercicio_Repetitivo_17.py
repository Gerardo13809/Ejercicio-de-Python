# Notas de matemáticas

acumulador = 0;
maximo = 0;
minimo = 10;

for i in range(1, 11):

    numero_lista = int(input("Introduce el número de lista: "));
    nota = int(input("Introduce la nota: "));

    if i == 1:
        maximo = nota;
        minimo = nota;
        lista_maxima = numero_lista;
        lista_minima = numero_lista;

    if nota > maximo:
        maximo = nota;
        lista_maxima = numero_lista;

    if nota < minimo:
        minimo = nota;
        lista_minima = numero_lista;

    acumulador = acumulador + nota;
media = acumulador / 10;

print(f"La nota máxima es {maximo}, del alumno número {lista_maxima}.");
print(f"La nota mínima es {minimo}, del alumno número {lista_minima}.");
print(f"La media de la clase es {media}.");
