# Este programa usa la función input para pedir al usuario
# las horas que trabaja y su tarifa de cobro, para luego calcular y mostrar
# el salario bruto del mismo.

horas = input("Cuantas horas trabajó?")
horas = float(horas)
tarifa = input("¿Cual es su tarifa de cobro por hora?")
tarifa = float(tarifa)
salario = horas * tarifa
print("Salario: ", salario)
