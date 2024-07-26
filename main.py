import calendar
from calendario import Calendario
from escala import Funcionario



nome = input('Digite o nome do funcionário: ')
ano = int(input('Digite o ano: '))
mes_folga = int(input('Digite o mês: '))
ultimo_dia_folga = int(input('Digite o último dia de folga do funcionário: '))

funcionario = Funcionario(nome, ultimo_dia_folga)
gerador = Calendario(ano, mes_folga, funcionario.ultima_folga)
