import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

matriks_konfusi = np.array([
    [1106,    0,   40], 
    [ 171,    0,   23],  
    [ 350,    0,  228]  
])

label_kelas = ["Negatif", "Netral", "Positif"]

plt.figure(figsize=(7, 5))

sns.heatmap(
    matriks_konfusi,
    annot=True,           
    fmt="d",            
    cmap="Blues",         
    xticklabels=label_kelas,
    yticklabels=label_kelas,
    linewidths=0.8,
    annot_kws={"size": 12, "weight":"bold"}
)

plt.xlabel("Prediksi Sentimen", fontsize=11)
plt.ylabel("Aktual Sentimen", fontsize=11)

plt.tight_layout()
plt.savefig(
    "Gambar5_Matriks_Konfusi_TikTok.png",
    dpi=300,                # Standar jurnal
    bbox_inches="tight"
)

plt.show()