def main():
    print(econtrar_elementro_faltante([1,3,4,5,6]))

def econtrar_elementro_faltante(lista:list):
    listaOrdenada = sorted(lista)

    faltante = -1

    for i in range(len(lista)):
        if i+1  != listaOrdenada[i]:
            faltante = i+1
            break

    return  faltante

if __name__ == "__main__":
    main()