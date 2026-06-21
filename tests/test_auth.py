# Тест на авторизацию
def test_authorization(obj_authorization):
    assert obj_authorization.status_code == 200


# Тест на регистрацию
def test_register(obj_random_register):
    assert obj_random_register.status_code == 201
