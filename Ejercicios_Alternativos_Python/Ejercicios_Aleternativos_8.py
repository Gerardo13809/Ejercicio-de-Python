#Ver si es equilatero, isosceles o escaleno

numero1 = int(input("Introduce un ladito: "));
numero2 = int(input("Introduce otro laditos: "));
numero3 = int(input("Introduce otro ladito más: "));

if numero1 == numero2 == numero3:

    print("El triangulo es Equilatero");

elif numero1 == numero2 or numero2 == numero3 or numero3 == numero1:

    print("El triangulo es Isosceles");

else:

    print("El triangulo es Escaleno");