# dicionário

# criando o dicionario
dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Malur', 'idade': 19, 'altura': 1.60, 'peso': 60.1}

print(dicionario)
print(dicionario['idade']) # acessando itens

dicionario['graduação'] = 'ADS' # adicionando valores
print(dicionario)

dicionario['graduação'] = 'Análise e Desenvolvimento de Sistemas' # alterando valores
print(dicionario)

# imprimindo chave e valor do dicionario
for chave in dicionario:
    print(chave,":",dicionario[chave])
    
# testando existencia de chave
print("peso" in dicionario)