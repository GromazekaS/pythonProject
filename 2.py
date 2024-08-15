'''Упражнение 2: Написать функцию с валидацией входных данных и
генерацией исключений
Задание: Создать функцию validate_user_input(data), которая принимает словарь с данными пользователя. Функция
должна проверять наличие и корректность ключей name (строка) и age (положительное число). В случае некорректных
данных генерировать соответствующие исключения.
Пошаговая инструкция:
Создайте функцию validate_user_input(data).
Проверьте, что data является словарем. Если нет, вызовите TypeError.
Проверьте, что ключ name присутствует в словаре и его значение является строкой. Если нет, вызовите
ValueError.
Проверьте, что ключ age присутствует в словаре и его значение является положительным числом. Если нет,
вызовите ValueError.
Используйте ключевое слово from, чтобы создать цепочку исключений, если это необходимо.
Проверка:
Протестируйте функцию с корректными данными, например, {"name": "Alice", "age": 30}.
Протестируйте функцию с отсутствующим ключом name.
Протестируйте функцию с некорректным значением для age (например, строкой или отрицательным
числом).
Протестируйте функцию с некорректным типом входных данных (например, строкой вместо словаря).'''


class InvalidAgeError(Exception):
    def __init__(self, age, message="Возраст недействителен"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.age}"


def validate_user_input(data):
    try:
        if not isinstance(data, dict):
            raise TypeError
    except TypeError:
        print('Ошибка типа')
        return False
    try:
        x = data['name']
        y = data['age']
        if not isinstance(y, (int, float)): raise TypeError
        if y < 0:
            print(InvalidAgeError(y))
            raise InvalidAgeError(y)
    except KeyError:
        print('Ошибка ключа')
        return False
    except TypeError:
        print('Ошибка типа поля "age"')
        return False
    except InvalidAgeError:
        print('Недопустимое значение поля "age"')
        return False
#    try:
#        data.get('name')
#    except ValueError:
    return True

test_dict = {"name": "Alice", "age": 30}

print(test_dict)
print(f"Данные являются корректным словарем: {validate_user_input(test_dict)}")
print("\ndata = {'age': -10}")
print(f"Данные являются корректным словарем: {validate_user_input({'age': -10})}")
print("\ndata = {'name': 'Mike', 'age': -10}")
print(f"Данные являются корректным словарем: {validate_user_input({'name': 'Mike', 'age': -10})}")
print('\ndata = [1, 2, 3]')
print(f"Данные являются корректным словарем: {validate_user_input([1, 2, 3])}")
print('\nEnd')
