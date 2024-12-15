# Filtrar recomendações sem feedback
recomendacoes_pendentes = recomendacao[recomendacao['recomendacao_status']=="AGUARDANDO RESPOSTA"]

# Calcular o tempo desde o encaminhamento
recomendacoes_pendentes['dias_desde_envio'] = (pd.Timestamp.now() - pd.to_datetime(recomendacoes_pendentes['recomendacao_dia_encaminhamento'], errors='coerce')).dt.days

# Ordenar por tempo desde o encaminhamento
recomendacoes_pendentes = recomendacoes_pendentes.sort_values(by='dias_desde_envio', ascending=False)

# Exibir as 10 recomendações mais antigas pendentes
print(recomendacoes_pendentes.head(10)[['recomendacao_numero', 'recomendacao_dia_encaminhamento', 'dias_desde_envio']])
