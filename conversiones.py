import sys

def convertir_divisas(tasa_sol, tasa_peso_arg, tasa_dolar, valor):
    sol = valor * tasa_sol
    peso_arg = valor * tasa_peso_arg
    dolar = valor * tasa_dolar
    return sol, peso_arg, dolar

def main():
    tasa_sol = float(sys.argv[1])
    tasa_peso_arg = float(sys.argv[2])
    tasa_dolar = float(sys.argv[3])
    valor = float(sys.argv[4])

    sol, peso_arg, dolar = convertir_divisas(tasa_sol, tasa_peso_arg, tasa_dolar, valor)

    print(f"Los {valor} pesos equivalen a:")
    print(f"{sol} Soles")
    print(f"{peso_arg} Pesos Argentinos")
    print(f"{dolar} Dólares")

if __name__ == "__main__":
    main()