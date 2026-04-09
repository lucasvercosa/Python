frase = " curso e análise de desenvolvimento de sistemas "
print(frase [3]) #isso mostra o espaço da memória 

print(frase [3:17])#intervalo

print(frase [3:17:2])# essa parte pula de 2 em 2

print(frase [:4])# pega do início até o que vc escolheu

print(frase [4:])#pega do que vc escolheu até o final

print(frase [20::2])

print(len(frase))#conta os espaços

print(frase.count("a"))# procura a letra específica

print(frase.count ("e", 2,5))

print(frase.find("urs"))#find = a partir de qual espaço começa

print(frase.find("android"))# -1 n existe essa sequência

print("opa" in frase)# verifica se esta na variável

print(frase.replace("curso", "aulas")) #troca a palavra 

print(frase)

print(frase.upper())# deixa em maiúsculo

print(frase.lower())# minúsculo

print(frase.capitalize())# primeira letra da 1 palavra em maiúsculo

print(frase.title())# todas as primeiras letras em maiúsculo

print(frase.strip())# tira o espaço em branco 

print(frase.rstrip())# tira o espaço em branco da direita

print(frase.lstrip())#tira o espaço em branco da esquerda

print(frase.split())# transformar o valor da variável em lista 

print("@".join
      (frase))#une um símbolo 