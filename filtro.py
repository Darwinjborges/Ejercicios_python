import sys

def filtrar_productos(umbral, operacion='mayor'):
    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }

    if operacion == 'mayor':
        resultado = {producto: precio for producto, precio in precios.items() if precio > umbral}
        print("Los productos mayores al umbral son: ", ', '.join(resultado.keys()))
    elif operacion == 'menor':
        resultado = {producto: precio for producto, precio in precios.items() if precio < umbral}
        print("Los productos menores al umbral son: ", ', '.join(resultado.keys()))
    else:
        print("Lo sentimos, no es una operación válida")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filtrar_productos(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        filtrar_productos(int(sys.argv[1]), sys.argv[2])
    else:
        print("Uso: python filtro.py <umbral> [mayor|menor]")
