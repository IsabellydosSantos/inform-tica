peso = float(input("Informe seu peso(em Kg): "))
altura = float(input("Informe sua altura(em m): "))

imc = peso / (altura**2)

imc = round(imc)

print("Seu IMC é igual a: ", imc)