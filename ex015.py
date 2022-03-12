# Aluguel de carro + kmetragem = preco total do aluguel
dias = int(input('Quantos dias de aluguel?'))
kms = int(input('Quantos Kms rodados?'))
total = (dias*60)+(kms*.15)
print(f'O valor final é de {(total):.2f} reais')