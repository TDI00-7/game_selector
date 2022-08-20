import rps
import ttt

def main():
    game_on = True
    while game_on:
        game_selection = input(f"What game would you like to play?\n(1) Rock Paper Scissors\n(2) Tic Tac Toe\n(3) I dont want to play anymore\n")
        if game_selection == "1":
            rps.play_rock_paper_sissors()
            game_on = play_again()
        elif game_selection == "2":
            ttt.player_move()
            game_on = play_again()
        elif game_selection == "3":
            exit
        else:
            print("Game Over")
            exit


def play_again():
    anwser = input(f"Would you like to play another game? Enter (y) or (n)\n")
    if anwser == "n":
        game_on = False
        return game_on   


if __name__ == "__main__":
    main()