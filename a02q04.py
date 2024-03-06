def main():
    try:
        entrada = int(input('Digite um número: '))
    except:
        print("Entrada inválida!")
        exit()

    print(f'{entrada} é divisivel {contar_divisores(entrada)} vezes.')

    

def contar_divisores(numero: int):
    cont = 0
    for i in range(2,numero):
        if numero % i == 0:
            cont += 1
    return cont

if __name__ == "__main__":
    main()