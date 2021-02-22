# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Number:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __mul__(self, other):
        return self.a * other.a, self.b * other.b

    def __str__(self):
        return f'{self.a}, {self.b}'


num_1 = Number(2, 3)
num_2 = Number(3, 3)

a, b = num_1 + num_2
num_3 = Number(a, b)
print(num_3)

a, b = num_1 * num_2
num_3 = Number(a, b)
print(num_3)
