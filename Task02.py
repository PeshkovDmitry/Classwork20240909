def remove_symbols(text: str) -> str:
    """
    Функция удаления из строки всех символов, кроме латиницы и пробелов
    >>> remove_symbols("hello world")
    'hello world'
    >>> remove_symbols("Hello World")
    'hello world'
    >>> remove_symbols("Hello, World!")
    'hello world'
    >>> remove_symbols("Привет World")
    ' world'
    >>> remove_symbols("Привет, World!")
    ' world'
    """
    out = ""
    for c in text:
        if (c.isascii() and c.isalpha()) or c == " ":
            out += c
    return out.lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
