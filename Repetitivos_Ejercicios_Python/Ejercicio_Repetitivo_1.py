#1. Introducir un número entero y realizar su tabla de multiplicar. Formato de salida
numero= int(input("Introduce un numerito: "));

for i in range(1,11):
    print(f"{numero}*{i}={numero*i}");