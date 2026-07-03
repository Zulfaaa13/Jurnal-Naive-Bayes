import matplotlib.pyplot as plt

# Data
labels = ['Negatif', 'Netral', 'Positif']
jumlah_ulasan = [5730, 970, 2890]
persentase = ['59,7%', '10,1%', '30,1%']
warna = ['#d62728', '#1f77b4', '#2ca02c']  # Warna sesuai gambar ke-2

# Buat grafik
plt.figure(figsize=(12, 8))
bars = plt.bar(labels, jumlah_ulasan, color=warna, edgecolor='black')

# Tambahkan teks (jumlah + persentase) di atas setiap batang
for bar, count, pct in zip(bars, jumlah_ulasan, persentase):
    tinggi = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, tinggi + 100,  # 100 = jarak teks dari atas batang
             f'{count}\n({pct})',
             ha='center', va='bottom', fontsize=14, fontweight='bold')

# Hapus garis grid
plt.grid(False)

# Hapus garis atas dan kanan (opsional, agar lebih bersih seperti gambar ke-2)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Atur label dan judul
plt.ylabel('Jumlah Ulasan', fontsize=16)
plt.xlabel('Kelas Sentimen', fontsize=18)
plt.ylim(0, 6200)  # Batas sumbu y agar teks tidak terpotong

plt.tight_layout()
plt.show()