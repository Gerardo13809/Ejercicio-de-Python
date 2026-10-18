#Calcular la nota en insuficiente, suficiente, bien, notable, sobresaliente

nota= float(input("Introduce tu nota numerica: "));

if nota <= 4.49:

    print("Insuficiente");

elif nota < 6:

    print("Suficiente");

elif nota < 8:

    print("Bien");

elif nota < 9:

    print("Notable");

else:

    print("Sobresaliente");