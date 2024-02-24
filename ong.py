def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def productoria(lista):
    resultado = 1
    for elemento in lista:
        resultado *= elemento
    return resultado

def calcular(**kwargs):
    for key, value in kwargs.items():
        if 'fact' in key:
            print(f'El factorial de {value} es {factorial(value)}')
        elif 'prod' in key:
            print(f'La productoria de {value} es {productoria(value)}')

calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)