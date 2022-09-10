import random
board_list=[1,2,3,4,5,6,7,8,9]
list=[1,2,3,4,5,6,7,8,9]
#remove 5
list.remove(5)
#display board
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console."
    global board_list
    global list
    board_list[4]="X"
    #top
    print("+-------"*board+"+")
    print("|       "*board+"|")
    for num in range(0,3):
            print("|   "+str(board_list[num])+"   ",end="")
    print("|")
    print("|       "*board+"|")
    print("+-------"*board+"+")
    #mid
    print("|       "*board+"|")
    for num in range(3,6):
            print("|   "+str(board_list[num])+"   ",end="")
    print("|")
    print("|       "*board+"|")
    print("+-------"*board+"+")
    #down
    print("|       "*board+"|")
    for num in range(6,9):
            print("|   "+str(board_list[num])+"   ",end="")
    print("|")
    print("|       "*board+"|")
    print("+-------"*board+"+")
    return

def victory_for(board, sign):
    # check rows
    if board_list[0] == sign and board_list[0] == board_list[1] and board_list[1]==board_list[2] or board_list[3] == sign and board_list[3] == board_list[4] and board_list[4]==board_list[5] or board_list[6] == sign and board_list[6] == board_list[7] and board_list[7]==board_list[8]:
        return sign

    # check columns
    if board_list[0] == sign and board_list[0] == board_list[3] and board_list[3]==board_list[6] or board_list[1] == sign and board_list[1] == board_list[4] and board_list[4]==board_list[7] or board_list[2] == sign and board_list[2] == board_list[5] and board_list[5]==board_list[8]:
        return sign
    
    # check diagonals
    if board_list[0] == sign and board_list[0] == board_list[4] and board_list[4] == board_list[8] or \
        board_list[2] == sign and board_list[2] == board_list[4] and board_list[4] == board_list[6]:
        return sign
    

    return None
    
def enter_move(board):
    print("computer move:"+str(5))
    display_board(3)
    winner=[]
    while len(list)>0:
        board=int(input("your move (1-9):"))
    #your move
        
        #checking board in list
        if board in list:
            #giving sign for the value in a list and displaying board
            board_list[board-1]="O"
            sign="O"
            display_board(3)
            list.remove(board)
            #checking if won and printing won
            won=victory_for(board,sign)
            winner.append(won)
            if sign in winner:
                print("You won")
                break
            
        
    #comp move
            #giving board vlue using the new changed list and using random
            #giving sign for the value in a list and displaying board
            board=random.choice(list)
            board_list[board-1]="X"
            sign="X"
            print("computer move:"+str(board))
            display_board(3)
            victory_for(board, sign)
            list.remove(board)
            #checking if won and printing won
            won=victory_for(board,sign)
            winner.append(won)
            if sign in winner:
                print("computer won")
                break
            
            if sign not in winner and len(winner)>7:
                print("Its Tie")
            
                
           
        else:
            print("already occupied or number exceed")

def play_game():
    print("""=================================================
                    ***TIC TAC TOE***
=================================================""")
    print(" ")
    start_end = int(input("type " + str(0)+ " to start and "+str(1)+" to end the game :"))
   
    if start_end==0:
        print(" ")
        print("Computer sign:- X ")
        print("Your sign:- O ")
        print(" ")
        enter_move(3)
    elif start_end==1:
        return
    else:
        print("check your input")

play_game()
