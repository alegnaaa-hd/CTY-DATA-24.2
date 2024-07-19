

RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
LIGHTGREY = '\033[37m'
DARKGREY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[93m'
LIGHTBLUE = '\033[94m'
PINK = '\033[95m'
LIGHTCYAN = '\033[96m'
RESET = '\033[0m'
color_dictionary = {
        "red" : RED,
        "green" : GREEN,
        "orange" : ORANGE,
        "blue" : BLUE,
        "purple": PURPLE,
        "cyan": CYAN,
        "lightgrey": LIGHTGREY,
        "darkgrey": DARKGREY,
        "lightred": LIGHTRED,
        "lightgreen": LIGHTGREEN,
        "yellow": YELLOW,
        "lightblue": LIGHTBLUE,
        "pink": PINK,
        "LIGHTCYAN": LIGHTCYAN
}

# asks two users their colors of choice
# and their specific characters to play with
# returns a tuple (player1settings, player2settings)
# player1setting itself is a tuple(player1_piece,player1_color)
# player2setting itself is a tuple(player2_piece,player1_color)
# if there is an error, choose default colors, and characters for user_settings
def get_user_settings():

    global color_dictionary
    global RESET
    user_1piece = str(input("Enter Just One character to represent player 1: "))
    user_2piece = str(input("Enter Just One character to represent player 2: "))
    print("List of colors to choose from: ", end="")
    j = 0 
    for color_key_value in color_dictionary.items():
        (color_key,color_value) = color_key_value
        color_name = str(color_key).upper()
        print(f" {color_value} {color_name} {RESET}, ", end="")
        if j >= 4:
            print("")
            j = 0
        else:
            j += 1
    try:
        player1_color = str(input("Enter Player 1 color: "))
        player2_color = str(input("Enter Player 2 color: "))
        player1_color = player1_color.lower()
        player2_color = player2_color.lower()
        player1_color_code = color_dictionary[player1_color]
        player2_color_code = color_dictionary[player2_color]
        users_settings = ((user_1piece,player1_color_code),(user_2piece,player2_color_code))
        return users_settings
    except:
        user1_default = ('X', GREEN)
        user2_default = ('Y', RED)
        default_users_settings = (user1_default,user2_default)

        return default_users_settings
    
        
        
        

    

    