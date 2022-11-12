# 1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
#     ‘name’: ‘Г.М.О.’,
#     ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
#     ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
#     {‘name’: ‘Шапито’,‘year’: 2014}]
# }
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.



import json, pickle

my_favotite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
               {'name': 'Шапито', 'year': 2014}]
}

json_group = json.dumps(my_favotite_group)
print(json_group)
print(type(json_group))

pickle_group = pickle.dumps(my_favotite_group)
print(pickle_group)
print(type(pickle_group))

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favotite_group, f)

with open('group.pickle', 'wb') as g:
    pickle.dump(my_favotite_group, g)


#2: Создать модуль music_deserialize.py.
#В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.

with open('group.json', 'r', encoding='utf-8') as read:
    new_file = json.load(read)
print(new_file)
print(type(new_file))

with open('group.pickle', 'rb') as h:
    picle_g = pickle.load(h)
print(picle_g)
print(type(picle_g))