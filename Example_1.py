# 1 - Дано число, привести его к типу str / bool
a = 2  # int
a = str(a)  # '2'
a = bool(a)  # 'True'

# 2 - Написать результат сложения строки '100' и числа 99
''' 
'100' и 99 сложить нельзя т.к. это разные типы данных. Нужно их привести к одному общему
'''

# 3 - Чем отличается тип данных list от tuple?
''' 
Список(list) отличается от кортежа(tuple) тем что он изменяемый (можно добавлять/удалять элементы, изменять их).
Кортеж же не изменяемый. Также у них отличие в синтаксисе: список пишется как [], кортеж ().
Из-а того что список изменяемый у него 'плавающая' длина, у кортежа она неизменна.
'''

# 4 - Напишите код, который принимает на ввод число:
# a - если передано не числовое значение, вывести сообщение об ошибке
# b - если передали число, то возвести его в квадрат и умножить на 10

q = int(input())  # если мы введем не целое число, то будет ошибка типа данных
print((q ** 2) * 10)  # возводим введённое число в квадрат и умножаем на 10
# Вообще тут очень несколько вариантов. Например, можно в первой строке указать просто input(), а дальше через if
# if type(q) == int...

# 5 - Проверяем наличие ключа 'x' в словаре 'data'
''' 
 1) Можно решить методом d.keys(). Так мы увидим все ключи в данном словаре.
 2) data.items() Увидим все ключи и все значения в словаре 'data'.
 3) data['x'] Если ключа 'х' нет, то получим ошибку.
 4) data.pop('x') Если ключ 'x' есть, то пара ключ-значения удалится из словаря. Если нет, то получим ошибку.
 5) del data['x']  Если ключ 'x' есть, то пара ключ-значения удалится из словаря. Если нет, то получим ошибку.
 6) 'x' in data Если ключ 'x' есть, то получим True. Если нет, то получим False.
 7) data.get('x') Если ключ 'x' есть, то получим его значение. Если нет, то получим None.
 8) data.setdefault('x') Если ключ 'х' есть в словаре, то увидим его значение.
 Если ключа 'х' нет, то он будет создан, а его значение станет None. Также значение None можно изменить указав в запросе
 через запятую нужное нам значение, например  data.setdefault('x', 123)). Будет 'x': 123, но если 'x' там был, то не 
 изменится.
 9) print(data) Увидим весь словарь xDDD тоже можно поискать ключ 'x'.
 10) Можно преобразовать словарь в список (list(data)) и получить список его ключей.
 11) Также можно используя методы описанные выше, но через if...      if 'x' in data...
 '''

# 6 - Дан словарь (dict). В словаре может быть любое количество ключей, а значения только int/str.
user = {
    'first_name': 'John',
    'last_name': 'Wick',
    'age': 99
}

# v1
# first_name: John
# last_name: Wick
# age: 99


def print_dict_v1(dict):
    for key, value in dict.items():
        print(key, value, sep=': ')

# v2
# - First Name: John (str)
# - Last Name: Wick (str)
# - Age: 99 (int)


def print_dict_v2(dict):
    for key, value in dict.items():

        if type(value) == int:
            value_type = 'int'
        else:
            value_type = 'str'

        print(f'- {key.title().replace("_"," ")}: {value} ({value_type})')

# v3
# Quick stats:
# - 3 keys (first_name, last_name, age)
# - 2 unique types (str, int)
# ----
# - First Name: John (str)
# - Last Name: Wick (str)
# - Age: 99 (int)


def print_dict_v3(dict):
    print('Quick stats:')

    user_keys = []
    for key in user.keys():
        user_keys.append(key)
    keys = ', '.join(user_keys)
    print(f'- {len(dict)} keys ({keys})')

    user_values = []
    for types in user.values():
        if type(types) == str:
            user_values.append('str')
            str_type = 1    # показываем что этот тип присутствует в словаре
        else:
            user_values.append('int')
            int_type = 1    # такой же счетчик, но для другого типа

    for elem in user_values:    # убираем повторы
        if user_values.count(elem) > 1:
            user_values.remove(elem)

    user_values = ', '.join(user_values)

    print(f'- {str_type + int_type} unique types: ({user_values})')
    print('----\nDict information:')

    for key, value in dict.items():       # далее идёт повтор функции v2

        if type(value) == int:
            value_type = 'int'
        else:
            value_type = 'str'

        print(f'- {key.title().replace("_"," ")}: {value} ({value_type})')
