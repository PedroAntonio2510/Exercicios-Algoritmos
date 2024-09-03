
# Exercicio 3

import json

with open('./Exec3/faturamento.json') as file:
  data = json.load(file)

faturamentos = [dia["valor"] for dia in data['faturamento_diario'] if dia["valor"] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

print(f"O menor faturamento do mês: {menor_faturamento}")
print(f"O maior faturamento do mês: {maior_faturamento}")
print(f"Numero de dias com faturamento acima da média: {dias_acima_da_media}")