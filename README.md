# Consumo-de-Energia
#App: Calculo de consumo de energia
#Linguagem : Python
#Formula usada : consumoMensal = (potencia * horasDia * 30) / 1000
#Intruções : 1° digite o nome do aparelho, 2° digite a potência em Watts, 3° digite quantas hrs de uso do aparelho. Depois disso o App irá mostrar o resultado. 

aparelho = input('Digite qual o nome do aparelho: ')
watts = int (input('Qual a potência em watts?: '))
hrs = int(input('Quantos horas de uso?: '))

consumoMensal = (watts * hrs * 30) / 1000
valor = consumoMensal * 0.87
print(f'O consumo mensal é {consumoMensal} KWH/mês aproximadamente.')
print(f'O valor do consumo será aproximadamente R${valor}.')
