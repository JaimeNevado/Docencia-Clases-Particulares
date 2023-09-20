def fibonacci(n):
    # Recursiva
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

'''
def sumar_fibo(n):
    i = 0
    total = 0
    while i < n:
        total = total + fibonacci(i)
        i += 1
    return total


print(sumar_fibo(4))

'''

print(fibonacci(3))