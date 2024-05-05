def caching_fibonacci():
    cache = {}  # Порожній словник для кешування результатів обчислення

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # Перевірка, чи є результат в кеші
            return cache[n]
        else:
            # Рекурсивне обчислення та зберігання результату в кеші
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci з кешуванням
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
