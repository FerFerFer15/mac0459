# Contar ocorrências por tipo de motor
motores_contagem = aeronave['aeronave_motor_tipo'].value_counts()

# Plotar os tipos de motores mais comuns em ocorrências
plt.figure(figsize=(10, 6))
motores_contagem.head(10).plot(kind='bar', color='lightcoral')
plt.title("Tipos de Motores Associados às Ocorrências")
plt.xlabel("Tipo de Motor")
plt.ylabel("Número de Ocorrências")
plt.xticks(rotation=45)
plt.show()
