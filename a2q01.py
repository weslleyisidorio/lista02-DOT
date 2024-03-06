def main():

    entrada = int(input("Digite um numero: "))
    numerosPrimosGemeos = retornaGemeos(entrada)
    print(numerosPrimosGemeos)

def ehPrimo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False

    return True

def retornaGemeos(entrada):
    saida = []
    for i in range(2, entrada):
        if ehPrimo(i) and ehPrimo(i+2):
            saida.append(i)

    return saida
       
        

if __name__ == "__main__":
    main()