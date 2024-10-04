def sum(a, b):
    """función que suma"""
    resultado = a + b
    return (resultado)


def mul(a, b):
    """función que multiplica"""
    resultado = a * b
    return (resultado)

# programa principal -main-

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'    suma de {a} y {b} : {sum(a, b)}')
print(f'producto de {a} y {b} : {mul(a, b)}')

