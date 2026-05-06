print("-=-"*10)
print("Analisador de triângulos")
print("-=-"*10)
a=float(input("Primeiro segmento "))
b=float(input("Segundo segmento "))
c=float(input("terceiro segmento "))
if a<b+c and b<c+a and c<a+b
    print("Os segmentos acima podem formar um triângulo")
else:
    print("Os segmentos acima não podem formar um triângulo")