matriz = [[0,0,0,],[0,0,0],[0,0,0]]
for L in range (0,3):
    for C in range (0,3):
     matriz [L][C] = int(input(f'Digite um valor para [{L},{C}]: '))
for L in range (0,3):
    for C in range (0,3):
        print(f'[{matriz[L][C]}]',end='')
    print()