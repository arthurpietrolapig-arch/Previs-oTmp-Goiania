import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1. Coordenadas de Goiânia na API gratuita do Open-Meteo
url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=-16.6869&longitude=-49.2648"
    "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
    "&timezone=America%2FSao_Paulo"
)

# 2. Busca e organização dos dados
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["daily"])
# Formata a data para Dia/Mês (ex: 04/08)
df["time"] = pd.to_datetime(df["time"]).dt.strftime("%d/%m")

# 3. Criação do gráfico
fig, ax1 = plt.subplots(figsize=(10, 5))

# Linhas de Temperatura Máxima e Mínima
ax1.plot(df["time"], df["temperature_2m_max"], color="#e74c3c", marker="o", linewidth=2.5, label="Temp. Máxima (°C)")
ax1.plot(df["time"], df["temperature_2m_min"], color="#2980b9", marker="o", linewidth=2.5, label="Temp. Mínima (°C)")
ax1.set_xlabel("Data", fontsize=11, fontweight="bold")
ax1.set_ylabel("Temperatura (°C)", fontsize=11, fontweight="bold")
ax1.grid(True, linestyle="--", alpha=0.5)

# Barras de Chuva no eixo secundário
ax2 = ax1.twinx()
ax2.bar(df["time"], df["precipitation_sum"], color="#3498db", alpha=0.3, width=0.4, label="Chuva (mm)")
ax2.set_ylabel("Chuva (mm)", fontsize=11, fontweight="bold")

# Título e Legendas
plt.title("Previsão do Tempo para Goiânia - Próximos 7 Dias", fontsize=14, fontweight="bold", pad=15)

# Combina as legendas dos dois eixos
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

plt.tight_layout()

# 4. Salva a imagem
plt.savefig("previsao_goiania.png", dpi=300)
print("Gráfico gerado e salvo como previsao_goiania.png")
