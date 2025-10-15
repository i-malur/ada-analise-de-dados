# conversão de tipos

numero1 = '19'
numero2 = '10'
print(numero1 + numero2) # concatenação

print(type(numero1)) # verificando o tipo da variável numero1

numero_int = int(numero1) # alterando o tipo de numero1 e armazenando em nova variável

print(numero_int, type(numero_int))

# int()
# str()
# float()
# bool()

altura = input("digite sua altura: ") # na função input() todo dado digitado por usuário é string
print(altura, type(altura))

idade = int(input("digite sua idade: ")) # aqui, já definimos automaticamente qual o tipo de dado que o usuário vai digitar e armazenar
print(idade, type(idade))

