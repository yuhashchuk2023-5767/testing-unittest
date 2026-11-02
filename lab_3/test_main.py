import pytest
from main import get_angles

def test_get_angles_triangle():
    """Тест для трикутника."""
    assert get_angles("triangle") == 3

def test_get_angles_rectangle():
    """Тест для прямокутника."""
    assert get_angles("rectangle") == 4

def test_get_angles_square():
    """Тест для квадрата."""
    assert get_angles("square") == 4

def test_get_angles_invalid():
    """Тест для перевірки викидання винятку для невідомої фігури."""
    with pytest.raises(ValueError):
        get_angles("circle")

def test_get_angles_without_assert():
    """
    Демонстрація того, що виклик функції без assert підвищує покриття коду,
    але не перевіряє правильність результату (тест-заглушка).
    """
    get_angles("triangle")  # Викликаємо, але не перевіряємо значення