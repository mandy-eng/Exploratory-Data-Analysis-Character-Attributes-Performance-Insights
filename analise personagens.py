import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r"C:\Users\Valley\Desktop\scripts-py\planilha dr projeto de dados.xlsx")
df.head()
df.info()
df.describe()
print(df.columns)
df['Influência no Julgamento'] = (
    df['Influência no Julgamento']
    .str.lower()
    .str.strip()
)
df['Talento Ultimate'] = (
    df['Talento Ultimate']
    .str.strip()
)
colunas_numericas = [
    'Altura (cm)',
    'QI (Est.)',
    'Sobrevivência (%)'
]
for col in colunas_numericas:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df.isnull().sum()
df = df.dropna()
contagem_influencia = df['Influência no Julgamento'].value_counts()
contagem_influencia
qi_por_influencia = (
    df.groupby('Influência no Julgamento')['QI (Est.)']
    .mean()
)
sobrevivencia_por_influencia = (
    df.groupby('Influência no Julgamento')['Sobrevivência (%)']
    .mean()
    .sort_values(ascending=False)
)
qi_por_talento = (
    df.groupby('Talento Ultimate')['QI (Est.)']
    .mean()
    .sort_values(ascending=False)
)
top_sobreviventes = df.sort_values(
    by='Sobrevivência (%)',
    ascending=False
)[['Nome do Personagem', 'Sobrevivência (%)']]
top_sobreviventes
contagem_influencia.plot(kind='bar')
plt.title('Contagem de Personagem por Influência no Julgamento')
plt.xlabel('Influência no Julgamento')
plt.ylabel('Quantidade')
plt.show()

qi_por_influencia.plot(kind='bar')
plt.title('QI Médio por nível de Influência no Julgamento')
plt.xlabel('Influência no Julgamento')
plt.ylabel('QI Estimado')
plt.show()

sobrevivencia_por_influencia.plot(kind='bar')
plt.title('Sobrevivência por nível de Influência no Julgamento')
plt.xlabel('Influência no Julgamento')
plt.ylabel('Sobrevivência (%)')
plt.show()

qi_por_talento.plot(kind='bar')
plt.title('QI Médio por Talento Ultimate')
plt.xlabel('Talento Ultiamate')
plt.ylabel('QI Estimado')
plt.show()

df.to_excel('analise_personagens_dr_projeto_dados.xlsx', index=False)


