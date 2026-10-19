aluno = {}
aluno ['nome'] = str(input('Qual é o seu nome '))
aluno ['media'] = float(input('Qual é a sua média '))
if aluno ['média'] >= 6.0:
    aluno ['situação'] = 'Aprovado'
else:
    aluno ['situação'] = 'Reprovado'
print(aluno)