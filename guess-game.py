import random

def play_guess_the_number():
    print("=" * 40)
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100.")
    print("Попробуй угадать его за минимальное количество попыток.")
    print("=" * 40)

    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            user_input = input("Введите ваше предположение (или 'q' для выхода): ")
            
            if user_input.lower() == 'q':
                print(f"Жаль, что вы уходите. Загаданное число было: {secret_number}")
                break

            guess = int(user_input)
            attempts += 1

            if guess < secret_number:
                print("Ваше число МЕНЬШЕ загаданного. Попробуйте еще раз.")
            elif guess > secret_number:
                print("Ваше число БОЛЬШЕ загаданного. Попробуйте еще раз.")
            else:
                guessed = True
                print(f"\n🎉 Поздравляю! Вы угадали число {secret_number}!")
                print(f"Вам потребовалось {attempts} попыток.")
                print("=" * 40)

        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

if __name__ == "__main__":
    play_guess_the_number()