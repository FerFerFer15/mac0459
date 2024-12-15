# Definir regiões do Brasil
regioes = {
    "Norte": ["AM", "RR", "AP", "PA", "TO", "RO", "AC"],
    "Nordeste": ["MA", "PI", "CE", "RN", "PB", "PE", "AL", "SE", "BA"],
    "Centro-Oeste": ["MT", "MS", "GO", "DF"],
    "Sudeste": ["SP", "RJ", "ES", "MG"],
    "Sul": ["PR", "SC", "RS"]
}

# Criar uma nova coluna 'regiao' no dataframe OCORRENCIA
def mapear_regiao(uf):
    for regiao, estados in regioes.items():
        if uf in estados:
            return regiao
    return "Desconhecido"

ocorrencia['regiao'] = ocorrencia['ocorrencia_uf'].apply(mapear_regiao)

# Contar ocorrências por região
ocorrencias_por_regiao = ocorrencia['regiao'].value_counts()

# Plotar a distribuição de ocorrências por região
plt.figure(figsize=(8, 6))
plt.bar(ocorrencias_por_regiao.index, ocorrencias_por_regiao.values, color='orange')
plt.title("Distribuição de Ocorrências por Região")
plt.xlabel("Região")
plt.ylabel("Número de Ocorrências")
plt.grid(axis='y')
plt.show()
