"""
My approach to creating this solution has been to think about the number of moves possible in the game and
the number of possible winning combinations. I realised that it would be possible to boil down the winning
combinations to 8 winning combinations if you sort the numbers in ascending order. My solution to this problem is based
on this approach. This solution is not perfect, but it works for most cases. If I had more time or could do it again,
I would play around with a few more approaches like trying to use list indexes for checking for winners.
"""


# This function checks if the moves are winning moves or not.
# The function checks it against this list ['159', '258', '357', '456', '147', '123', '369', '789'] of win combo.
# The function will check if any of these winning combinations are present in the string combo you fee into it.
def winner_check(combo_to_test):
    winning_combinations_in_str = ['159', '258', '357', '456', '147', '123', '369', '789']
    for combo in winning_combinations_in_str:
        if combo in combo_to_test:
            return True


# This function sorts the moves and converts them into a string so that they can be checked by winner_check().
# The reason for this is that winner check has a list of strings it uses to check for a winning combination.
# step 1 is sorting the entry using sorted() to ensure that the numbers are in ascending order.
# step 2 is to join the numbers and make them 1 string.
def move_to_str_converter(entry):
    sort_entry = sorted(entry)
    converted_to_str = "".join(map(str, sort_entry))
    return converted_to_str


# These are the lists that are appended to when the for loop starts running.
X_player = []
O_player = []
taken_positions = []
board_start = ['|_1_|', '|_2_|', '|_3_|', '|_4_|', '|_5_|', '|_6_|', '|_7_|', '|_8_|', '|_9_|']

print(f"Welcome to my tic tac toe Game!!😊 \n{''.join(map(str, board_start[:3]))}"
      f"\n{''.join(map(str, board_start[3:6]))} "
      f"\n{''.join(map(str, board_start[6:]))}\nThese are your selection positions\n")


# As there are only 9 moves possible in a single game I can use a for loop with a limited range.
# This code only starts checking for winners after 5 moves as that is when the first player has enough moves to win.
# If there is no winner after 9 moves it's a draw.
for i in range(1, 6):
    player1 = int(input("X Make your move 😊, select your position between 1 and 9."))

    if player1 in taken_positions or player1 > 9 or player1 == 0:
        print("That position is already taken or out of range.")
        player1 = int(input("X Make your move 😊, select from available positions."))
    X_player.append(player1)
    taken_positions.append(player1)
    board_start[player1 - 1] = '|_X_|'
    print(f"{''.join(map(str, board_start[:3]))}\n{''.join(map(str, board_start[3:6]))}"
          f"\n{''.join(map(str, board_start[6:]))}\n")

    if i >= 3:
        X_moves = move_to_str_converter(X_player)
        if winner_check(X_moves):
            print("X is the Winner!!!")
            break
    if i == 5:
        print("it's a draw!!! Congratulations to X and O!")
        break
    player2 = int(input("O it's your turn 😊, select from available positions."))

    if player2 in taken_positions or player2 > 9 or player2 == 0:
        print("That position is already taken or out of range.")
        player2 = int(input("O it's your turn 😊, select from available positions."))
    O_player.append(player2)
    taken_positions.append(player2)
    board_start[player2 - 1] = '|_O_|'
    print(f"{''.join(map(str, board_start[:3]))}\n{''.join(map(str, board_start[3:6]))}"
          f"\n{''.join(map(str, board_start[6:]))}\n")
    if i >= 3:
        O_moves = move_to_str_converter(O_player)
        if winner_check(O_moves):
            print("O is the Winner!!!")
            break
