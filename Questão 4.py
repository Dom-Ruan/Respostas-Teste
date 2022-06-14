faturamento = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88,
               "ES": 27165.48, "Outros": 19849.53}

soma = 0

for estado in faturamento:
    soma += faturamento[estado]

for estado in faturamento:
    porcentagem = (faturamento[estado] / soma) * 100
    print(estado, "-", "%.2f" %porcentagem+"%")
