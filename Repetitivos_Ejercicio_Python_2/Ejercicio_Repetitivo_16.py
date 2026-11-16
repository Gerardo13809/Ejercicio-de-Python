# Introducir mujeres y hombres

contador_h = 0;
contador_m = 0;
acumulador_h = 0;
acumulador_m = 0;

edad = int(input("Introduce tu edad: "));

while edad > 0:

    sexo = input("Introduce tu sexo (H o M): ").upper();

    if sexo == "H":
        contador_h += 1;
        acumulador_h += edad;

    elif sexo == "M":
        contador_m += 1;
        acumulador_m += edad;

    edad = int(input("Introduce tu edad: "));

if contador_h > 0:
    media_h = acumulador_h / contador_h;
    print(f"Se han introducido {contador_h} hombres y la media de edad es de {media_h} años.");
else:
    print("No se han introducido hombres.");

if contador_m > 0:
    media_m = acumulador_m / contador_m;
    print(f"Se han introducido {contador_m} mujeres y la media de edad es de {media_m} años.");
else:
    print("No se han introducido mujeres.");