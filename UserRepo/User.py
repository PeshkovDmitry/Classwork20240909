class User:
    def __init__(self, name, user_id, level) -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User:{self.name}, id:{self.user_id}, level:{self.level}'