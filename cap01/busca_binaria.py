def busca_binaria(lista, item):
    # Ponto baixo da lista.
    baixo = 0 
    # Ponto alto da lista.
    alto = len(lista) - 1 

    while baixo <= alto:
        meio = len(lista) / 2

        # Chute do provável número
        chute = lista[meio] 
    
        if chute == item: return meio
        if chute > item:
            alto = meio - 1
        if chute < item:
            baixo = meio + 1

    # Retorna none caso o elemento não esteja na lista.
    return None
