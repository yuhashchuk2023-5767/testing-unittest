"""
Модуль містить базові математичні та рядкові функції для тестування.
"""

def add(a, b):
    """Повертає суму двох чисел."""
    return a + b

def subtract(a, b):
    """Повертає різницю двох чисел."""
    return a - b

def multiply(a, b):
    """Повертає добуток двох чисел."""
    return a * b

def divide(a, b):
    """Повертає частку двох чисел. Викликає ValueError при діленні на нуль."""
    if b == 0:
        raise ValueError("Ділення на нуль неможливе!")
    return a / b

def is_palindrome(text: str) -> bool:
    """Перевіряє, чи є рядок паліндромом (без урахування регістру та пробілів)."""
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]