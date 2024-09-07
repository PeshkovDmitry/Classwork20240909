from UserRepo.UserException import UserException


class LevelError(UserException): # ошибка при проверке на уровень пользователя
    def __init__(self, level, exam):
        self.level = level
        self.exam = exam

    def __str__(self):
        return f'Уровень пользователя должен быть не ниже {self.exam}.\n' \
        f'Ваш уровень {self.level}. Ошибка добавления.'