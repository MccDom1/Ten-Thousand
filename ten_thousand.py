# main.py
from ten_thousand.game_logic import GameLogic
from ten_thousand.utils import get_input
def main():
    print("Welcome to the Ten Thousand dice game!")
    total_score = 0
    current_round = 1
    while True:
        print(f"\nRound {current_round}")
        num_dice = get_input("Enter the number of dice to roll: ")
        dice_roll = GameLogic.roll_dice(num_dice)
        print(f"You rolled: {dice_roll}")
        score = GameLogic.calculate_score(dice_roll)
        print(f"Score for this roll: {score}")
        total_score += score
        print(f"Total score: {total_score}")
        play_again = input("Do you want to roll again or bank the current score? (roll/bank): ").lower()
        if play_again == 'bank':
            print(f"Round {current_round} completed. Banking {total_score} points.")
            total_score = 0
            current_round += 1
        elif play_again != 'roll':
            break
    print("Thanks for playing!")
if __name__ == "__main__":
    main()