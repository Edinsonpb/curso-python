a = 0
b = 0
c = 0
porcentaje = 0.25

x = float(input("digite el valor de la nota 1: ")) * porcentaje
y = float(input("digite el valor de la nota 2: ")) * porcentaje
z = float(input("digite el valor de la nota 3: ")) * porcentaje

esperada = float(input("digite la nota esperada al fiinal del periodo: "))
acumulada = x + y + z
minima = (esperada - acumulada) / porcentaje

if minima > 5.0:
    print("con las notas dadas la nota de la calificacion final supera el 5.0 
    por lo tanto no ess posible alcanzar la nota esperada")
else:
    minima = str(minima)
    print("ud necesita obtener : " + minima + " en su ultima calificacion")