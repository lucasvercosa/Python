from math import hypot
catop=float(input("Cateto oposto: "))
catad=float(input("Cateeto adjacente: "))
hi=hypot(catop,catad)
print("A hipotenusa vai medir {}".format(hi))