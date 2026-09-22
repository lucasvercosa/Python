matriz = [[0,0,0],[0,0,0],[0,0,0]]
total3 = maior = somapar = 0
for L in range (0,3):
    for C in range (0,3):
       matriz [L][C] = int(input(f'Digite um valor para [{L}, {C}]: '))
       if matriz [L][C] % 2 == 0:
          somapar += matriz [L][C]
       if C == 2:
          total3 += matriz [L][C]
       if L == 1 and C == 0:
          maior = matriz [L][C]
       elif L == 1 and C !=0 and matriz[L][C]> maior:
            maior = matriz [L][C]
for L in range(0,3):
    for C in range(0,3):
        print(f'[{matriz[L][C]}]', end='')
        print()
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos números da terceira coluna é igual a {total3}')
print(f'O maior valor da da linha 2 é {maior}')