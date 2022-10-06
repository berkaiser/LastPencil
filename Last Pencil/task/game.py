import random
msg_0 = "How many pencils would you like to use:"
msg_1 = "The number of pencils should be numeric"
msg_2 = "The number of pencils should be positive"
msg_3 = "Who will be the first (John, Jack):"
msg_4 = "Choose between 'John' and 'Jack'"
msg_5 = "Possible values: '1', '2' or '3'"
msg_6 = "Too many pencils were taken"

players = ["John", "Jack"]
possibles = ["1", "2", "3"]


def pencount(x):
    print(x * "|")

def whats_left(x, y):
    if x + 1 < y:
        print("Too many pencils were taken")

def who_won(x, winner):
    if x == 0:
        print(f"{winner} won!")

def check_possibles():
    while True:
        user_input = input()
        if user_input not in possibles:
            print(msg_5)
        else:
            if int(user_input) > pencils:
                print(msg_6)
            else:
                return  int(user_input)

def bot(x):
    if x % 4 == 0:
        return 3
    if x % 4 == 3:
        return 2
    if x % 4 == 2:
        return 1
    else:
        return 1


# Game
print(msg_0)
while True:
    number = input()
    # Check number
    if number.isdigit() == False:
        print(msg_1)
    elif int(number) <= 0:
        print(msg_2)
    while number.isdigit() == True and int(number) != 0:
        print(msg_3)
        player_1 = input()
        # Check player
        while player_1 not in players:
            print(msg_4)
            player_1 = input()
            continue
        # Game starts
        pencils = int(number)
        while player_1 in players:
           if player_1 == "John":
               next_player = "Jack"
               pencount(pencils)
               print(f"{player_1}'s turn: ")
               pen_of_one = check_possibles()
               pencils -= pen_of_one
               if pencils == 0:
                   print(f"{next_player} won!")
                   exit()
                   break
               pencount(pencils)
               #The Bot plays
               print(f"{next_player}'s turn!")
               pen_of_next = bot(pencils)
               print(pen_of_next)
               pencils -= int(pen_of_next)
               if pencils == 0:
                   print(f"{player_1} won!")
                   exit()

           elif player_1 == "Jack":
               next_player = "John"
               pencount(pencils)
               print(f"{player_1}'s turn!")
               pen_of_one = bot(pencils)
               print(pen_of_one)
               pencils -= int(pen_of_one)
               if pencils == 0:
                   print(f"{next_player} won!")
                   exit()
                   break
               pencount(pencils)
                # Player's turn
               print(f"{next_player}'s turn:")
               pen_of_next = check_possibles()
               pencils -= pen_of_next
               if pencils == 0:
                   print(f"{player_1} won!")
                   exit()
                   break
        break
