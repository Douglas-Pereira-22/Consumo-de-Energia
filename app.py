aparelho = input('Digite qual o nome do aparelho: ')
watts = int (input('Qual a potência em watts?: '))
hrs = int(input('Quantos horas de uso?: '))

consumoMensal = (watts * hrs * 30) / 1000
valor = consumoMensal * 0.87
print(f'O consumo mensal é {consumoMensal} KWH/mês aproximadamente.')
print(f'O valor do consumo será aproximadamente R${valor}.')