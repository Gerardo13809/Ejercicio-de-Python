#SuperCalculeitor

operacion= (input("Introduce entre uno de estos operados arimetico + - * / % "));

if operacion == "+":

    numero1= float(input("introduce un numerito: "));
    numero2= float(input("introduce otro numerito: "));

    suma= numero1 + numero2;

    print("El resultado de la suma es", suma);

elif operacion == "-":

    numero1= float(input("introduce un numerito: "));
    numero2= float(input("introduce otro numerito: "));

    resta= numero1 - numero2;

    print("El resultado de la resta es", resta);

elif operacion == "*":

    numero1= float(input("introduce un numerito: "));
    numero2= float(input("introduce otro numerito: "));

    multiplicacion= numero1 * numero2;

    print("El resultado de la multiplicacion es", multiplicacion);

elif operacion == "/":

    numero1= float(input("introduce un numerito: "));
    numero2= float(input("introduce otro numerito: "));

    division= numero1 / numero2;

    print("El resultado de la division es", division);

elif operacion == "%":

    numero1= float(input("introduce un numerito: "));
    numero2= float(input("introduce otro numerito: "));

    resto= numero1 % numero2;

    print("El resultado del resto es", resto);