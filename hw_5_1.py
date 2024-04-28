def caching_fibonacci():
    # кеш для зберігання обчисленних значень чисел фібоначі
    cache = {}

    def fibonacci(n):
        # базові випадкі для чисел фібоначі
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # перевірка чи число вже зберігається у кеші
        if n in cache:
            return cache[n]

        # рекурсивне обчислення числа фібоначі
        # обчислення збереженних чисел фібоначі для уникнення зайвих обчислень 
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # повернення внутрішньої функціі фібоначі
    return fibonacci

# створення екзепляра функціі caching_fibonacci
fib = caching_fibonacci()

# виклик функціі для обчислення числа 10 фібоначі
print(fib(10)) 
