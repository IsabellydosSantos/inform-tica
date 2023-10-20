peso = float(input("Informe seu peso(em Kg): "))
altura = float(input("Informe sua altura(em m): "))

imc = peso / (altura**2)

imc = round(imc)

if(imc <= 18.6):
    print("Seu IMC é igual a ", imc, ", você está abaixo do peso")

elif(imc <= 24.9):
    print("Seu IMC é igual a ", imc, ", você está no peso ideal")

elif(imc <= 29.9):
    print("Seu IMC é igual a ", imc, ", você está com sobrepeso")

elif(imc <= 30):
    print("Seu IMC é igual a ", imc, ", você está obeso")

elif(imc >= 31):
    print("Seu IMC é igual a ", imc, ", você está com besidade mórbida")