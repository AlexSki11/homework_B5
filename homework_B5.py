#IDLE

list_ = [[0]*3 for i in range(3)]


def new_game(): 
    list_ = [[0]*3 for i in range(3)]
    
    for i in range(3):
        list_[i][0] = ""
        for j in range(3):
            list_[i][j] = ""
    return list_

def new_game_again():
    print("play again?")
    print("Y - YES")
    print("N - NO")
    x = input("\n")
    while(x != "Y" or x != "N"):
        x = input("\n")
    return True if x == "Y" else False

def check_move(x,y):
    if 0<=x<=2 and 0<=y<=2:
        if not list_[x][y]:#code readability
            return False
        else:
            return True

    return True
def view_table(list_):
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
def move_player_1(player_name_1):
    print(f"move {player_name_1}")
    x = int(input("enter x \n"))
    y = int(input("enter y \n"))
    while(check_move(x,y)):
        print("Repeat the input")
        x = int(input("enter x \n"))
        y = int(input("enter y \n"))
    global list_
    list_[x][y] = "x"
def move_player_2(player_name_2):
    print(f"move {player_name_2}")
    x = int(input("enter x \n"))
    y = int(input("enter y \n"))
    while(check_move(x,y)):
        print("Repeat the input")
        x = int(input("enter x \n"))
        y = int(input("enter y \n"))

    list_[x][y] = "o"



def check_win(list_):
    result_list = list(filter(lambda item: not item, list_))
    if not result_list:
        print("draw")
        return new_game_again()
    
    return False
    
    


def start_game():
    list_ = new_game()
    player_name_1 = input("enter name player_1 \n")

    while(not player_name_1):
        player_name_1 = input("enter name player_1 \n")
    
    player_name_2 = input("enter name player_2 \n")

    while(not player_name_2):
        player_name_2 = input("enter name player_2 \n")

    while(check_win):
        view_table(list_)
        move_player_1(player_name_1)
        move_player_2(player_name_2)
        print(list_)
    


def main():
    start_game()


if __name__ == "__main__":
    main()
    
