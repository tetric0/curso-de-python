# Generador de números impares
def odd_numbers_generator (start, limit):
    if start%2 == 0:
        start += 1

    while start < limit:
        yield start
        start += 2

for num in odd_numbers_generator(5, 15):
    print(num)

# Generador de números impares
def even_numbers_generator (start, limit):
    if start%2 != 0:
        start += 1

    while start < limit:
        yield start
        start += 2

for num in even_numbers_generator(5, 15):
    print(num)