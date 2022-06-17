import unittest
from collections import ChainMap

print('Генерация ChainMap без аргументов')
a = ChainMap()
print(a)
print(type(a))
print()

print('Генерация ChainMap с аргументами')
numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}
all = ChainMap(numbers, letters)

print(all)
print(type(all))
print()

print('ChainMap может содержать повторяющиеся ключи с разными значениями')
a = {'1': 'mom', '2': 'dad', '3': 'son'}
b = {'1': 'cat', '2': 'dog'}
family = ChainMap(a, b)

print(family)
print(type(family))
print()

print('ChainMap поддерживает все методы словаря')
print(f'Метод fromkeys: {ChainMap.fromkeys(["one", "two", "three"])}')
print(f'Метод get: {all.get("one")}')
print('и т.д.')
print()

print('ChainMap: maps')
print(all.maps)  # возвращает список из всех входных отобажений

all.maps.append({"c": "C"})
print(all.maps)
print()

print('ChainMap: new_child()')
bool = {"0": False, "1": True}
all = all.new_child(
    bool)  # возвращает новый ChainMap, содержащий входное отбражение - параметр(bool), за ним следуют все текущие отображения ChainMap

for i in all.maps:
    print(i)
print()

print('ChainMap: parents')
all = all.parents  # возвращает новый ChainMap со всеми текущими отображениями ChainMap, кроме первого

for i in all.maps:
    print(i)
print()


class MyTestCase(unittest.TestCase):
    def test_error_non_int_float(self):
        """Ключ отсутствует после поиска по всему списку отображений"""
        with self.assertRaises(KeyError) as context:
            all["three"]


if __name__ == '__main__':
    unittest.main()
