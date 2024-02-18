# 16.A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

def fibonacci(n):
    fibonacci_series = [0, 1]
    while fibonacci_series[len(fibonacci_series)-1] < n:
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series

n = 500
fibonacci_series = fibonacci(n)
print("Série de Fibonacci até que o ultimo valor seja maior que 500:", fibonacci_series)