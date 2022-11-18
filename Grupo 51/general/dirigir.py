import random
ejercicios=['56, Pág 91, 31','57, Pág 94, 38',
            '59, Pág 97, 18','62, Pág 102, 14',
            '39, Pág 309, 21','40, Pág 310, 16',
            '41, Pág 312, 24','42, Pág 314, 13',
            '43, Pág 317, 25','44, Pág 319, 21',
            '46, Pág 323, 19','51, Pág 330, 14',
            '53, Pág 336, 22','61, Pág 356, 9',
            '62, Pág 359, 13','63, Pág 361, 15']
miembros=(['Jorge','Díaz','Anderson','Dayron','Motta'])
random.shuffle(miembros)
resultado=""
def tocaEjercicio(x):
    toca=random.sample(ejercicios,k=x)
    for i in toca:
        if i in ejercicios:
            ejercicios.remove(i)
        else:
            print('value is not in the list')
    return toca
for index, i in enumerate(miembros):
    if (index==len(miembros)-1):
        resultado+=f"""
        {i}, hace los siguientes ejercicios:
                        {tocaEjercicio(4)}\n"""
    else:
        resultado+=f"""
        {i}, hace los siguientes ejercicios:
                        {tocaEjercicio(3)}\n"""
print(resultado)