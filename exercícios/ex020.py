import math
ang=float(input("Digite o ângulo que deseja"))
seno=math.sin(math.radians(ang)) #Os valores tem que ser em radianos então usamos o math.radians
cose=math.cos(math.radians(ang))
tang=math.tan(math.radians(ang))
print("O ângulo de {} tem seno de {:.2f}".format(ang,seno))
print("O ângulo de {} tem coseno de {:.2f}".format(ang,cose))
print("O ângulo de {} tem tângente de {:.2f}".format(ang,tang))