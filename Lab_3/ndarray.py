import numpy as np

print('Генерация ndarray через array()')
a = np.array([1, 2, 3])
print(a)
print(type(a))
print()

b = np.array([[1.5, 2, 3], [4, 5, 6]])
print(b)
print(type(b))

print()

b = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=complex)
print(b)
print()

print('Генерация ndarray через zeros() и ones()')
a = np.zeros((3, 5))
b = np.ones((2, 2))
print(a)
print()
print(b)
print()

print('Генерация ndarray через eye()')
a = np.eye(5, dtype=int)
print(a)
print()

print('Генерация ndarray через empty()')
a = np.empty((4, 2))
print(a)
print()

print('Генерация ndarray через arange() и linspace()')
a = np.arange(10)
print(a)
b = np.linspace(0, 2, 9)  # генерация последовательности от 0 до 2 содержащая 9 элементов
print(b)
print()

print('Генерация ndarray через func() и fromfunction')


def func(i, j):
    return 4 * i + j


print(np.fromfunction(func, (3, 4)))
print()

print('Базовые операции')
a = np.array([20, 30, 40, 50])
b = np.arange(4)

print(a)
print(b)
print()

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)  # При делении на 0 возвращается inf (бесконечность)
print('a ** b =', a ** b)
print('a % b =', a % b)  # При взятии остатка от деления на 0 возвращается 0
print()

print('Операции между массивом и числом')
print('a + 1 =', a + 1)
print('a < 35 = ', a < 35)
print()

print('Операции для обработки массивов')
print('cos: ', np.cos(a))
print('sin: ', np.sin(a))
print('и другие')
print()

print('Унарные операции')
a = np.fromfunction(func, (3, 3))
print(a)
print()
print('sum: ', a.sum())
print('max: ', a.max())
print('min: ', a.min())
print()
print(a.min(axis=0))  # наименьшее число в каждом столбце
print(a.min(axis=1))  # наименьшее число в каждой строке
print()

print('Операции индексирования массивов аналогичны другим последовательностям ')
a = np.arange(10)
print(a)
print(a[1])
print(a[3:7])
try:
    del a[4:6]
except ValueError:
    print('Нельзя удалить значения через срезы')
print()

a = np.fromfunction(func, (3, 3))
print(a)
print()
print(a[1, 2])
print(a[(1, 2)])
print(a[1][2])
print()

print('Манипуляции с формой')
a = np.fromfunction(func, (3, 6))
print(a)
print()
print(a.shape)  # форма
print(a.ravel())  # делает массив плоским
print()
a.shape = (9, 2)  # изменение формы массива
print(a)
print()
print(a.transpose())  # транспонирование
print()
print(a.reshape((3, 6)))  # изменение формы
print()
a.resize((2, 9))  # изменение массива вместе с формой
print(a)
print()

print('Объединение массивов')
a = np.array([[1, 2], [3, 4]])
b = np.array([[10, 11], [12, 13]])
print(np.vstack((a, b)))  # объединение по первым осям
print()
print(np.hstack((a, b)))  # рбъединение по последним осям
print()
print(np.column_stack((a, b)))  # объединение по столбцам
print()
print(np.row_stack((a, b)))  # объединение по строкам
print()

print('Разбиение массива')
a = np.arange(12).reshape((2, 6))
print(a)
print()
print(np.hsplit(a, 3))  # разбить по столбцам
print()
print(np.vsplit(a, 2))  # разбить по строкам
print()
print(np.array_split(a, 3))  # разбить по осям
