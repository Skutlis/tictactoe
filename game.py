

board = [["", "", ""],
        ["", "", ""],
        ["", "", ""]]

def printBoard(board: list):
    pass



def put(position: str, gamePiece: str):
    if (not len(position) == 2):
        return

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
    if board[pos1][pos2] == "":
        board[pos1][pos2] = gamePiece
    

    

            

