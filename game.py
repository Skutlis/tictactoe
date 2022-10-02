
board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

def printBoard():
    printB = "   1 2 3 \n"
    printB += "  ------- \n"
    printB += "A |" + "|".join(board[0]) + "| \n"
    printB += "  ------- \n"
    printB += "B |" + "|".join(board[1]) + "| \n"
    printB += "  ------- \n"
    printB += "C |" + "|".join(board[2]) + "| \n"
    printB += "  ------- \n"
    print(printB)



def put(position: str, gamePiece: str):
    if (not len(position) == 2):
        return False

    letter = position[0]
    number = position[1]
    pos1 = 1
    pos2 = 1
    if (letter == "A"):
        pos1 = 0

    elif (letter == "B"):
        pos1 = 1

    elif (letter == "C"):
        pos1 = 2
    if (number == "1"):
        pos2 = 0
    elif (number == "2"):
        pos2 = 1
    elif (number == "3"):
        pos2 = 2
    if board[pos1][pos2] == " ":
        board[pos1][pos2] = gamePiece
    return True
    
def gameDone():
    win, piece = hWin()
    if win:
        return piece
    win, piece = vWin()
    if win:
        return piece
    win, piece = dWin()
    if win:
        return piece
    return " "

def hWin ():
    for row in board:
        piece = " "
        for cell in row:
            if cell == " ":
                break
            if piece == " ":
                piece = cell
            elif piece != cell:
                break
        return True, piece #win vist vi kommmer gjennom hele raden
    return False, " "  #ingen win dersom om vi kommer hit

def vWin ():
    for i in range(3):
        piece = " "
        for j in range(3):
            cell = board[j][i]
            if cell == " ":
                break
            if piece == " ":
                piece = cell
            elif piece != cell:
                break
        return True, piece #win vist vi kommmer gjennom hele raden
    return False, " "  #ingen win dersom om vi kommer hit

def dWin ():
    d1 = board[0][0]
    if board [0][0] == board [1][1] and board [0][0] == board[2][2] and board [0][0] != " ":
        return True, board[0][0]
    if board [0][2] == board [1][1] and board [0][0] == board[2][0] and board [0][2] != " ":
        return True, board[0][2]
    return False, " "

p1 = "X"
p2 = "O"
turn = p1            
isDone = False
while not isDone:
    pos = input(f"{turn}'s turn. Pick a position: ")
    if not put(pos, turn):
        print("Error, not valid position. Pick again")
        continue
    winPiece = gameDone()
    if winPiece != " ":
        break
    if turn == p1:
        turn =p2
    elif turn == p2:
        turn = p1


print(f"The winner is {winPiece}")


            


            


    

            

