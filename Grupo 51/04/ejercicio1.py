# Iniciamos las variables a utilizar
names = []
times = []
# Pedimos los datos
def fill_name():
    name = input('Ingrese el nombre del nadador: ')
    names.append(name)
def fill_time():
    time = int(input('Ingrese el tiempo del nadador: '))
    if time in times:
        print('Rectifique ya que es muy poco probable que haya un empate.')
        fill_time()
    else:
        times.append(time)
def assign_rewards():
    print('---------- GANADORES ----------')
    cont = 0
    while cont != 3:
        temp = 0
        win = min(times)
        for i in range(len(times)):
            if win == times[i]:
                if cont == 0:
                    print(f'Oro     : {names[i]} [{times[i]}]')
                    cont += 1
                    temp = i
                elif cont == 1:
                    print(f'Plata   : {names[i]} [{times[i]}]')
                    cont += 1
                    temp = i
                elif cont == 2:
                    print(f'Bronce  : {names[i]} [{times[i]}]')
                    cont += 1
                    temp = i
        times.pop(temp)
        names.pop(temp)
        temp = 0
print("--- PRUEBA DE LOS 100 METROS ---")
for i in range(5):
    fill_name()
    fill_time()
    print()
assign_rewards()
