#Visualizar suspensos y aprovados

aprovados = 0;
suspensos = 0;

repeteiciones = int(input("Introduce las veces que se repetira el programa: "));

while repeteiciones != 0:
    nota = int(input("Introduce un notita: "));

    if nota >= 5:
        aprovados += 1;

    else:
        suspensos += 1;

    repeteiciones -= 1;

print("Hay",aprovados, "aprovados");
print("Hay",suspensos, "suspensos");