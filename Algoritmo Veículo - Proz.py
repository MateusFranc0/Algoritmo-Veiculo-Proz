#Algoritmo Proz

quant_rds = int(input("Informe a quantidade de rodas do veículo: "))
peso_bruto = float(input("Informe o peso bruto em quilogramas do veículo: "))
quant_pessoas = int(input("Informe a quantidade de pessoas no veículo: "))


if quant_rds == 2 or quant_rds == 3:
    categoria = "A"
elif quant_rds == 4 and peso_bruto <= 3500 and quant_pessoas <= 8:
    categoria = "B"
elif quant_rds >= 4 and peso_bruto > 3500 and peso_bruto <= 6000:
    categoria = "C"
elif quant_rds >= 4 and quant_pessoas > 8:
    categoria = "D"
elif quant_rds >= 4 and peso_bruto > 6000:
    categoria = "E"
else:
    categoria = "Categoria não identificada"


print("A categoria de habilitação para o veículo informado é:", categoria)