import matplotlib.pyplot as plt

metrik = ['Akurasi', 'Presisi\n(Weighted)', 'Recall\n(Weighted)', 'F1-Score\n(Weighted)']
nilai = [69.6, 64.2, 69.6, 63.5]
warna = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] 

fig, ax = plt.subplots(figsize=(12, 8), dpi=120)

bars = ax.bar(metrik, nilai, color=warna, edgecolor='black', linewidth=1.5)

for bar in bars:
    tinggi = bar.get_height()
    # Format angka: ganti titik dengan koma
    label_teks = f'{tinggi:.1f}%'.replace('.', ',')
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        tinggi + 0.8,
        label_teks,
        ha='center', va='bottom', fontsize=16, fontweight='bold'
    )

ax.set_ylabel('Nilai (%)', fontsize=14)
ax.set_xlabel('Metrik Evaluasi', fontsize=16)
ax.set_ylim(0, 100)
ax.tick_params(axis='both', labelsize=14)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
