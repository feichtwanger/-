import random

# Состояния виселицы в ASCII
HANGMAN_PICS = [
    '''
      +---+
          |
          |
          |
         ===''', '''
      +---+
      O   |
          |
          |
         ===''', '''
      +---+
      O   |
      |   |
          |
         ===''', '''
      +---+
      O   |
     /|   |
          |
         ===''', '''
      +---+
      O   |
     /|\\  |
          |
         ===''', '''
      +---+
      O   |
     /|\\  |
     /    |
         ===''', '''
      +---+
      O   |
     /|\\  |
     / \\  |
         ==='''
]

# Функция для чтения слов из файла
def load_words_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return words

# Функция для выбора случайного слова
def get_random_word(word_list):
    return random.choice(word_list)

# Функция для отображения текущего состояния игры
def display_game_state(hidden_word, wrong_guesses):
    print(HANGMAN_PICS[len(wrong_guesses)])
    print(f"Слово: {' '.join(hidden_word)}")
    print(f"Ошибки ({len(wrong_guesses)}): {', '.join(wrong_guesses)}\n")

# Основная логика игры
def play_game(words):
    word = get_random_word(words)
    hidden_word = ['_'] * len(word)
    wrong_guesses = []
    correct_guesses = set()

    while True:
        display_game_state(hidden_word, wrong_guesses)
        
        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву!\n")
            continue

        if guess in correct_guesses or guess in wrong_guesses:
            print("Вы уже вводили эту букву!\n")
            continue

        if guess in word:
            correct_guesses.add(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    hidden_word[i] = guess
            if '_' not in hidden_word:
                print("Поздравляем, вы выиграли!")
                break
        else:
            wrong_guesses.append(guess)
            if len(wrong_guesses) == len(HANGMAN_PICS) - 1:
                display_game_state(hidden_word, wrong_guesses)
                print(f"Вы проиграли! Загаданное слово было: {word}")
                break

def main():
    words = load_words_from_file('words.txt')
    
    while True:
        print("Добро пожаловать в игру 'Виселица'!")
        print("1. Начать новую игру")
        print("2. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            play_game(words)
        elif choice == '2':
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()