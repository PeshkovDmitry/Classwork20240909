import pytest
from UserRepo.Repo import Repo
from UserRepo.User import User


@pytest.fixture
def good_user_data():
    name = "Скворцов"
    id_user = 9
    level = 1
    return name, id_user, level


@pytest.fixture
def bad_user_data():
    name = "Мухоморов"
    id_user = 8
    level = 4
    return name, id_user, level


@pytest.fixture
def user_set():
    user_set = set()
    user_set.add(User("Иванов", 1, 1))
    user_set.add(User("Петров", 2, 2))
    user_set.add(User("Сидоров", 3, 3))
    return user_set


@pytest.fixture
def repo(user_set):
    repo = Repo()
    repo.users.update(user_set)
    return repo


def test_passed_checking(repo):
    assert repo.check_login("Сидоров") == "Сидоров Пользователь найден!"


def test_failed_checking(repo):
    assert repo.check_login("Комаров") == "Пользователь не найден"


def test_adding(repo, good_user_data):
    repo.create_user('Семенов', 8, 3)
    assert repo.check_login("Семенов") == "Семенов Пользователь найден!"


if __name__ == '__main__':
    pytest.main(['-v'])
