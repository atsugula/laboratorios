datos = [[0 for x in range(3)] for y in range(3)]
datos[0][0] = 3
datos[0][1] = 7
datos[0][2] = 4
datos[1][0] = 9
datos[1][1] = 6
datos[1][2] = 2
datos[2][0] = 11
datos[2][1] = 5
datos[2][2] = 10

# Identificar numero primos del array


def prime():
    primos = []
    for x in range(len(datos)):
        for i in range(len(datos)):
            temp = is_prime(datos[x][i])
            if temp:
                primos.append(datos[x][i])
    primos.sort()
    return primos


def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False   
            return prime
    return prime


def is_par():
    pares = []
    for x in range(len(datos)):
        for i in range(len(datos)):
            if (datos[x][i] % 2 == 0):
                pares.append(datos[x][i])
    return pares


def is_odd():
    impares = []
    for x in range(len(datos)):
        for i in range(len(datos)):
            if (datos[x][i] % 2 != 0):
                impares.append(datos[x][i])
    return impares


print(prime())
print(is_par())
print(is_odd())
