#Exemplo 1

c = 1
while c < 10:
    print (c)
    c += 1
print('fim') # O while pode ser usado quando sabemos ou não o limite

#Exemplo 2

n = 1
while n != 0:
    n = int(input("Digite um valor: "))
print("Fim")

#Exemplo 3

r = "sim"
while r == "sim":
    n = int(input("Digite um valor "))
    r = str(input("Quer continuar [sim/não]? "))
    lower()
print("Fim")

#Exemplo 4

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor '))
    if n!=0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou tantos números pares {par} e tantos números impares {impar}')