largura=float(input('Largura da parede'))
altura=float(input('Altura da parede'))
area=largura*altura
print('sua parede tem a dimensão{}x{} e sua área é de {}m quadrados;'.format(largura,altura,largura*altura))
print('para pintar essa parede, você precisa de {}L de tinta'.format(area/2))