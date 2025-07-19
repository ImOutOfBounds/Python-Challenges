def rearungeNumber(num) -> int:
    numList = list(str(num))


    sortedList = quickSort(numList)
    num1 = ''
    num2 = ''

    for i in range(len(sortedList)):
        num1 += sortedList[i]
        num2 += sortedList[-(i + 1)]
    
    print(num1)
    print(num2)
    return abs(int(num1) - int(num2))


def quickSort(numList) -> list[int]:
    if len(numList) <= 1:
        return numList
    
    pivotIndice = len(numList) // 2
    pivot = numList[pivotIndice]
    
    left = []
    right = []

    for i in range(len(numList)):
        if i == pivotIndice:
            pass
        elif numList[i] > pivot:
            # print(str(numList[i]) + " é maior que o pivo: " + str(pivot))
            right.append(numList[i])
        else:
            # print(str(numList[i]) + " é menor ou igual que o pivo: " + str(pivot))
            left.append(numList[i])

    return quickSort(left) + list(pivot) + quickSort(right)

print(rearungeNumber(27189873028))

