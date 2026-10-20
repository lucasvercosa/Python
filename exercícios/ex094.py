from datetime import datetime
dados = {}
dados ['nome'] = str(input("Digite seu nome: "))
nasc = int(input('Em qual ano você nasceu? '))
dados ['idade'] = datetime.now().year - nasc
dados ['ctps'] = int(input('Qual é o seu CTPS? '))
if dados ['ctps'] != 0:
    dados['contratação'] = int(input('ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = ((dados['contratação']+ 35) - datetime.now().year)
for k,v in dados.items():
    print(f'- {k} tem o valor {v}')