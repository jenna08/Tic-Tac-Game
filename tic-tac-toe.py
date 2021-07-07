from random import randrange

def display_board(board):
    for i in range(3):
        print("+-------"*3, end="+\n")

        print("|       "*3, end="|\n")
        print("|  ", board[i][0], "  |  " , board[i][1], "  |  ", board[i][2], "  |")
        print("|       "*3, end="|\n")    

    print("+-------"*3, end="+\n")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board, player, x_move=''):
    if x_move != '':
        your_move = (x_move)
    else:    
        your_move = int(input("Enter your move:"))

    if your_move>0 and your_move<10:
        x = position_dict[your_move].split(",")
        row = int(x[0])
        col = int(x[1])
    
        if [row, col] in free_fields:
            board[row][col] = player
        else:
            return False
    else:
        return False
    
    return True        
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    global free_fields 
    free_fields = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free_fields.append([i,j])

    print(free_fields)
     # The function browses the board and builds a list of all the free squares; 
     # the list consists of tuples, while each tuple is a pair of row and column numbers.

def check_col(sign, col):
    for i in range(0,3):
        if board[i][col] != sign:
            return False
    return True    

def check_row(sign, row):
    for i in range(0,3):
       if board[row][i] != sign:
            return False
    return True  

def check_diagonal(sign, row, col):
    if row==col:
        if row!=1:
            if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == sign):
                #print("1","row,col->",row,col)
                return True
        else:
            if board[0][0] == board[1][1] == board[2][2] == sign:
                #print("2","row,col->",row,col)
                for m in range(0,3):
                    for n in range(2,-1,1):
                        #print(m,n)
                        if board[m][n] != sign:
                            #print("3","row,col->",row,col)
                            return False
            else:
                #print("4","row,col->",row,col)
                return False
    else:
        for m in range(0,3):
            for n in range(2,-1,1):
                #print("m,n->",m,n)
                if board[m][n] != sign:
                    return False
    #return True    
        
def victory_for(board, sign):

    for r in range(0,3):
        for c in range(0,3):
            if board[r][c] == sign:
                row_num = r
                col_num = c
                if check_col(sign, col_num):
                    print("Player", sign, "wins-col")
                    return True
                
                if check_row(sign, row_num):
                    print("Player", sign, "wins-row")
                    return True

                temp = check_diagonal(sign, row_num, col_num)
                if r==c or r+c==2:
                    if check_diagonal(sign, row_num, col_num):
                        #print("diag result-", temp, row_num, col_num)    
                        print("Player", sign, "wins-diag")
                        return True
    return False   
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    return None
    # The function draws the computer's move and updates the board.

global position_dict
position_dict = {
                    1:"0,0", 2:"0,1", 3:"0,2",
                    4:"1,0", 5:"1,1", 6:"1,2",
                    7:"2,0", 8:"2,1", 9:"2,2"
                }
#print(position_dict)
userX = 'X'
userO = 'O'

global board
board = [
           [1,2,3],
           [4,5,6],
           [7,8,9]
        ];

board[1][1] = userX
display_board(board)

##for test in board:
##    k=1
##    print(k,"->", test)
##    for test_2 in test:
##        t=1
##        print(t,"->", test_2)
##        t+=1
##    k+=1

for p in range(1,9):
    player = 'X'
    make_list_of_free_fields(board)
    print("p->",p)

       
    if p%2 != 0:
        player = 'O'
        print("player-", player)
        
        while (not enter_move(board, userO)):
            enter_move(board, userO)
        display_board(board)
        
    else:
        player = 'X'
        print("player-", player)
        move_for_X = randrange(1,10)

        while( not enter_move(board, userX, move_for_X) ):   
            move_for_X = randrange(1,10)
        display_board(board)

    if p>4:
        result = victory_for(board, player)
        if result:
            break
   
    if p==8:
        print("Its a Tie")

