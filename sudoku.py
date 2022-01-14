board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]
def show_board(puzzle): # for printing the puzzle
    for i in range(9):
        if i%3 == 0 and i != 0:
            print("_____________________")
        for j in range(9):
            if j%3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(puzzle[i][j])
            else:
                print(puzzle[i][j],end=" ")

def find_empty(puzzle): # for finding the empty element in the puzzle
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return (i,j)  # row and column
    return False

def valid(puzzle,number,position):
    for i in range(9): #for checking any repeat number in that row
        if puzzle[position[0]][i] == number and position[0] != i:
            return False
    for i in range(9): # for checking any repeat number in that column
        if puzzle[i][position[1]] == number and position[1] != i:
            return False
    # for checking any repeat number in the block of 3x3
    row_start = (position[0]//3)*3
    col_start = (position[1]//3)*3
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if puzzle[i][j] == number and (i,j) != position:
                return False
    return True

def solve(puzzle):
    find = find_empty(puzzle)
    if not find:
        return True
    else:
        row,col = find
    for number in range(1,10):
        if valid(puzzle,number,(row,col)):
            puzzle[row][col] = number
            if solve(puzzle):
                return True
            puzzle[row][col] = 0

    return False

print(show_board(board))
solve(board)
print(show_board(board))

