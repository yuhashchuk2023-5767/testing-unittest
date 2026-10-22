"""
Модуль для демонстрації тестування за допомогою pytest.
"""

def calculate_discount(price: float, discount_percent: float) -> float:
    """Обчислює ціну зі знижкою. Викликає ValueError при некоректних даних."""
    if price < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError("Некоректні вхідні дані для ціни або знижки!")
    return round(price * (1 - discount_percent / 100), 2)

def get_user_status(age: int) -> str:
    """Повертає статус користувача залежно від віку."""
    if age < 0:
        raise ValueError("Вік не може бути від'ємним!")
    elif age < 18:
        return "minor"
    elif age < 65:
        return "adult"
    else:
        return "senior"