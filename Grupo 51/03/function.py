# Recursividad
x=1
d=""
def forDos(w,j):
    global x,d
    if j>1 and j<5:
        x+=(w*j)-2
        d=f"""w = {w}, j = {j}, x = {x}"""
        forDos(w,j+1)
def forUno(w):
    if w>0:
        forDos(w,2)
        forUno(w-1)
forUno(6)
print(d)