# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 9 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Введите число: "))
fibonacci = []
for i in range(n):
    fibonacci.append(fib(i))

fibonacci_minus_index=list()
for i in range (n-1):
    if len(fibonacci_minus_index)%2==0:
        fibonacci_minus_index.append(-fibonacci[len(fibonacci)-i-1])
    else: 
        fibonacci_minus_index.append(fibonacci[len(fibonacci)-i-1])

result = fibonacci_minus_index+fibonacci
print(result)
