palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar',
            'trabalhador','mercado','programador','futuro')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end = '') #end não quebra linha e o \n quebra 
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')