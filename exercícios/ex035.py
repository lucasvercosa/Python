n1=float(input("Digite o primeiro número "))
n2=float(input("Digite o segundo número "))
n3=float(input("digite o terceiro número "))
menor=n1
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n2
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
print("O maior valor digitado foi {}".format(maior))
print("O menor valor foi {}".format(menor))