par = 0
impar = 0

for i in range (4):
    x = int(input("Informe um valore inteiro: "))
    x = x % 2
    if (x > 0):
        impar += 1
    else:
        par += 1

print("Você digitou {} valores pares e {} valores impares".format (par, impar))