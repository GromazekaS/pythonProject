'''Упражнение 1: Написать функцию с обработкой ошибок для преобразования
строки в число
Задание: Создать функцию convert_to_int(value), которая пытается преобразовать строку в целое число. Обработать
случаи, когда преобразование невозможно, и когда возникает любое другое исключение.
Пошаговая инструкция:
 Создайте функцию convert_to_int(value).
 Используйте блок try для попытки преобразования строки в целое число с помощью функции int().
 Обработайте исключение ValueError, выведя сообщение о невозможности преобразования.
 Обработайте любое другое исключение, выведя сообщение о неожиданной ошибке.
 Добавьте блок finally, который выведет сообщение о завершении попытки преобразования.
Проверка:
 Протестируйте функцию с корректной строкой, например, "123".
 Протестируйте функцию с некорректной строкой, например, "abc".
 Протестируйте функцию с другим типом данных, например, списком [1, 2, 3].'''


def convert_to_int(value: str) -> int:
    result = None
    try:
        result = int(value)
    except ValueError:
        print("Ошибка: переданая строка не является числом.")
    except TypeError:
        print("Ошибка: переданое значение вообще список.")
    else:
        print(f"Строка: '{value}' преобразована в число {result} типа {type(result)}")
    finally:
        print("Преобразование завершено")
        return result


print(convert_to_int("abc"))
print(convert_to_int([1, 2, 3]))
print(convert_to_int("123"))
