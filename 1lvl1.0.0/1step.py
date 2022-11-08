# 1
# number = int(input("Введтие число: "))
# number = number + 2
# print(number)
# 2
# number = -1
# while number < 0 or number > 10 :
#     number = int(input("Введите число: "))
#     if number > 10:
#         print("введеное число больше необходимого")
#     if number < 0:
#         print("Число меньше необходимого")
#
# else:
#     if number == 0:
#         print("Ноль в квадрате = ", number)
#     else:
#         number = number ** 2
#         print(number)

while True:
    number = int(input('Введите число: '))
    if number > 0 and number < 10:
        print(number ** 2)
        break
    else:
        print('Число должно быть >0 и 10<')
# Мед карта
# print("Заполните медецинскую карту:")
# name = input("Введите ваше имя: ")
# second_name = input("Введите вашу фамилию: ")
# age = int(input("Введите ваш возраст: "))
# mass = float(input("Введите ваш вес: "))
#
# if age < 30 and 50 <= mass  < 120:
#     print(name, second_name, age, mass, "- хорошее состояние")
# elif age > 30 and 50 < mass <= 120:
#     print(name, second_name, age, mass, "- Вам следует заняться собой")
# elif age > 40 and 120 > mass < 50:
#     print(name, second_name, age, mass, "- Вам требуется врач")
# else:
#     print(name, "- с вами все ок")