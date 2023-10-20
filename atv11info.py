num = int(input("Informe o número que você quer saber o fatorial: "))

result = 1
count = 1

while count <= num:
    result *= count
    count += 1

print(result)