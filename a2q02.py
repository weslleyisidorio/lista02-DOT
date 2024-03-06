def main():
    string1 = input("Digite uma palavra ou frase: ").lower().strip()
    string2 = input("Digite outra palavra ou frase: ").lower().strip()

    print(verificar_anagrama(string1, string2))

def verificar_anagrama(string1, string2):
    flag = False

    if (len(string1) == len(string2)):
        ord1 = sorted(string1)
        ord2 = sorted(string2)
        if ord1 == ord2:
            flag = True
    
    return flag
  

if __name__ == '__main__':
    main()