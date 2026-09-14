galera = []
dado = []
tomai = tomen = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    # galera.append(dado) assim vai apagar as duas listas porque estão conectadas
    dado.clear()
print(galera)
for p in galera:
    if p[1] >=18:
        print(f'{p[0]} é o maior de idade')
        tomai += 1
    else:
        print(f'{p[0]} é menor de idade')
        tomen += 1
print(f'Temos {tomai} maiores de idade e {tomen} menores de idade')