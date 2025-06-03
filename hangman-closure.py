# hangman-closure.py
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = "".join([c if c in guesses else "_" for c in secret_word])
        print(display)
        return set(secret_word).issubset(set(guesses))

    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter secret word: ").lower()
    guess_fn = make_hangman(secret)

    while True:
        guess = input("Enter a letter: ").lower()
        if guess_fn(guess):
            print("You guessed the word!")
            break

