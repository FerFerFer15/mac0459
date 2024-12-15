# Extrair a hora da coluna 'ocorrencia_hora'
ocorrencia['hora'] = pd.to_datetime(ocorrencia['ocorrencia_hora'], errors='coerce').dt.hour

# Contar o número de ocorrências por hora
ocorrencias_por_hora = ocorrencia['hora'].value_counts().sort_index()

# Plotar o gráfico da distribuição
plt.figure(figsize=(10, 6))
plt.bar(ocorrencias_por_hora.index, ocorrencias_por_hora.values, color='skyblue')
plt.title("Distribuição de Ocorrências por Hora do Dia")
plt.xlabel("Hora do Dia")
plt.ylabel("Número de Ocorrências")
plt.xticks(range(0, 24))
plt.grid(axis='y')
plt.show()
