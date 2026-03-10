nome=input('Qual é o seu nome?')
print('prazer em conhece-lo{:20}!'.format(nome))
print('prazer em conhece-lo{:>20}!'.format(nome)) #Direita
print('prazer em conhece-lo{:<20}!'.format(nome)) #Esquerda
print('prazer em conhece-lo{:^20}!'.format(nome)) #Centro

nome=int(input('Digite um valor'))
outro=int(input('Digite outro valor'))
soma=(nome+outro) #Criar a variavel quando utiliza outra parte do codigo
print('A soma é {}'.format(soma))