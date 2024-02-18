# 15.A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

def fibonacci(n):
    fibonacci_series = [1, 1]
    while len(fibonacci_series) < n:
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series

# Gerando a série até o nono termo
n = 90
fibonacci_series = fibonacci(n)
print("Série de Fibonacci até o nono termo:", fibonacci_series)