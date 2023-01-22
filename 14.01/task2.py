# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

board = [i for i in range(1, 10)]

def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = int(input(("Ваш ход "+ player_token+"?")))
        if player_answer >=1 and player_answer <=9:
            if str(board[player_answer-1])  not in "XO":
               board[player_answer-1] = player_token
               valid = True
            else:
                print("Эта ячейка  уже занята")
        else:
            print("Неверное значение,введите число от 1 до 9")
    
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    win = False
    counter = 0
    while not win:
        draw_board(board)
        if counter %2 == 0:
            take_input("x")
        else:
            take_input("0")

        counter+= 1
        if counter > 4:
            temp = check_win(board)
            if temp:
                win = True
                print(temp, "выиграл!")
                break
        if counter == 9:
            print("Ничья")
            break
        
draw_board(board)


    
    


        


