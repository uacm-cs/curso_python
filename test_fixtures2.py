import pytest

def get_user_info(user_id):

    # Estos datos generalmente provienen de la Base de Datos o de una API
    if user_id == 1:
        return {'name': 'Luisa', 'age': 30}
    elif user_id == 2:
        return {'name': 'Pedro', 'age': 40}
    elif user_id == 3:
        return {'name': 'Juan', 'age': 50}
    else:
        return None

@pytest.mark.parametrize("user_id, expected_name, expected_age", [
    (1, 'Luisa', 30),
    (2, 'Pedro', 40),
    (3, 'Juan', 50),
    (4, None, None),
])
def test_get_user_info(user_id, expected_name, expected_age):
    user_info = get_user_info(user_id)
    if user_info is None:
        assert user_info == expected_name
    else:
        assert user_info['name'] == expected_name
        assert user_info['age'] == expected_age