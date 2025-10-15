# while
'''
import random
numero_sorteado = random.randint(1, 20)
numero_usuario = int(input("Digite um número de 1 a 20: (0 para sair): "))
tentativas = 1

while(numero_usuario != 0 and tentativas < 5):
    if(numero_usuario != numero_sorteado):
        print("Você errou, tente novamente!")
        numero_usuario = int(input("Digite um número de 1 a 10: (0 para sair): "))
        tentativas+= 1
        if tentativas == 5:
            print("Acabou as tentativas!")
    else:
        print("Parabéns!!")
        break
'''
# for - looping que usamos quando sabemos que tem um final

# começa em 0 e vai até 9
'''for variavel in range(10):
    print('\n', variavel)'''
    
# começa em 1 e vai até menor que 10 (9)
'''for variavel1 in range(1, 10):
    print('\n', variavel1)'''

# começa em 1 e vai até menor que 11 (10)
'''for variavel2 in range(1, 11):
    print('\n', variavel2)'''

# começa em 1 e vai até menor que 11 (10) de 2 em 2 números
'''for variavel in range(1, 11, 2):
    print('\n',variavel)'''


# range(valor inicial, valor final -1, passo do laço (de 2 em 2, 3 em 3 e etc..))
lista_notas = [] # criando lista para armazenar notas
media = 0
for i in range(1, 4):
    notas = float(input(f"digite a nota {i}: ")) #injetando variável i para mostrar qual nota deve ser digitado
    lista_notas.append(notas) 
    media += notas
    
print("Lista de noatas:", lista_notas)
print("média das notas:", media/3)

'''

As estruturas de repetição for e while são fundamentais na programação e servem, essencialmente, para a mesma coisa: executar um bloco de código repetidas vezes. A principal diferença entre elas está na intenção e na sintaxe, o que define quando é melhor usar uma ou outra.

Diferença Principal: Certeza do Número de Repetições
A melhor forma de decidir entre for e while é pensando se você sabe ou não de antemão quantas vezes o código precisa se repetir.

Estrutura	Propósito Principal	Quando Usar
for	=> Usado quando você sabe o número exato de iterações. Exemplo: contar até um número específico, percorrer todos os elementos de uma lista (Array), ou iterar sobre um intervalo definido.
while => Usado quando você não sabe o número exato de iterações. Exemplo: repetir até que uma condição externa seja satisfeita, como esperar uma entrada válida do usuário ou processar dados de um arquivo.

'''