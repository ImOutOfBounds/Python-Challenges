def ticTacToeBlock(pos1, pos2) -> int:
    gameMatrix = buildGame()

    for i in range(3):
        for j in range(3):
            if pos1 == gameMatrix[i][j]:
                pos1cord = (i, j)
            if pos2 == gameMatrix[i][j]:
                pos2cord = (i, j)

    if pos1cord[0] == pos2cord[0]:
        return getMissingRow(pos1cord[0], gameMatrix, pos1, pos2)
    elif pos1cord[1] == pos2cord[1]:
        return getMissingCol(pos1cord[1], gameMatrix, pos1, pos2)
    elif pos1cord[1] != pos2cord[1]:
        return getMissingVertical(pos1, pos2)

    return -1



def getMissingRow(rowNum, gameMatrix, num1, num2) -> int:
    for i in gameMatrix[rowNum]:
        if num1 != i and num2 != i:
            return i
    return 0



def getMissingCol(colNum, gameMatrix, num1, num2) -> int:
    possibleRes = []
    for i in range(3):
        for j in range(3):
            if j == colNum:
                possibleRes.append(gameMatrix[i][j])
    
    for i in possibleRes:
        if num1 != i and num2 != i:
            return i
    return 0



def getMissingVertical(num1, num2) -> int:
    if num1 != 4 and num2 != 4:
        return 4
    elif num1 == 4:
        return abs(8-num2)
    elif num2 == 4:
        return abs(8-num1)
    return 0



def buildGame() -> list[list[int]]: 
    gameMatrix = []
    k = 0

    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(k)
            k += 1
        gameMatrix.append(row)

    return gameMatrix
    


test_cases = {
    1: {"expected": 2, "p1": 0, "p2": 1}, 
    2: {"expected": 4, "p1": 0, "p2": 5},  
    3: {"expected": 5, "p1": 3, "p2": 4},  
    4: {"expected": 4, "p1": 1, "p2": 7},  
    5: {"expected": 8, "p1": 0, "p2": 4}, 
    6: {"expected": 6, "p1": 2, "p2": 4},  
    7: {"expected": 8, "p1": 2, "p2": 5},  
    8: {"expected": 5, "p1": 4, "p2": 3},  
    9: {"expected": 7, "p1": 1, "p2": 4}, 
    10: {"expected": 4, "p1": 2, "p2": 6}, 
}

for i, case in test_cases.items():
    result = ticTacToeBlock(case["p1"], case["p2"])
    print(f"Test {i}: Expected: {case['expected']} | Result: {result} | P1: {case['p1']} | P2: {case['p2']}")