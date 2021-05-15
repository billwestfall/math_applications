
import random


def encode(correct, guess):
    output_arr = [''] * len(correct)

    for i, (correct_char, guess_char) in enumerate(zip(correct, guess)):
        output_arr[i] = 'X' if guess_char == correct_char else 'O' if guess_char in correct else '-'

    return ''.join(output_arr)


def safe_int_input(prompt, min_val, max_val):
    while True:
        user_input = input(prompt)

        try:
            user_input = int(user_input)
        except ValueError:
            continue

        if min_val <= user_input <= max_val:
            return user_input


def play_game():
    print("Welcome to Mastermind.")
    print("You will need to guess a random code.")
    print("For each guess, you will receive a hint.")
    print("In this hint, X denotes a correct color, and O a letter in the original string but in a different position.")
    print()

    number_of_letters = safe_int_input("Select a number of possible letters for the code (2-6): ", 2, 6)
    code_length = safe_int_input("Select a length for the code (4-4): ", 4, 4)

    letters = 'WBURGY'[:number_of_letters]
    code = ''.join(random.choices(letters, k=code_length))
    guesses = []

    while True:
        print()
        guess = (input(f"Enter a guess of length {code_length} ({letters}): ")).upper().strip()

        if len(guess) != code_length or any([char not in letters for char in guess]):
            continue
        elif guess == code:
            print(f"\nYour guess {guess} was correct!")
            break
        else:
            guesses.append(f"{len(guesses)+1}: {' '.join(guess)} => {' '.join(encode(code, guess))}")

        for i_guess in guesses:
            print("------------------------------------")
            print(i_guess)
        print("------------------------------------")


if __name__ == '__main__':
    play_game()
