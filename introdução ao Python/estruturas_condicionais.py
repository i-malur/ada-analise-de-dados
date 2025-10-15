# estruturas condicionais -> if - elif - else

idade = int(input("Qual é sua idade? "))

if(idade >= 18 and idade < 60):
    print("Adulto")
elif(idade >= 12 and idade < 18):
    print("Adolecente")
elif(idade >= 60):
    print("Idoso")
else:
    print("Criança")