num = [2,5,9,1]
num [2] = 3 #pode modificar a lista
# num [4] = 7 vai dar erro porque não tem esse índice na lista
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2,0) #adiciona na posição 2 o valor de zero empurrando os outros elementos
num.insert(2,2) #adiciona na posição 2 o valor de zero empurrando os outros elementos
num.remove(2) #remove a primeira ocorrência 
num.remove(3) #da erro pois não existe o número 4
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
num.pop(2) #Elimina o lemento 2
print(num)
print(f'Essa lista tem {len(num)} elementos')