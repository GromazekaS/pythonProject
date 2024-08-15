'''Упражнение 3: Написать класс собственного исключения и использовать его
Задание: Создать класс NegativeNumberError, который будет генерироваться, если переданное число
отрицательное. Использовать это исключение в функции check_positive_number.
Пошаговая инструкция:
 Создайте класс NegativeNumberError, наследующий от Exception.
 Переопределите конструктор, чтобы принимать значение числа и сообщение об ошибке.
 Переопределите метод __str__, чтобы возвращать информативное сообщение.
 Создайте функцию check_positive_number, которая проверяет, является ли число положительным. Если
число отрицательное, функция должна вызывать исключение NegativeNumberError.
Проверка:
 Протестируйте функцию с отрицательным числом.
 Протестируйте функцию с положительным числом.
 Убедитесь, что исключение NegativeNumberError правильно обрабатывается и выводит информативное
сообщение.'''


class NegativeNumberError(Exception):
    def __init__(self, value, message="Ошибка. Отрицательное число"):
        self.val = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.val}"

def check_positive_number(value: int):
    try:
        if value < 0:
            raise NegativeNumberError(value)
    except NegativeNumberError:
        print(NegativeNumberError(value))
        return False
    return True


print(check_positive_number(-5))
print(check_positive_number(5))
