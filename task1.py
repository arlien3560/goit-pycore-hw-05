def caching_fibonacci():
    # Словник для кешування результатів
    cache = {}
    
    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]
    
    return fibonacci

if __name__ == "__main__":
    fib = caching_fibonacci()
    
    print(fib(10))
    print(fib(15))
    
    # Додаткові тести
    print(fib(0))
    print(fib(1))
    print(fib(5))
    print(fib(20))