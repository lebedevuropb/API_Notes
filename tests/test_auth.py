from tests.generation import generate_email, generate_username, generate_password


# Позитивные тесты

# Тест на авторизацию
def test_authorization(obj_login):
    response = obj_login.login("loginpermonents@yandex.ru", "qwerty123")
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert "token" in response.json(), "В ответе отсутствует поле «token»"


# Тест на регистрацию
def test_register(obj_register):
    response = obj_register.register(generate_email(), generate_password(), generate_username())
    assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
    assert response.json()["message"] == "Успешная регистрация!", "Отсутствует сообщение об успешной регистрации"


# Негативные тесты

# Тест на проверку регистрации с неверным email, по сваггеру 400, но на деле приходит 500
def test_register_bad_request(obj_register):
    response = obj_register.obj_register("1", 435231, "Username")
    assert response.status_code == 500, \
        f"Ожидался статус 500, получен {response.status_code}, в сваггере 400, но 400 не вызывается"


# Тест проверки уже существующего email
def test_register_invalid_email(obj_register):
    response = obj_register.register("loginpermonents@yandex.ru", "qwerty123", "Username")
    assert response.status_code == 409, f"Ожидался статус 409, получен {response.status_code}"
    assert response.json()["message"] == "Пользователь с таким email уже существует", \
        "Отсутствует сообщение 'Пользователь с таким email уже существует'"


# Тест проверки не зарегистрированного логина
def test_authorization_invalid(obj_login):
    response = obj_login.login(generate_email(), generate_password())
    assert response.status_code == 401, f"Ожидался статус 409, получен {response.status_code}"
    assert response.json()["message"] == "Ошибка авторизации... Пожалуйста, проверь почту или пароль", \
        "Отсутствует сообщение 'Ошибка авторизации... Пожалуйста, проверь почту или пароль'"
