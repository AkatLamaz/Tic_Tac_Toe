import os

button = 0

skeleton = [
    ['', ' ', '|', ' ', '|', ' '],
    ['', '-', '|', '-', '|', '-'],
    ['', ' ', '|', ' ', '|', ' '],
    ['', '-', '|', '-', '|', '-'],
    ['', ' ', '|', ' ', '|', ' ']
]

skeleton_show = [
    ['1', '|', '2', '|', '3'],
    ['-', '|', '-', '|', '-'],
    ['4', '|', '5', '|', '6'],
    ['-', '|', '-', '|', '-'],
    ['7', '|', '8', '|', '9']
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome_message():
    print("Welcome to Tic Tac Toe game!\n")

def start_game():
    button = int(input("Press '1' to start the game: "))
    if button == 1:
        clear_screen()
    else:
        print("Please press '1' to start the game.")

def print_player_symbols(player1_symbol, player2_symbol):
    print("Player 1", player1_symbol, "vs", player2_symbol, "Player 2 \n")

def get_player_move(player_symbol):
    print("Player", player_symbol)
    gui()
    while True:
        try:
            button = int(input("Enter a number (or 0 to exit): "))
            if button == 0:
                print("Exiting game...")
                exit()
            elif 1 <= button <= 9:
                row = ((button * 2) - 1) // 6 # Indeks wiersza
                col = ((button * 2) - 1) % 6 # Indeks kolumny
                if row == 1:
                    row += 1
                elif row == 2:
                    row += 2
                if skeleton[row][col] == ' ':
                    skeleton[row][col] = player_symbol
                    break
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

def play_game(player1_symbol, player2_symbol):
    i = 0
    while i < 9:
        if i % 2 == 0:
            get_player_move(player1_symbol)
        else:
            get_player_move(player2_symbol)
        clear_screen()
        gui()
        if check_winner():
            if i % 2 == 0:
                print("Player 1 Wins!")
            else:
                print("Player 2 Wins!")
            break
        i += 1
    else:
        print("It's a tie!")

def ask_to_play_again():
    restart = input("Do you want to play again? (y/n): ")
    return restart.lower() == "y"

def gui():
    for row1, row2 in zip(skeleton, skeleton_show):
        print(' '.join(row1) + '       ' +' '.join(row2))

def check_winner():
    # check rows
    for row in range(0, 5, 2):
        if skeleton[row][1] == skeleton[row][3] == skeleton[row][5] and skeleton[row][1] != ' ': 
            return True

    # check columns
    for col in range(1, 6, 2):
        if skeleton[0][col] == skeleton[2][col] == skeleton[4][col] and skeleton[0][col] != ' ': 
            return True

    # check diagonals
    if skeleton[0][1] == skeleton[2][3] == skeleton[4][5] and skeleton[0][1] != ' ': 
        return True
    if skeleton[0][5] == skeleton[2][3] == skeleton[4][1] and skeleton[0][5] != ' ': 
        return True

    return False

def reset_game():
 global skeleton
 skeleton = [
    ['', ' ', '|', ' ', '|', ' '],
    ['', '-', '|', '-', '|', '-'],
    ['', ' ', '|', ' ', '|', ' '],
    ['', '-', '|', '-', '|', '-'],
    ['', ' ', '|', ' ', '|', ' '] 
]

def main():
    print_welcome_message()
    start_game()
    player1_symbol = "O"
    player2_symbol = "X"
    print_player_symbols(player1_symbol, player2_symbol)
    while True:
        play_game(player1_symbol, player2_symbol)
        if not ask_to_play_again():
            break
        reset_game()

if __name__ == "__main__":
 main()