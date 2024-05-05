from typing import Callable
import re

def generator_numbers(text: str):
    # Використовуємо регулярний вираз для пошуку дійсних чисел у тексті
    pattern = r"\b[-+]?\d+\.\d+\b"
    # Знаходимо всі дійсні числа у тексті
    numbers = re.findall(pattern, text)
    # Повертаємо генератор
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    # Викликаємо передану функцію для отримання генератора дійсних чисел
    numbers_generator = func(text)
    # Обчислюємо загальну суму чисел
    total_sum = sum(numbers_generator)
    return total_sum

# Приклад використання
text = '''Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, 
доповнений додатковими надходженнями 27.45 і 324.00 доларів.'''
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
