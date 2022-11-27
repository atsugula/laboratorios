import time

numeros = [[0.0 for x in range(2)] for y in range(3)]
for i in range(3):
    for j in range(2):
        numeros[i][j] = float(input(f"Digite numeros[{i}][{j}]: "))
for i in range(3):
    print(numeros[i])
    time.sleep(1)
print("Numero de filas: ",len(numeros))
print("Numero de columnas: ",len(numeros[0]))