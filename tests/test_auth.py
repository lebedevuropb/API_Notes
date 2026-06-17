from lesson.lesson_18API.auth_api import AuthAPI


def test_register():
    reg = AuthAPI()
    response = reg.register("lesson49@gmail.com", "qwerty123", "PythonCool1")

    assert response.status_code == 201
    assert response.json()["message"] == "Успешная регистрация!"


def test_login():
    login = AuthAPI()
    response = login.login("lesson49@gmail.com", "qwerty123")

    assert response.status_code == 200
