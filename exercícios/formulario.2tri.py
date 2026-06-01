from random import randint
from time import sleep
print('''Suas opções
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
jogada = int(input("Qual é a sua jogada? "))
jogadapc = randint(0,2)
itens = ("Pedra", "Papel", "Tesoura")
print("jo")
sleep(1)
print("ken")
sleep(1)
print("po !!!")
sleep(1)
print("-=-" * 10)
print(f'''computador jogou {itens[jogadapc]}
      jogador jogou {itens[jogada]}''')
print("-=-" * 10)
if jogadapc == 0 and jogada == 1 or jogadapc == 1 and jogada == 0 or jogadapc == 2 and jogada == 2:
    print("Computador vence")
elif jogada == 1 and jogadapc == 2 or jogada == 0 and jogadapc == 2 or jogada == 1 and jogadapc == 0:
    print("Jogador vence")
else:
    print("empate")



print("="*11+"LOJAS LV"+"="*11)
preco = float(input("Preço das compras: "))
print('''FORMAS DE PAGAMENTO
      [1] à vista dinheiro/cheque
      [2] à vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
pagamento = int(input("Qual é a opção? "))
if pagamento == 1:
    desconto = preco - (preco*0.15)
    print("Sua compra com desconto a vista fica R${:.2f}".format(desconto))
elif pagamento == 2:
    desconto = preco - (preco*0.08)
    print("Sua compra no cartão fica R${:.2f}".format(desconto))
elif pagamento == 3:
    cartao = preco/2
    print("Sua compra parcelada no cartão fica 2x de {:.2f}".format(cartao))
elif pagamento == 4:
    parcela = int(input("Digite o número de parcelas: "))
    juros = preco + (preco*0.25)
    total= juros/parcela
    print("A sua compra no cartão vai ser feita em {} parcelas. O valor de cada parcela fica R${:.2f} e o total com juros é R${:.2f}".format(parcela, total_parcela, juros))              
else:
    print("Opção inválida de pagamento. Tente novamente.")