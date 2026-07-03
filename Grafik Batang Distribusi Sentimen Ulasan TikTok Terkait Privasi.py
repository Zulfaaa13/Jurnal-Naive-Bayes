import matplotlib.pyplot as plt

labels = ['Negatif', 'Netral', 'Positif']
jumlah_ulasan = [5730, 970, 2890]
persentase = ['59,7%', '10,1%', '30,1%']
warna = ['#d62728', '#1f77b4', '#2ca02c']  

plt.figure(figsize=(12, 8))
bars = plt.bar(labels, jumlah_ulasan, color=warna, edgecolor='black')

for bar, count, pct in zip(bars, jumlah_ulasan, persentase):
    tinggi = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, tinggi + 100,  
             f'{count}\n({pct})',
             ha='center', va='bottom', fontsize=14, fontweight='bold')

plt.grid(False)

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.ylabel('Jumlah Ulasan', fontsize=16)
plt.xlabel('Kelas Sentimen', fontsize=18)
plt.ylim(0, 6200)  

plt.tight_layout()
plt.show()
