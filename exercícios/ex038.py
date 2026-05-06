salario=float(input("Salário do comprador: R$ "))
financiamento=float(input("Quantos anos de financiamento? "))
casa=float(input("Qual é o valor da casa? "))
prestacao=casa/(financiamento*12)
if prestacao <=  salario*0.3:
    print("Para pagar uma casa de {} em {} anos a prestação será de R${:.2f} é suficiente. Emprestimo aprovado".format(casa,financiamento,prestacao))
elif prestacao > salario*0.3:
    print("Para pagar uma casa de {} em {} anos a prestação será de R${:.2f} é muito pouco. Emprestimo negado".format(casa,financiamento,prestacao))