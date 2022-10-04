#Вычислить число c заданной точностью d
from math import pi


d = int(input('Задайте точность d :\n'))
res = round(pi, d)
print('Число ПИ с заданной точностью', d, 'равно', res)