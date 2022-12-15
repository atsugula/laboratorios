import numpy
start_text = """Juan 23 4500
María 12 800
Pedro 34 8500"""
payments = []

# Ponemos los datos del enunciado
def start_file():
    file = open('empleado.txt', 'w')
    file.write(start_text)
    file.close()


def split_data():
    with open('empleado.txt', 'r') as file:
        data = [line.rstrip() for line in file]
        for text in data:
            temp = text.split(' ')
            temp.pop(0)
            payments.append([int(payment) for payment in temp])

def update_file():
    with open('empleado.txt', 'w+') as file:
        for i in range(len(payments)):
            if i == 0:
                value = numpy.prod(payments[i])
                file.write(f' Juan 23 4500 ${value}\n')
            if i == 1:
                value = numpy.prod(payments[i])
                file.write(f' María 12 800 ${value}\n')
            if i == 2:
                value = numpy.prod(payments[i])
                file.write(f' Pedro 34 8500 ${value}')

start_file()
split_data()
update_file()
print('Guardado con éxito.')