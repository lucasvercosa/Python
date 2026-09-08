galera = []
dado = []
tomai=tomen=0
for c in range (0,3):
    dado.append(str(input('nome ')))
    dado.append(int(input('idade ')))
    galera.append(dado[:])
    dado.clear()
    print(galera)