valor = int(input("Digite um número inteiro: "))
soma = 0
while valor != 0:
    soma = soma + (valor % 10)
    valor = valor // 10

print(soma)
