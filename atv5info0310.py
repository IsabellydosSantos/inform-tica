dist = float(input("Informe a distância entre os destinos(em Km): "))
cons = float(input("Informe o consumo do carro em (km/1): "))
valc = float(input("Informe o valor do combustível(em R$): "))

gastl = dist/cons

gastt = gastl * valc

print("O gasto total da viagem será de ", gastt, " reais")