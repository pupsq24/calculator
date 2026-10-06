def add_numbers(a: float, b: float) -> float:
    """Сложить два числа и вернуть результат."""
    return a + b


def divide(a: float, b: float) -> float:
    """Разделить a на b. Вызывает ValueError при b=0."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b