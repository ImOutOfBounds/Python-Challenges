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
    elif pos1cord[1] != pos2cord[1] :
        pass # pegar numero que falta na horizontal

    return 0


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
    

print(ticTacToeBlock(1, 7))