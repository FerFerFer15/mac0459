# Extrair o ano da coluna 'ocorrencia_dia'
ocorrencia['ano'] = pd.to_datetime(ocorrencia['ocorrencia_dia'], errors='coerce').dt.year

# Contar o número de ocorrências por ano
ocorrencias_por_ano = ocorrencia['ano'].value_counts().sort_index()

# Plotar o gráfico de ocorrências ao longo dos anos
plt.figure(figsize=(10, 6))
plt.plot(ocorrencias_por_ano.index, ocorrencias_por_ano.values, marker='o', linestyle='-')
plt.title("Número de Ocorrências Aeronáuticas ao Longo dos Anos")
plt.xlabel("Ano")
plt.ylabel("Número de Ocorrências")
plt.grid()
plt.show()