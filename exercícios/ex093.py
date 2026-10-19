from random import randint
from operator import itemgetter
jogo = {'Jogador 1':randint (1,6),
        'Jogador 2':randint (1,6),
        'Jogador 3':randint (1,6),
        'Jogador 4':randint (1,6)
        }
ranking= []
print('valores sorteados')
for k,v in jogo.items ():
    print(f'{k} tirou {v} no dado')
ranking = 