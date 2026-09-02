#exemplo 1
teste = []
teste.append('Gustavo')
teste.append(30)
galera = []
#galera.append(teste)
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
#galera.append(teste) muda a lista de cima pois eu estou ligando as listas
galera.append(teste[:]) #agora ele ta fazendo uma copia e não ligando as listas
print(teste)
print(galera)