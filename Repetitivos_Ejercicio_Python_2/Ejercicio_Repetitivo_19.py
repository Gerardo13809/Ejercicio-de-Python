# Calcular capital e intereses

año_de_curso = int(input("Introduce el año de inicio: "));
capital = float(input("Introduce el capital inicial: "));
interes = float(input("Introduce el interés: "));
años = int(input("Introduce el número de años: "));

for i in range(años):

    beneficio = capital * interes / 100;
    capital_final = capital + beneficio;

    print(f"\nAño: {año_de_curso}");
    print(f"Capital a principios de año: {capital}€");
    print(f"Beneficio obtenido: {beneficio}€");
    print(f"Capital a final de año: {capital_final}€");

    capital = capital_final;
    año_de_curso += 1;
