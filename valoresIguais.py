def valoresIguais (lista1, lista2):

    lista = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                lista.append(lista1[i])
    return lista

