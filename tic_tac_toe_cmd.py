import time
from colorama import init
init()
from colorama import Fore

#define the x\o table by list
move_list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
learn_list=['1','2','3','4','5','6','7','8','9']


#clean screen
def clean_scr():
    print('\n'*20)


#function for print all the table
def print_on_screen(control_list):
    counter=0
    for i in range (13):
        x=0
        if i ==0:
            print('-'*13)
        elif i in (4,8,12):
            print(Fore.BLUE + '-'*13)
            counter+=3
        else:
            print_rows(control_list,i,counter)


#function that print only the rows
def print_rows(control_list,col,counter):
    if col % 2 == 0 and counter != 9:
        print(Fore.BLUE + f'| {control_list[counter]} | {control_list[counter+1]} | {control_list[counter+2]} |')
        counter += 3
    else:
        print(Fore.BLUE + f'|   |   |   |')


#function that enter the symbol to move list
def enter_symbol(number,symbol):
    global move_list
    if number<1 or number>9:
        print("Error!!! enter number between 1 to 9")
        return False
    if space_is_free(number):
        move_list[number-1]=symbol.upper()
        return True
    else:
        print(number)
        print("Error!!!! you cant choose this position")
        return False


#function that check the rows
def check_row(game_table):
    row1=''.join(set(game_table[0:3]))
    row2=''.join(set(game_table[3:6]))
    row3=''.join(set(game_table[6:9]))
    if row1=='X' or row2 =='X' or row3=='X':
        return 'X'
    elif row1=='O' or row2=='O' or row3=='O':
        return 'O'
    return None


#functoin that check the columns
def check_column(game_table):
    column1=''.join(set(game_table[0::3]))
    column2=''.join(set(game_table[1::3]))
    column3=''.join(set(game_table[2::3]))
    if column1=='X' or column2 =='X' or column3=='X':
        return 'X'
    elif column1=='O' or column2=='O' or column3=='O':
        return 'O'
    return None


#function that check the slants
def check_slant(game_table):
    slant1=''.join(set(game_table[0::4]))
    slant2=''.join((set(game_table[2:8:2])))
    if slant1=='X' or slant2=='X':
        return 'X'
    elif slant1=='O' or slant2=='O':
        return 'O'
    return None


#function that check if someone win
def check_win(game_table):
    row=check_row(game_table)
    column=check_column(game_table)
    slant=check_slant(game_table)
    if row!=None:
        return row
    elif column!=None:
        return column
    elif slant!=None:
        return slant
    return None


#function that check if the place is free
def space_is_free(pos):
    return move_list[pos-1]==' '


#function that check if the board is full
def board_full():
    return ' ' not in move_list

#general function for player move
def player_move(symbol,counter):
    player_move = int(input(f'enter where you want to put the {symbol}'))
    check = enter_symbol(player_move, symbol)
    while check == False:
        player_move = int(input(f'enter where you want to put the {symbol}'))
        check = enter_symbol(player_move, symbol)
    clean_scr()
    print_on_screen(move_list)
    player_one_win = check_win(move_list)
    if player_one_win == symbol:
        print(f'player {symbol} is the winner it took : {counter} turns')
        return symbol
    return None

#function for choosing symbol
def choose_symbol():
    player_one_symbol=None
    player_two_symbol = None
    while player_one_symbol != 'X' and player_one_symbol != 'O':
        player_one_symbol=input('choose your symbol :X or O the one with X is the first player').upper()
        print(player_one_symbol)
    if player_one_symbol=='X':
        player_two_symbol='O'
    elif player_one_symbol=='O':
        player_two_symbol='X'
    return (player_one_symbol,player_two_symbol)

#the main function for 2 players
def two_players():
    clean_scr()
    player_one_symbol,player_two_symbol=choose_symbol()
    print_on_screen(move_list)
    i=0
    while not (board_full()):
        i += 1
        turn=None
        turn=player_move(player_one_symbol,i)
        if ' ' not in move_list or turn!=None:
            break
        i+=1
        turn=player_move(player_two_symbol, i)
        if ' ' not in move_list or turn!=None:
            break
    if(check_win(move_list) == None):
        print('its a tie !!!')

###################

#the ai algorithem
def computer_move(cp_sign,player_sign):
    possible_moves = list(map(lambda x:x+1,[x for x in range(len(move_list)) if move_list[x] == ' ']))
    print(possible_moves)
    move=0
    for letter in [cp_sign,player_sign]:
        for i in possible_moves:
            learn_list=move_list[:]
            learn_list[i-1]=letter
            if check_win(learn_list):
                move=i
                return move
    corner_open=[]
    for i in possible_moves:
        if i in [0,2,6,8]:
            corner_open.append(i)
    if len(corner_open)>0:
        move=select_random(corner_open)
        return move
    if 4 in possible_moves:
        move=4
        return move
    edge_open=[]
    for i in possible_moves:
        if i in [1,3,5,7]:
            edge_open.append(i)
    if len(edge_open)>0:
        move=select_random(corner_open)

    return move

#choose position randomly
def select_random(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]

#the main function for player and computer
def vs_computer():
    clean_scr()
    player_symbol,computer_symbol=choose_symbol()
    checker=None
    if player_symbol == 'X':
        checker=0
    elif player_symbol == 'O':
        checker=1
    i=0
    while not (board_full()):
        i += 1
        turn = None
        if checker == 0:
            turn = player_move(player_symbol, i)
        if checker == 1:
            move = computer_move(computer_symbol, player_symbol)
            enter_symbol(move,computer_symbol)
            print_on_screen(move_list)
            turn=check_win(move_list)
        if turn==computer_symbol:
            print("the computer WINS !!!!")
        if ' ' not in move_list or turn != None:
            break
        i += 1
        if checker == 1:
            turn = player_move(player_symbol, i)
        if checker == 0:
            move = computer_move(computer_symbol, player_symbol)
            enter_symbol(move,computer_symbol)
            turn=check_win(move_list)
            print_on_screen(move_list)
        if turn==computer_symbol:
            print("the computer WINS !!!!")
        if ' ' not in move_list or turn != None:
            break
    if (check_win(move_list) == None):
        print('its a tie !!!')

#the start explain of the game + choosing game
def start_tictactoe_game():
    print('Hello this is tic tac toe game : below you will see the screen we will play with : ')
    print_on_screen(move_list)
    time.sleep(3)
    clean_scr()
    print('now you will choose your moves with the number : 1-9 ,see the next table : ')
    time.sleep(1)
    print_on_screen(learn_list)
    time.sleep(3)
    answer=input('so are you ready to play ? press yes or no')
    if(answer.lower()=='yes'):
        decision = input('you want to play 2 friends ? or computer ? Press f for friend or c for computer').lower()
        if(decision.lower()=='f'):
            two_players()
        else:
            vs_computer()

    else:
        print('Goodbye')
        exit()

start_tictactoe_game()
