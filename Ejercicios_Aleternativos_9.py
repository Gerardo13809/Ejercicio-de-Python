#Hacer calculo de área de una circunferencia de longitud de circunferencia

import math

letra= input("Introduce A o L: ").lower();
radio= float(input("Introduce el radio de la circunferencia: "));

if letra == "a":
    area= math.pi * radio**2;

    print("El area de la circunferencia es", area);

elif letra == "l":
    area= 2 * math.pi * radio;

    print("La longitud de la circunferencia es", area);

else:

    print("Error no has puesto ni A ni L");