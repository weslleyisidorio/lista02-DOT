def main():
    string = input("Digite uma palavra ou frase: ").lower().strip()
    print(contar_caracteres(string))

def contar_caracteres(string:str):
    dici = {}
    for i in range(len(string)):
        if string[i] not in dici:
            add = string[i]
            dici[add] = 1
        else:
            dici[string[i]] += 1

    return dici

if __name__ == "__main__":
    main()