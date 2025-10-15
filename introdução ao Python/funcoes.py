# Funções

def saudacao():
    print("Bem vindo(a/e)!")


# funções com parametros
def saudacao(nome, curso):
    print(f"Bem vindo(a/e), {nome}! Aproveite o curso de {curso}!".format(nome, curso))

saudacao("malu", "Dados com Python")
saudacao("luiz", "JavaScript")

# funções com parametros defaut
def saudacao(nome, curso="Python"):
    print(f"Bem vindo(a/e), {nome}! Aproveite o curso de {curso}!".format(nome, curso))

saudacao("malu")
saudacao("luiz", "C++")

# funções com retorno
def soma(numero1, numero2):
    return numero1 + numero2 # retorna e encerra

print("resultado da soma: ", soma(90, 100))

def calculadora(num1, num2, operacao="+"):
    match operacao:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2

num1 = float(input("digite número 1: "))
num2 = float(input("digite número 2: "))
operacao = input("digite operador: +(soma), -(subtração), *(multiplicação), /(divisão) ")
print("resultado da operação: ", calculadora(num1, num2))

num1 = float(input("digite número 1: "))
num2 = float(input("digite número 2: "))
operacao = input("digite operador: +(soma), -(subtração), *(multiplicação), /(divisão) ")
print("resultado da operação: ", calculadora(num1, num2, operacao))