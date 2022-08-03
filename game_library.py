import random

ROCK = "r"
SISSORS = "s"
PAPER = "p"
INVALID = "i"
valid_choices = [ROCK, PAPER, SISSORS]
choice_to_move_mapping = {
    "r": ROCK,
    "ro": ROCK,
    "roc": ROCK,
    "rock": ROCK,
    "s": SISSORS,
    "si": SISSORS,
    "sis": SISSORS,
    "siss": SISSORS,
    "sisso": SISSORS,
    "sissor": SISSORS,
    "sissors": SISSORS,
    "p": PAPER,
    "pa": PAPER,
    "pap": PAPER,
    "pape": PAPER,
    "paper": PAPER,
}




def get_user_choice(input_str):    
    lower_str = input_str.lower()                 #sets input_str to lower case
    if lower_str in choice_to_move_mapping:       #checks dic for a match with lower_str
        return choice_to_move_mapping[lower_str]  #returns value
    
    return INVALID

def play_rock_paper_sissors():
    num_of_rounds = int(input("How many games do you want to play?\n"))
    round_count = 0
    user_total = 0
    cpu_total = 0

    while num_of_rounds > int(user_total + cpu_total):
        user = input("Choose your weapon: 'r' for rock, 'p' for paper, and 's' for sissors\n")
        user_final = get_user_choice(user)
        if user_final == INVALID:
            return("Game Over")

        cpu_final = random.choice(valid_choices)

        print(user_final + "/" + cpu_final)

        if user_final == cpu_final:
          #  user_total += 1
          #  cpu_total += 1
            print("You tied this round!") 
            print("Score (" + str(user_total) + "/" + str(cpu_total) + ") of " + str(num_of_rounds))
    
        elif is_win(user_final,cpu_final ):
            user_total += 1
            print("You won this round!")
            print("Score (" + str(user_total) + "/" + str(cpu_total) + ") of " + str(num_of_rounds)) 
        
        elif is_win(user_final, cpu_final) == False:
            cpu_total += 1
            print("You lost this round.") 
            print("Score (" + str(user_total) + "/" + str(cpu_total) + ") of " + str(num_of_rounds)) 
        else:
            print("Invalid return from is_win")
        round_count += 1

    if user_total > cpu_total:
        return("Congragulations, You win the match!")
    elif user_total < cpu_total:
        return("Congragulations, You suck and lose!")
    elif user_total == cpu_total:
        return("Da Fak, we tied???")

  
# def long_hand(letter):
#     if letter == SISSORS:
#         return "sissors"
#     elif letter == ROCK:
#         return "rock"
#     elif letter == PAPER:
#         return "paper"




def is_win(player,opponent):
    #returns true if player wins

    if player == ROCK and opponent == PAPER:
        return False
    elif player == ROCK and opponent == SISSORS:
        return True
    elif player == PAPER and opponent == SISSORS:
        return False
    elif player == PAPER and opponent == ROCK:
        return True
    elif player == SISSORS and opponent == ROCK:
        return False
    elif player == SISSORS and opponent == PAPER:
        return True
    


print(play_rock_paper_sissors())