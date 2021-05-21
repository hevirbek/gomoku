n = 0
while not 3 <= n:
    n = int(input("Size:"))

board = list()

for i in range(n):
    board.append([])

for x in range(n):
    for y in range(n):
        board[x].append("-")

letters = ["A", "B", "C", "D", "E", "F", "G", "H"]


# Function to display the board
def print_board(board):
    print("\t", end="")
    for i in range(n):
        print(letters[i], end="\t")
    print()
    for x in range(n):
        print(x, end="\t")
        for y in range(n):
            print(board[x][y], end="\t")
        print()


# Function to check if the first player wins
def winM(board):
    for x in range(n):
        if "T" not in board[x] and "-" not in board[x]:
            return True

    for y in range(n):
        win = True
        for x in range(n):
            if board[x][y] != "M":
                win = False
        if win:
            return True

    win = True

    for x in range(n):
        if board[x][x] != "M":
            win = False

    if win:
        return True

    win = True

    for x in range(n):
        if board[x][n-x-1] != "M":
            win = False

    if win:
        return True

    return False


# Function to check if the first player wins
def winT(board):
    for x in range(n):
        if "M" not in board[x] and "-" not in board[x]:
            return True

    for y in range(n):
        win = True
        for x in range(n):
            if board[x][y] != "T":
                win = False
        if win:
            return True

    win = True

    for x in range(n):
        if board[x][x] != "T":
            win = False

    if win:
        return True

    win = True

    for x in range(n):
        if board[x][n-x-1] != "T":
            win = False

    if win:
        return True

    return False


# Function to check if there is available spot on the board
def board_end(board):
    for x in range(n):
        if "-" in board[x]:
            return False
    return True


# Function to fills the given point on the board
# with the given letter and returns False if that spot is filled
def fill_spot(board, x, y, c):
    if board[x][y] != "-":
        return True

    board[x][y] = c


turn = 0
print_board(board)
while True:
    if turn % 2 == 0:
        point = input("First player:")
        x = int(point[0])
        y = letters.index(point[1])
        t = fill_spot(board, x, y, "M")
        if not t:
            if winM(board):
                print_board(board)
                print("First Player wins!")
                break
            turn += 1
        else:
            print("Orası dolu")
    else:
        point = input("Second player:")
        x = int(point[0])
        y = letters.index(point[1])
        print(x, y)
        t = fill_spot(board, x, y, "T")
        if not t:
            if winT(board):
                print_board(board)
                print("Second player wins!")
                break
            turn += 1
        else:
            print("Orası dolu")

    print_board(board)

    if board_end(board):
        print("Game over, no winner")
        break
