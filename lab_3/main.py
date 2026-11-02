"""
Модуль для демонстрації покриття коду та розгалужень (Code & Branch Coverage).
"""

def get_angles(shape_type: str) -> int:
    """Повертає кількість кутів для заданої фігури."""
    if shape_type == "triangle":
        return 3
    elif shape_type == "rectangle":
        return 4
    elif shape_type == "square":
        return 4
    else:
        raise ValueError(f"Невідома фігура: {shape_type}")
    