import pytest
from main import calculate_discount, get_user_status

def test_calculate_discount_success():
    """Тестування успішного обчислення знижки."""
    assert calculate_discount(100, 20) == 80.0
    assert calculate_discount(250, 10) == 225.0
    assert calculate_discount(50, 0) == 50.0

def test_calculate_discount_exception():
    """Тестування винятків при неправильних даних знижки."""
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)
    with pytest.raises(ValueError):
        calculate_discount(100, 150)

@pytest.mark.parametrize("age, expected", [
    (5, "minor"),
    (17, "minor"),
    (18, "adult"),
    (30, "adult"),
    (64, "adult"),
    (65, "senior"),
    (80, "senior"),
])
def test_get_user_status(age, expected):
    """Тестування статусу користувача за віком (параметризований тест)."""
    assert get_user_status(age) == expected

def test_get_user_status_exception():
    """Тестування винятку для від'ємного віку."""
    with pytest.raises(ValueError):
        get_user_status(-5)