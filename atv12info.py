cneg = 0
cpos = 0

for i in range (5):
    val = float(input("Informe um valor: "))
    if val < 0:
       cneg += 1
    else:
       cpos += 1

print("Você digitou {} valores negativos e {} valores positivos".format(cneg, cpos))
