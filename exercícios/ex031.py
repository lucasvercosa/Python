from random import randint
from time import sleep #FAZ ELE ESPERAR
aleatorio=randint(0,5)
print("Vou pensar em um número entre 0 e 5. Tente adivinhhar")
jogador=int(input('Em que número eu pensei'))
print("Processando...")
sleep(3) #ESPERA 3 SEGUNDOS
if aleatorio==jogador:
    print("Parabéns! Você conseguiu")
else:
    print("Ganhei eu pensei no número {} e não o {}".format(aleatorio,jogador))