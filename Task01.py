def remove_symbols(text: str) -> str:
    """
    Функция удаления из строки всех символов, кроме латиницы и пробелов
    >>>remove_symbols("Hello, world!")
    hello world
    """
    out = ""
    for c in text:
        if (c.isascii() and c.isalpha()) or c == " ":
            out += c
    return out.lower()


if __name__ == "__main__":
    print(remove_symbols("Привет, мир!"))
    print(remove_symbols("Hello, world!"))
