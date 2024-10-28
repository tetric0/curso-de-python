# PROBAR DIFERENTES NÚMEROS
num = 4

# EJEMPLO DE FUNCIÓN RECIRSIVA (2): FIBONACCI
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial (n-1)

print("El factorial de {} es: {}".format(num, factorial(num)))


# EJEMPLO DE FUNCIÓN RECIRSIVA (2): FIBONACCI
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("La serie de Fibonacci para el número {} es: {}".format(num, fibonacci(num)))


# RETO CLASE 21
def sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria(n-1)


print("La sumatoria de {} es: {}".format(num, sumatoria(num)))