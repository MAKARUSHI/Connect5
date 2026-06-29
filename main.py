def initializeBoard(gameRatio):
    board = []
    for i in range(0, gameRatio["row"] * gameRatio["column"]):
        board.append(" - ")
    return board

# TODO: Remove the Func suffix where it is not necessary
def getInputPosition(sign, board, gameRatio):
    print(sign + " is playing")
    print("Type untaken position (column)")
    positionInput = input("Input: ")
    tempIndex = checkInput(positionInput, board, gameRatio)
    if tempIndex is None:
        return None
    return tempIndex

def checkInput(positionInput, board, gameRatio):
    pos = positionInput
    pos.strip()
    if not pos.isdigit():
        return None
    pos = int(pos) - 1

    if pos < gameRatio["column"] and pos >= 0:
        for i in range(gameRatio["row"] - 1, -1, -1):
            tempIndex = i * gameRatio["column"] + pos
            # TODO: Consider using just "-" to store the state
            if board[tempIndex] == " - ":
                return tempIndex
    print("Type valid position max:" + str(gameRatio["column"]))
    return None

def changePlayerFunc(signs, signInt):
    signInt += 1
    return signs[signInt % len(signs)], signInt

def addPosition(board, currentSign, inputPosition):
    board[inputPosition] = currentSign
    return board

def displayBoard(board, gameRatio):
    for i in range(gameRatio["row"]):
        for j in range(gameRatio["column"]):
            print(board[i * gameRatio["column"] + j], end="")
        print("")
    print("---"*gameRatio["column"])
    for i in range(1, gameRatio["column"] + 1):
        print(f" {i} ", end="")
    print("")

def findRowValidIndex(position, step, finish):
    positionMinus = 0
    while (position + 1 + positionMinus * step) % gameRatio["column"] != finish:
        if positionMinus == 4:
            break
        positionMinus += 1
    return positionMinus

def findColValidIndex(rowIndex, step, finish):
    positionMinus = 0
    while True:
        if positionMinus == 4:
            break
        if rowIndex + positionMinus * step == finish:
            break
        positionMinus += 1
    return positionMinus
    
def rowColCheck(board, currentSign, startIndex, endIndex, step, type):
    rowCounter = 0
    for i in range(startIndex, endIndex + 1, step):
        if board[i] == currentSign:
            rowCounter += 1
            print("h")
            if rowCounter == 5:
                print(currentSign , "wins with a" , type , "line")
                break
        if board[i] != currentSign:
            rowCounter = 0

def checkWin(position, board, gameRatio, currentSign):
    rowIndex = position // gameRatio["column"]
    colIndex = position % gameRatio["column"]

    # number of posible turns back and fourth in row
    rowValidIndexMinusStart = findRowValidIndex(position, -1, 1)
    rowValidIndexMinusEnd = findRowValidIndex(position, 1, 0)

    # position minus posible moves (min and max positions) row
    rowStartIndex = position - rowValidIndexMinusStart
    rowEndIndex = position + rowValidIndexMinusEnd

    # number of posible turns back and fourth in column
    colValidIndexMinusStart = findColValidIndex(rowIndex, -1, 0)
    colValidIndexMinusEnd = findColValidIndex(rowIndex, 1, gameRatio["row"] - 1)
    
    # position minus posible moves (min and max positions) column
    colStartIndex = position - gameRatio["column"] * colValidIndexMinusStart
    colEndIndex = position + gameRatio["column"] * colValidIndexMinusEnd
    
    print("start row", rowStartIndex, "end row", rowEndIndex)
    print("start col", colStartIndex, "end col", colEndIndex)

    rowColCheck(board, currentSign, rowStartIndex, rowEndIndex, 1, "row")
    rowColCheck(board, currentSign, colStartIndex, colEndIndex, gameRatio["column"], "column")

    counter = 1
    correctCounter = 0
    minTemp = min(rowValidIndexMinusStart, colValidIndexMinusStart)
    pos = position - minTemp - minTemp * gameRatio["column"]
    while pos >= 0 and pos < gameRatio["column"] * gameRatio["row"]:
        if board[pos] == currentSign:
            correctCounter += 1
            if correctCounter == 5:
                print(currentSign , "wins with a diagonal to right")
                break
        else:
            correctCounter = 0
       
        pos = pos + 1 + 1 * gameRatio["column"]
        counter += 1
    
    counter = 1
    correctCounter = 0
    minTemp = min(rowValidIndexMinusEnd, colValidIndexMinusStart)
    pos = position + minTemp - minTemp * gameRatio["column"]
    while pos >= 0 and pos < gameRatio["column"] * gameRatio["row"]:
        if board[pos] == currentSign:
            correctCounter += 1
            if correctCounter == 5:
                print(currentSign , "wins with a diagonal to left")
                break
        else:
            correctCounter = 0
       
        print(pos)
        pos = pos - 1 + 1 * gameRatio["column"]
        counter += 1

  

gameRatio = {"row":7,"column":7}
endGame = False
signs = [" x ", " o "]
signInt = -1
inputPosition = None

board = initializeBoard(gameRatio)

while not endGame:
    currentSign, signInt = changePlayerFunc(signs, signInt)
    while inputPosition == None:
        inputPosition = getInputPosition(currentSign, board, gameRatio)
    addPosition(board, currentSign, inputPosition)
    checkWin(inputPosition, board, gameRatio, currentSign)
    inputPosition = None
    displayBoard(board, gameRatio)
