from utils.generation import generate_email, generate_username, generate_password
from config.credentials import EMAIL, PASSWORD, USERNAME


# Позитивные тесты

# Тест на авторизацию
def test_authorization(login_api):
    response = login_api.login(EMAIL, PASSWORD)

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert "token" in response.json(), "В ответе отсутствует поле «token»"


# Тест на регистрацию
def test_register(register_api):
    response = register_api.register(generate_email(), generate_password(), generate_username())

    assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
    assert response.json()["message"] == "Успешная регистрация!", "Отсутствует сообщение об успешной регистрации"


# Негативные тесты
# Тест на проверку авторизации с отсутствием логина
def test_login_empty_email(login_api):
    response = login_api.login("", PASSWORD)

    assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"


# Тест на проверку авторизации с отсутствием пароля
def test_login_empty_password(login_api):
    response = login_api.login(EMAIL, "")

    assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"


# Тест на проверку регистрации с неверным email, по сваггеру 400, но на деле приходит 500
def test_register_bad_request(register_api):
    response = register_api.register("1", 435231, "Username")

    assert response.status_code == 400, \
        f"Ожидался статус 400, получен {response.status_code}"


# Тест проверки уже существующего email
def test_register_invalid_email(register_api):
    response = register_api.register(EMAIL, PASSWORD, USERNAME)

    assert response.status_code == 409, f"Ожидался статус 409, получен {response.status_code}"
    assert response.json()["message"] == "Пользователь с таким email уже существует", \
        "Отсутствует сообщение 'Пользователь с таким email уже существует'"


# Тест проверки не зарегистрированного логина
def test_authorization_invalid(login_api):
    response = login_api.login(generate_email(), generate_password())

    assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
    assert response.json()["message"] == "Ошибка авторизации... Пожалуйста, проверь почту или пароль", \
        "Отсутствует сообщение 'Ошибка авторизации... Пожалуйста, проверь почту или пароль'"
