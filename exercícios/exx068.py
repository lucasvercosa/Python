n = c = s = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    c += 1
    s += n
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores foi {s}!')