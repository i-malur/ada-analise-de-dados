# O que são variáveis
'''
Variáveis são espaços na memória do computador usados para armazenar dados que podem mudar durante a execução de um programa. Elas permitem que o programa guarde, manipule e recupere informações dinamicamente.
Cada variável tem:
    Um nome (identificador, usado para acessar o valor);
    Um tipo (define o tipo de dado que pode guardar, como inteiro, real, caractere, etc.);
    Um valor (a informação armazenada).
    
Uma variável é como uma caixa com uma etiqueta: o nome da variável é a etiqueta, e o valor guardado é o que está dentro da caixa. Você pode abrir a caixa para ver o que tem, trocar o conteúdo ou colocar algo novo.
'''
# tipos de variáveis em python
'''
Numéricos: int (inteiro), float (reais ou decimais), complex (complexo: Representa números complexos, com uma parte real e uma parte imaginária (sufixo j). Exemplo: z = 3 + 4j)
Textual: String 
Booleano: False ou True
Coleções:
    Lista (list): É uma coleção ordenada e mutável (pode ser alterada) de itens. É definida por colchetes []. Exemplo: frutas = ["maçã", "banana", "uva"]
    Tupla (tuple):  É uma coleção ordenada e imutável (não pode ser alterada) de itens. É definida por parênteses ()
    Dicionário (dict): É uma coleção não ordenada de pares de chave:valor. As chaves devem ser únicas e imutáveis. É definido por chaves {}. Exemplo: pessoa = {"nome": "João", "idade": 25}
    Conjunto (set): : É uma coleção não ordenada e mutável de itens únicos (não permite duplicatas). É definido por chaves {}. Exemplo: numeros_primos = {2, 3, 5, 7} 
type(): função para ver os tipos de dados das variáveis
'''

# Estrutura da variável
# identificador=valor -> o que está do lado direito será atribuido ao identificador do lado esquerdo

idade = 19
nome = "Malu"
estudante = True
altura = 1.60

print('nome:', nome,',','idade:',idade,',','altura:',altura,',','estudando?',estudante)
print(type(nome))
print(type(altura))
print(type(idade))
print(type(estudante))