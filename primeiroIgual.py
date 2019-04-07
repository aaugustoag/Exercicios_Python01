def primeiroIgual (lista1, lista2):

    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                return i + 1
