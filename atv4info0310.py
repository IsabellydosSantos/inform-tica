alcool = float(input("Informe o valor do álcool(em R$): "))
gas = float(input("Informe o valor da gasolina(em R$): "))

porcen = (alcool / gas) *100

porcen = round(porcen)

if porcen >= 75:
 print("A relação entre os valores é de: ", porcen, "%. Compensa utilizar a gasolina.")
else:
 print("A relação entre os valores é de: ", porcen, "%. Compensa utilizar o álcool.")