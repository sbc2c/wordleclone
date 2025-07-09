import random

# ansi color codes
# asked google how to use ansi color codes
GREEN = "\033[42m\033[30m"   # green background, black text
YELLOW = "\033[43m\033[30m"  # yellow background, black text
GRAY = "\033[47m\033[30m"    # light gray background, black text
RESET = "\033[0m"

# load words from file
def load_words(filename):
    with open(filename, "r") as file:
        return [line.strip().lower() for line in file if len(line.strip()) == 5 and line.strip().isalpha()]

# get feedback on guess
def get_feedback(guess, target):
    feedback = [""] * 5
    target_list = list(target)

    # green pass
    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = "green"
            target_list[i] = None

    # yellow/gray pass
    for i in range(5):
        if feedback[i] == "":
            if guess[i] in target_list:
                feedback[i] = "yellow"
                target_list[target_list.index(guess[i])] = None
            else:
                feedback[i] = "gray"
    return feedback

# update alphabet status
def update_alphabet(alphabet, guess, feedback):
    for i in range(5):
        letter = guess[i]
        if feedback[i] == "green":
            alphabet[letter] = "green"
        elif feedback[i] == "yellow" and alphabet[letter] != "green":
            alphabet[letter] = "yellow"
        elif feedback[i] == "gray" and alphabet[letter] == "":
            alphabet[letter] = "gray"

# display guess with colored boxes
def display_guess(guess, feedback):
    for i in range(5):
        if feedback[i] == "green":
            print(f"{GREEN} {guess[i].upper()} {RESET}", end=" ")
        elif feedback[i] == "yellow":
            print(f"{YELLOW} {guess[i].upper()} {RESET}", end=" ")
        else:
            print(f"{GRAY} {guess[i].upper()} {RESET}", end=" ")
    print()

# display alphabet with colored letters
def display_alphabet(alphabet):
    print("alphabet:")
    for letter in "abcdefghijklmnopqrstuvwxyz":
        status = alphabet[letter]
        if status == "green":
            print(f"{GREEN} {letter.upper()} {RESET}", end=" ")
        elif status == "yellow":
            print(f"{YELLOW} {letter.upper()} {RESET}", end=" ")
        elif status == "gray":
            print(f"{GRAY} {letter.upper()} {RESET}", end=" ")
        else:
            print(f" {letter.upper()} ", end=" ")
    print("\n")

# main game loop
def play_wordle():
    words = load_words("words.txt")
    target = random.choice(words)
    attempts = 5
    alphabet = {ch: "" for ch in "abcdefghijklmnopqrstuvwxyz"}

    print("welcome to wordle!\n")

    for turn in range(1, attempts + 1):
        while True:
            guess = input(f"guess {turn}/5: ").lower()
            if len(guess) == 5 and guess.isalpha():
                break
            print("please enter a valid 5-letter word.")

        feedback = get_feedback(guess, target)
        update_alphabet(alphabet, guess, feedback)

        print("\nyour guess:")
        display_guess(guess, feedback)
        display_alphabet(alphabet)

        if guess == target:
            print(f"{GREEN}you guessed the word! {RESET}")
            return

    print(f"{GRAY}you're out of guesses. the word was: {target.upper()}{RESET}")

# run the game
play_wordle()
