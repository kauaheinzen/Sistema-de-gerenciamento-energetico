from ler import *
eletronicos = []

casa = ler_casa(1)
consumo_mensal = ler_consumo_total(1)
print(consumo_mensal[0])

for eletrodomestico in casa[1]:
    eletronicos.append(eletrodomestico)


prompt = f"""
Crie 10 soluções curtas para o problema de consumo excessivo de energia elétrica em uma residência,
considerando que a família possui {casa[0][1]} integrantes e possui os seguintes eletrodomésticos com os respectivos parâmetros sendo eles:
nome, consumo em Wh e horas utilizadas por dia, segue a lista de eletrônicos: {eletronicos}. 
O consumo total mensal é de {consumo_mensal[0]}W.
Após as análises e dicas, faça uma tabela com os eletrodomésticos, consumo em Wh, horas utilizadas por dia e o consumo total mensal de cada um deles após a aplicação dessas mudanças.
"""

print(prompt)