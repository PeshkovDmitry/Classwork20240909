from Task01 import remove_symbols
import unittest


class TestSymbolRemover(unittest.TestCase):

    def test_method_1(self):
        self.assertEqual(remove_symbols("hello world"), 'hello world', "Повторение строки не сработало")

    def test_method_2(self):
        self.assertEqual(remove_symbols("Hello World"), 'hello world', "Изненение регистра не сработало")

    def test_method_3(self):
        self.assertEqual(remove_symbols("Hello, World!"), 'hello world', "Удаление знаков пунктуации не сработало")

    def test_method_4(self):
        self.assertEqual(remove_symbols("Привет World"), ' world', "Удаление кириллицы не сработало")

    def test_method_5(self):
        self.assertEqual(remove_symbols("Привет, World!"), ' world', "Комплексный тест не сработал")


if __name__ == "__main__":
    unittest.main()
