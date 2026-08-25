valores = []
for cont in range (0,5):
    valores.append(int(input('Digite um valor ')))
for c,v in enumerate (valores): #mostra o índice e os valores
    print(f'Eu achei na posição {c} o valor de {v}')


A = [2,3,4,7]
# B = [4,5,6,7]
# B = A
B = A [:]
B [2] = 8
print(f'Lista A {A}')
print(f'Lista B {B}')