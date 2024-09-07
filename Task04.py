from Task01 import remove_symbols
import pytest


def test_method_1():
    assert remove_symbols("hello world") == 'hello world'


def test_method_2():
    assert remove_symbols("Hello World") == 'hello world'


def test_method_3():
    assert remove_symbols("Hello, World!") == 'hello world'


def test_method_4():
    assert remove_symbols("Привет World") == ' world'


def test_method_5():
    assert remove_symbols("Привет, World!") == ' world'


if __name__ == "__main__":
    pytest.main(['-v'])
