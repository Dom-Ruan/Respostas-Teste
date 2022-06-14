import json

with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

print(dados)
soma = 0
menor = 1000000
maior = 0
cont = 0

for dado in dados:
    valor = dado["valor"]
    
    if valor == 0:
        continue

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor


    soma += valor
    cont += 1

media = soma / cont

print("O menor valor de faturamento foi", menor)

print("O maior valor de faturamento foi", maior)

cont = 0

for dado in dados:
    if dado["valor"] > media:
        cont += 1

print("O faturamento foi superior a média em", cont, "dias")





