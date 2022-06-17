import unittest

print('Генерация range(Stop)')
a = range(10)
print(a)
print(type(a))
for it in a:
    print(it, end=" ")
print('\n')

print('Генерация range(Start, Stop[, Step])')
b = range(5, 10)
print(b)
print(type(b))
for it in b:
    print(it, end=" ")
print('\n')

c = range(5, 10, 2)
print(c)
print(type(c))
for it in c:
    print(it, end=" ")
print('\n')

print('Преобразование range в list')
c_list = list(c)
print(c_list)
print(type(c_list))
print()

print('Использование индекса с результатом работы range')
print(range(0, 10)[1])
print(range(0, 10)[9])
print()

print('Диапозон с отрицательными числами')
d = range(-10, -3)
for it in d:
    print(it, end=" ")
print('\n')

print('Нулевой диапозон')
d = range(0)
print(list(d))
print()

print('Объединенный вывод двух range')


def union():
    from itertools import chain
    merged = chain(range(5), range(10, 15))
    for it in merged:
        print(it, end=" ")


union()
print('\n')


class MyTestCase(unittest.TestCase):
    """Аргументы не могут быть float или str, только int"""
    def test_error_non_int_float(self):
        with self.assertRaises(TypeError) as context:
            range(1.1),

    def test_error_non_int_str(self):
        with self.assertRaises(TypeError) as context:
            range('str')

    def test_error_step(self):
        """Step не может быть 0"""
        with self.assertRaises(ValueError) as context:
            range(1, 10, 0)


if __name__ == '__main__':
    unittest.main()
