def setBoardFunc(board, gameRatio):
    for i in range(0, gameRatio["row"] * gameRatio["column"]):
        board.append(" - ")

def inputPositionFunc(sign, board, gameRatio):
    print(sign + " is playing")
    print("Type untaken position (column)")
    positionInput = input("Input: ")
    tempIndex = checkInputFunc(positionInput, board, gameRatio)
    if tempIndex is None:
        return None
    return tempIndex

def changePlayerFunc(signs, signInt):
    signInt += 1
    if signInt == 0:
        return signs[signInt], signInt
    return signs[signInt % len(signs)], signInt

def checkInputFunc(positionInput, board, gameRatio):
    pos = positionInput
    pos.strip()
    if not pos.isdigit():
        return None
    pos = int(pos) - 1

    if pos <= gameRatio["column"] and pos >= 0:
        for i in range(gameRatio["row"] - 1, -1, -1):
            tempIndex = i * gameRatio["column"] + pos
            if board[tempIndex] == " - ":
                return tempIndex
    print("Type valid position max:" + str(gameRatio["column"]))
    return None

def addPositionFunc(board, gameRatio, currentSign, inputPosition):
    board[inputPosition] = currentSign
    return board


def displayBoardFunc(board, gameRatio):
    for i in range(gameRatio["row"]):
        for j in range(gameRatio["column"]):
            print(board[i * gameRatio["column"] + j], end="")
        print("")
    print("---"*gameRatio["column"])
    for i in range(1, gameRatio["column"] + 1):
        print(f" {i} ", end="")
    print("")

def checkWin(position, board, gameRatio, currentSign):
    rowIndex = position // gameRatio["column"]
    #print("max/min i", max(rowIndex, position - 4 * gameRatio["column"]),min(position + gameRatio["column"] * rowIndex + 1, position + 4 * gameRatio["column"] + 1))
    print("row", rowIndex)
    countStartRow = 0
    countEndRow = 0
    rowMultiplier = 1
    rowIndexStart = max(rowIndex, position - 4 * gameRatio["column"])
    rowIndexEnd = min(position + 4 * gameRatio["column"] + 1, position + gameRatio["column"] * rowIndex + 1)
    
    c = position % gameRatio["column"]
    countStartRow = min(4, c) 
    countEndRow = min(4, (gameRatio["column"] - 1) - c)

    print("position", position)
    print("start", countStartRow, "end", countEndRow)
    for i in range(rowIndexStart, rowIndexEnd, gameRatio["column"]):
        for j in range(max(i - countStartRow, i - 4), min(i + countEndRow + 1, i + 5)):
            print(j, end="")
        print("")

gameRatio = {"row":7,"column":7}
endGame = False
signs = [" x ", " o "]
signInt = -1
inputPosition = None
board = []

setBoardFunc(board, gameRatio)

while not endGame:
    currentSign, signInt = changePlayerFunc(signs, signInt)
    while inputPosition == None:
        inputPosition = inputPositionFunc(currentSign, board, gameRatio)
    addPositionFunc(board, gameRatio, currentSign, inputPosition)
    checkWin(inputPosition, board, gameRatio, currentSign)
    inputPosition = None
    displayBoardFunc(board, gameRatio)
