dias=int(input('Quantos dias alugados?'))
km=float(input('Quantos km rodados?'))
diaria= dias*60
percuso= km*0.15
custo= diaria+percuso
print('O total a pagar é de R${:.2f}'.format(custo))