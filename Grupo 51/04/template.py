import os
import time
from tqdm import tqdm
# Funcion para limpiar pantalla dependiendo del sistema operativo
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
# Una barra de progreso
def bar():
    clear()
    print('-------- Procesando datos de las lluvias --------')
    for i in tqdm(range(100)):
        time.sleep(0.01)
    clear()