# Faca um program que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m*2
from email.errors import InvalidMultipartContentTransferEncodingDefect
from tkinter.tix import InputOnly


largura = float(input('Qual a largura da parede que você deseja pintar, em metros?'))
altura = float(input('Qual a altura da parede que você deseja pintar, em metros?'))
areaParede = altura * largura
tintaParede = areaParede / 2 # 1 litro por 2m*2

print(f'A quantia de tinta necessária para pintar a parede com a área de {areaParede}m*2 é de {tintaParede} litros')