# Etapas do algoritmo
# entrada - processamento - saída

nome = input("Qual seu nome? ")
genero = input("Qual seu gênero? (f - feminino, m - masculino, o - outro) ")

if (genero == "f"):
    print("bem vinda, ", nome)
elif(genero == "m"):
    print("bem vindo, ", nome)
else:
    print("bem vinde, ", nome)
