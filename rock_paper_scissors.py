# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

p1 = input("Player 1: ")
p2 = input("Player 2: ")
answers = ["rock", "paper", "scissors"]


def play_game():
    yn= input("Do you want to play?")
    if yn == "yes":
        a1 = input("{} you go first.".format(p1))
        a2 = input("{} your turn.".format(p2))
        while a1 and a2 in answers:
            if a1 == a2:
                print("Uhm, play again.")
                play_game()
            elif a1 == "rock" and a2 == "paper":
                p2_wins()
                break
            elif a1 == "rock" and a2 == "scissors":
                p1_wins()
            elif a1 == "paper" and a2 == "rock":
                p1_wins()
            elif a1 == "paper" and a2 == "scissors":
                p2_wins()
                break
            elif a1 == "scissors" and a2 == "rock":
                p1_wins()
                break
            elif a1 == "scissors" and a2 == "paper":
                p1_wins()
                break
    else:
        print("another time then.")


def p1_wins():
    print("Congratulations {}, you win!".format(p1))
    play_game()


def p2_wins():
    print("Congratulations {}, you win!".format(p2))
    play_game()


play_game()
