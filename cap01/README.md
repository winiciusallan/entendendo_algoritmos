# Pesquisa Binária

A pesquisa binária, ou busca binária, é um algoritmo para encontrar um item em uma lista ordenada.
Ele funciona dividindo a busca pela metade na porção da lista onde o item supostamente está.
Vamos supor que queremos encontrar um nome em um dicionário com as 26 letras do alfabeto. Na busca linear, o algoritmo iria varrer, no pior dos casos,
as 26 letras até encontrar o nome de interesse. Na busca binária, o algoritmo no seu pior caso faria 5 varreduras.

## Descrição do Algoritmo
O algoritmo se baseia na divisão e conquista, por isso vai sempre dividindo a busca pela metade.

[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Primeiro, definimos a faixa inicial de busca que será o ponto baixo (início) e o ponto alto (fim) da lista. Depois, pegamos o elemento central e fazemos a verificação se o elemento
que queremos encontrar é menor ou maior. 

<pre>
[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ^              ^               ^
baixo          meio            alto
</pre>

Caso maior, redefinimos a faixa de busca. O novo ponto baixo será o meio + 1, o ponto alto permancerá e o novo meio será calculado fazendo a média.

<pre>
[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    ^     ^      ^
                  baixo  meio   alto    
</pre>

Caso menor, redefinomos a faixa de busca. O ponto baixo permanecerá, o ponto alto será o meio da lista - 1 e o novo meio será calculado.

<pre>
[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ^     ^     ^
baixo  meio  alto            
</pre>

A faixa de busca vai sendo redefinida até que o nosso elemento do meio seja igual ao que queremos encontrar.

## Exemplo de código
```Python
# Iterativo
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
```

Apesar da recursão ainda não ter sido apresentado no material, trouxe um exemplo para ficar mais claro que é possível fazer o mesmo algoritmo utilizando uma estratégia diferente. Se você quiser pular para o tópico que trata de recursão clique [aqui](./cap03)
```Python
# Recursivo
def busca_binaria_recursiva(lista, item, baixo, alto):
    meio = int((baixo + alto) / 2)

    if lista[meio] == item: 
        return meio
    if lista[meio] > item: 
        return binary_search_recursive(lista, item, baixo, meio - 1)
    if lista[meio] < item: 
        return binary_search_recursive(lista, item, meio + 1, alto)
```

## Análise assintótica
