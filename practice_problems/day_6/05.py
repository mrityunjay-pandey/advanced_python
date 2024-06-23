def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


n = 10
fib_gen = fibonacci_generator(n)
for num in fib_gen:
    print(num)
