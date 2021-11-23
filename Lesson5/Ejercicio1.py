# Este programa usa la función input para pedir al usuario
# las horas que trabaja y su tarifa de cobro. Luego, usa y la nueva función
# "calculo_salario" para calcular y mostrar el salario bruto del mismo.
# Le paga 1,5 veces la tarifa por cada hora por encima de 40 horas
# (horas extra). Try-except se usan para advertir al usuario cuando provee
# la información de forma incorrecta.

# FUNCIONES ----
def calculo_salario(horas, tarifa):
    try:
        if horas > 40:
            horas_extra = horas - 40
            print("Usted trabajó ", horas_extra, "horas extra")
            salario = 40 * tarifa + horas_extra * (tarifa * 1.5)
            print("Su salario corresponde a: ", salario)
        else:
            print("Usted no trabajó horas exta")
            salario = horas * tarifa
            print("Su salario corresponde a: ", salario)

    except Exception as e:
        print("Error, escriba un número")

# PROGRAMA ----
horas = input("Cuantas horas trabajó?")
horas = float(horas)
tarifa = input("¿Cual es su tarifa de cobro por hora?")
tarifa = float(tarifa)

calculo_salario(horas, tarifa)
