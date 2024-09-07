from json import load, dump
from UserRepo.User import User
from UserRepo.LevelError import LevelError


class Repo:
    users = set()

    @staticmethod
    def load_users(path):
        with open(path, encoding='utf-8') as f:
            data = load(f)
        for level, value in data.items():
            for uid, name in value.items():
                Repo.users.add(User(name, uid, level))

    @staticmethod
    def check_login(name):
        try:
            for user in Repo.users:
                if user.name == name:
                    return f"{name} Пользователь найден!"
            raise NameError
        except NameError:
            return 'Пользователь не найден'

    @staticmethod
    def create_user(name, id_user, level):
        try:
            if level > 3:
                raise LevelError
        except LevelError:
            return 'Ошибка уровня'
        else:
            Repo.users.add(User(name, id_user, level))
