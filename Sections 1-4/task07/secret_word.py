def get_single_letter_input():
    while True:
        letter = input("Type a single letter: ").lower()
        if len(letter) == 1 and letter.isalpha():
            return letter
        else: 
            print(f"{letter} is not a valid single letter.")

def verify_create_formated_word(word, keyword, formated):
    new_formated = ''
    index = 0
    for letter in keyword:
        if letter == word:
            new_formated += keyword[index]
        else:
            if formated[index] != '*':
                new_formated += formated[index]
            else:
                new_formated += '*'
        index += 1
    return new_formated
def game(secret_word):
    tries = 0
    formated_secret_word = '*' * len(secret_word)
    while True:
        tries += 1
        word = get_single_letter_input()
        formated_secret_word = verify_create_formated_word(word, secret_word, formated_secret_word)
        print(formated_secret_word)
        if formated_secret_word == secret_word:
            print(f"You win !  {tries} tries.")
            break

if __name__ == "__main__":
    secret_word = 'apple'
    game(secret_word)