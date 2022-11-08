# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
#    Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def func(name, age, city):
    return print('{}, {} год(а), проживает в городе {}'.format(name, age, city))

func("Василий", 21, "Москва")

# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def max_number(x,y,z):
    result = (int(max(x, y, z)))
    return result

print(max(2,4,6))

# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

player_name = str(input('Введите имя персонажа №1: '))
player = {
    'name': player_name,
    'health': 100,
    'damage': 40,
    'armor': 1.6
}
enemy_name = str(input('Введите имя персонажа №2: '))
enemy = {
    'name': enemy_name,
    'health': 100,
    'damage': 60,
    'armor': 1.3
}
print(player)
print(enemy)

def attack(unit, target):
    damage = armor(unit['damage'], target['armor'])
    target['health'] -= damage
    print(f'Игрок {unit["name"]}, атаковал Игрока {target["name"]}, и нанес ему {unit["damage"]} урона. У Игрока {target["name"]} осталось {round(target["health"], 2)} здоровья ')

def armor(damage, armor):
    return damage / armor

attack(player, enemy)