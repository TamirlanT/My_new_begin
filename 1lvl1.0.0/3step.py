# Практическое задание
# 1. В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.


# Компьютер начинает его отгадывать предлагая игроку варианты чисел.
# Если компьютер угадал число, игрок выбирает “победа”.
# Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”.
# Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.


import random

bigger = '>'
lower = '<'

max = 100
min = 1
user_input = None
my_number = int(input('Введите ваше число: '))
bot_number = random.randint(min, max)

while my_number != bot_number:
    bot_number = random.randint(min,max)
    print(f'{bot_number} Это ваше число ?')
    user_input = str(input("Если оно больше введите '>', если оно меньше '<' "))

    if user_input == bigger:
        min = bot_number + 1
        bot_number = random.randint(min,max)
    else:
        max = bot_number - 1
        bot_number = random.randint(min,max)

else:
    print(f'Ваше число {bot_number}! Я победил! ')
