import cabezote
cabezote.mensaje()


def contar_vocales(frase):
    vocales = 'aeiouAEIOU'  # Se ponen tanto minusculas como minusculas
    return len([c for c in frase if c in vocales])


def contar_mayusculas(frase):
    # ciclo pregunta letra por letra si es mayuscula
    return len([l for l in frase if l.isupper()])


def contar_menor_tres(frase):
    # Fraccionamos la frase
    # Indicamos que solo guarde las que sean menores a 3
    return len([l for l in frase.split() if len(l) < 3])


frase = input('Ingrese una frase: ')

print(f'Cantidad de palabras con menos de tres letras: {contar_menor_tres(frase)}')
print(f'Cantidad de mayúsculas: {contar_mayusculas(frase)}')
print(f'Cantidad de vocales: {contar_vocales(frase)}')
