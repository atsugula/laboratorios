array=[['carlos',12,13],['jorge',14,30],['rojo',20,23]]
iterations = len(array) - 1
test = [0 for i in range(iterations)]
posTest = 0
for i in range(iterations, 0, -1):
    for pos in array:
        if posTest == (len(pos) - 1):
            continue
        test[posTest] += pos[posTest+1]
    posTest += 1
print(test)
print(iterations)