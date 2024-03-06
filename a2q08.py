def main():
    entrada = input("Digite uma frase: ")
    print(remover_vogais(entrada))

def remover_vogais(frase:str):
    compara = ['a', 'e', 'i', 'o','u', 'A', 'E','I','O', 'U']
    saida = ''
    for i in range(len(frase)):
        if frase[i] not in compara:
            saida += frase[i]

    return saida

if __name__ == "__main__":
    main()