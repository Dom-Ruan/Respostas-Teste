entrada = input("Digite a string a ser revertida: ")

saida = ""

tamanho = len(entrada)

for i in range(tamanho-1, -1, -1):
    saida += entrada[i]

print(saida)
