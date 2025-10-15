# listas

# criando listas 
lista = []
lista = list()

# adicionado itens na lista
lista_int = [1, 2, 5, -1] #inteiro
lista_float = [1.5, 6.8, 9.0, -9.8] #float
lista_string = ["malu", "caras", "sapatos"] #string
lista_diversos = [1, 4.5, "malu", False, lista_int] #podemos criar listas com valores de diferentes tipos e podemos adicionar outras listas dentro da lista

# cada item da lista tem seu index. toda lista começa com intex 0
# lista_diversos = [1(index 0), 4.5(index 1), "malu"(index 2), False(index 3), lista_int(index 4)]

print(lista_diversos[2]) # imprimindo conteúdo de index 2 "malu"

#quando bucamos valores do final da lista, usamos os valores negativos, -1 é o ultimo valor da lista e assim por diante
# lista_diversos = [1(index -5), 4.5(index -4), "malu"(index -3), False(index -2), lista_int(index -1)]
print(lista_diversos[-5]) # imprimindo penultimo elemeno da lista

#quando queremos imprimir valores em um intervalo da lista -1 (o útlimo elemento não é selecionado, então, devemos colocar 1 index a mais)
print(lista_diversos[2:5])

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23]
print(lista_numeros[1:7:2]) #imprimindo intervalo de lista de 2 em 2 itens, ou seja, entre index 2 a 6 (lembrando que devemos colocar 1 index a mais no final) serão impressos os npumeros de 2 em 2
print(len(lista_numeros)) # verificando o tamanho da lista (quantos elementos tem)

# métodos e funções
numeros = [34, 79, 90, 100, 134, 67, 899]
print("Lista bruta: ", numeros)

# append() - adicionando dados ao final da lista
numeros.append(3556)
print("novo item adicionado: ", numeros)

# insert() - adicionando dados na lista a partir da posição desejada
numeros.insert(2, 10)
print("novo item adicionado no indice 2: ", numeros)

# pop() - remover elementos da lista a partir do index desejadou (caso não tenha index informado), o último item
numeros.pop()
print("último item removido: ", numeros)

numeros.pop(0)
print("item removido a partir de um index passado: ", numeros)

# remove() - remove o valor informado da lista. caso tenha a repetição desse valor, ele remove o primeiro que encontrar
numeros.remove(100)
print("valor excluido da lista: ", numeros)

# count() -> quantidade de vezes que o valor aparece na lista
print("quantidade de 10 na lista:", numeros.count(10)) 

# index() -> para verfocar qual indice do valor
print("indica do valor 10: ", numeros.index(10))

# sort() -> ordenar lista de forma crescente
numeros.sort()
print("ordem crescente: ", numeros)
numeros.sort(reverse=True)
print("ordem decrescente: ", numeros)


# funções

# len() -> tamanho da lista
print("tamanho da lista: ", len(numeros))

# sum() -> soma dos itens da lista
print("soma da lista: ", sum(numeros))

# max() -> número maior
print("maior número: ", max(numeros))

# min() -> número menor
print("menor número: ", min(numeros))
'''
POO BÁSICO
Classe => O molde ou planta de um objeto. Define as características e comportamentos.	
Objeto => A coisa concreta criada a partir de uma Classe.	
Método => Uma Função que pertence e atua sobre um Objeto.	
Função => Um bloco de código autônomo que executa uma tarefa.
'''