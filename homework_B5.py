#IDLE
#Попытался использовать все знания в одной задаче
#После просмотра задачи прошу написать мне в пачку для критики
#Думаю я много где ошибся в плане написания кода

def new_game(): 
    list_ = [[0]*3 for i in range(3)]
    
    for i in range(3):
        list_[i][0] = " "
        for j in range(3):
            list_[i][j] = " "
    return list_


def view_table():
    print("  0 1 2")
    for i in range(3):
        print(i, end = " ")
        for j in range(3):
            print(list_[j][i], end = " ")

        print()
    for i in range(4):
        print("-", end = " ")
    print()

#do while (⌐■_■)

def check_move(x,y):
    if 0<=x<=2 and 0<=y<=2:
        if list_[x][y] == " ":#code readability
            return False
        else:
            return True

    return True
    
def move_player(name_player, num_player):
    print(f"move {name_player}")
    x = int(input("enter x \n"))
    y = int(input("enter y \n"))
    while(check_move(x,y)):
        print("Repeat the input")
        x = int(input("enter x \n"))
        y = int(input("enter y \n"))
    
    if num_player == 1:
        list_[x][y] = "x"
    else:
        list_[x][y] = "o"

def check_win():
    x = 0
    o = 0
    list_win_move = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],
                     [(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],
                     [(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],
                     [(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)]]


    for comb in list_win_move:
        symbols = []
        for cord in comb:
            symbols.append(list_[cord[0]][cord[1]])
            if symbols == ["x","x","x"]:
                print(f"{player_name_1}  win!")
                return True
            elif symbols == ["o","o","o"]:
                print(f"{player_name_2} win!")
                return True

        


    result_list = [element for inner in list_ #unpacking
                   for last in inner
                   for element in last]
    
    if " " not in result_list:
        print("draw")
        return True
    
    return False
    
def new_game_again():
    print("play again?")
    print("Y - YES")
    print("N - NO")
    x = input("\n")
    while(x != "Y" and x != "N"):
        x = input("\n")
    return True if x == "Y" else False



def start_game():
    global list_, list_move_player_1, list_move_player_2
    global player_name_1, player_name_2
    list_ = new_game()
    list_move_player_1 = []
    list_move_player_2 = []
    player_name_1 = input("enter name player_1 \n")

    while(not player_name_1):
        player_name_1 = input("enter name player_1 \n")
    
    player_name_2 = input("enter name player_2 \n")

    while(not player_name_2):
        player_name_2 = input("enter name player_2 \n")

    while True:
        if check_win():
            if new_game_again():
                list_ = new_game()
                list_move_player_1 = []
                list_move_player_2 = []
            else:
                break
        view_table()
        move_player(player_name_1, 1)
        if check_win():
            if new_game_again():
                list_ = new_game()
                list_move_player_1 = []
                list_move_player_2 = []
            else:
                break
        view_table()
        move_player(player_name_2, 2)
        
    

def main():
    start_game()


if __name__ == "__main__":
    main()
    
