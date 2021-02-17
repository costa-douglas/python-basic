import random

perdeu = False
continuar = True

soma = 0
cont = 1

while not perdeu and continuar:
    carta = random.randint(1, 10)
    soma = soma + carta

    print('{} a carta, pontuação: {}'.format(cont, soma))

    if soma > 21:
        perdeu = True
    else:
        resposta = input('Mais um carta ? ')
        if resposta == 'não' or resposta == 'NÃO':
            continuar = False
        else:
            cont = cont + 1

if perdeu:
    print('Você perdeu')
if soma == 21:
    print('Black Jack')
else:
    print('Você tem {} pontos'.format(soma, 21-soma))
