faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

valor_total = sum(faturamento.values())

percentuais = {estado: (valor / valor_total) * 100 for estado, valor in faturamento.items()}

print(f"Faturamento total: R$ {valor_total:.2f}\n")

for estado, percentual in percentuais.items():
  print(f"{estado}: {percentual:.2f}% do faturamento total.")