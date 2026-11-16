# Sucesión de Fibonacci

n = int(input("¿Cuántos números quieres mostrar?: "));

a = 1;
b = 1;

for i in range(n):
    print(a);

    siguiente = a + b;
    a = b;
    b = siguiente;