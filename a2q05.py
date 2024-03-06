def main():
    try:
        ano = int(input("Digite um ano: "))
    except:
        print("Entrada inválida!")
        exit()

    print(anoBissexto(ano))

    
def anoBissexto(ano:int):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 400 ==0):
        return True
    return False

if __name__== '__main__':
    main()