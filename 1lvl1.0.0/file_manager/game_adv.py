import random


def game():
    user_number = None
    count = 0
    number = random.randint(1, 100)
    print(number)
    levels = {
        1: 10,
        2: 5,
        3: 3
    }
    level = int(input('Выберите уровень сложности: '))
    max_count = levels[level]
    print("У вас есть", levels[level], 'попыток')

    user_count = int(input('Введите количество пользователей: '))
    users = []
    for i in range(user_count):
        user_name = input(f'Введите имя пользователя {i + 1}: ')
        users.append(user_name)
    print(users)

    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1

        if count > max_count:
            print('Lose')
            break
        print(f'Попытка № {count}')

        for user in users:
            print(f'Ход пользователя {user}')
            user_number = int(input('Введите число: '))
            if user_number == number:
                is_winner = True
                winner_name = user
                break

            elif number < user_number:
                print('Ваше число больше загаданного')

            else:
                print('Ваше число меньше загаданного')
    else:
        print(f'Победил {winner_name}!')


if __name__ == '__main__':
    game()
