import math

a = float(input("Введите первую сторону треугольника, см: "))
b = float(input("Введите вторую сторону треугольника, см: "))
c = float(input("Введите третью сторону треугольника, см: "))

p = (a+b+c)/2

cos_a = (b*b + c*c - a*a)/(2*b*c)
sin_a = math.sqrt(1-cos_a*cos_a)
tan_a = sin_a/cos_a

A = math.atan(tan_a)

r = (p-a)*math.tan(A/2)

S = round(math.pi*r*r, 2)

print("Площадь круга, вписанного в треугольник, равна", S,"см2")
