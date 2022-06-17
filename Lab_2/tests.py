import unittest
from main import gen_bin_tree, gen_bin_tree_recursive


class TestBinTreeGeneration(unittest.TestCase):
    """Тест рекурсивной функции"""
    def test_simple_case_recursive(self):
        self.assertEqual(gen_bin_tree_recursive(2, 13, lambda x: x + 5, lambda x: x * 3), {13: [{18: []}, {39: []}]})

    """Тест нерекурсивной функции"""
    def test_simple_case_non_recursive(self):
        self.assertEqual(gen_bin_tree(2, 13, lambda x: x + 5, lambda x: x * 2), {13: [{18: []}, {39: []}]})

    """Тест границ рекурсивной функции"""
    def test_limit_values_recursive(self):
        self.assertEqual(gen_bin_tree_recursive(1, 13, lambda x: x + 5, lambda x: x * 2), {13: []})

    """Тест границ нерекурсивной функции"""
    def test_limit_values_non_recursive(self):
        self.assertEqual(gen_bin_tree(1, 13, lambda x: x + 5, lambda x: x * 2), {13: []})

    """Тест на ввод 0 рекурсивной функции"""
    def test_error_recursive(self):
        with self.assertRaisesRegex(RecursionError, 'maximum recursion depth exceeded in comparison'):
            gen_bin_tree_recursive(0, 13, lambda x: x + 5, lambda x: x * 2)

    """Тест на ввод 0 нерекурсивной функции"""
    def test_error_non_recursive(self):
        with self.assertRaisesRegex(IndexError, 'list index out of range'):
            gen_bin_tree(0, 13, lambda x: x + 5, lambda x: x * 2)
