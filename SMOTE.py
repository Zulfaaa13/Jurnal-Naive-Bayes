import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

total_negatif = 5730
total_netral = 970
total_positif = 2890

np.random.seed(42)
ulasan_negatif = ["kebocoran data privasi aplikasi tiktok tidak aman"] * total_negatif
ulasan_netral  = ["biasa saja standar privasi lokasi kamera"] * total_netral
ulasan_positif = ["sangat aman perlindungan privasi bagus"] * total_positif

teks_data = ulasan_negatif + ulasan_netral + ulasan_positif
label_data = (['Negatif'] * total_negatif + 
              ['Netral'] * total_netral + 
              ['Positif'] * total_positif)

df = pd.DataFrame({'Ulasan': teks_data, 'Sentimen': label_data})

print("=========================================================")
print(" TAHAPAN 1: DISTRIBUSI KELAS AWAL DATASET (Tabel 4)      ")
print("=========================================================")
counts = df['Sentimen'].value_counts()
pct = df['Sentimen'].value_counts(normalize=True) * 100
for idx in counts.index:
    print(f"Kelas {idx:<8}: {counts[idx]:<5} ulasan ({pct[idx]:.1f}%)")

tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(df['Ulasan'])
y = df['Sentimen']

print("\n=========================================================")
print(" TAHAPAN 2: EKSTRAKSI FITUR DENGAN TF-IDF (Bab 2.6)       ")
print("=========================================================")
print(f"Berhasil mengonversi {X_tfidf.shape[0]} teks ulasan menjadi matriks numerik.")
print(f"Jumlah fitur kata unik yang terbentuk: {X_tfidf.shape[1]}")

X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42, stratify=y
)

print("\n=========================================================")
print(" TAHAPAN 3: DATA TRAINING SEBELUM SMOTE (Tabel 1)        ")
print("=========================================================")
print(y_train.value_counts())
print(f"Total Data Training Asli: {X_train.shape[0]} ulasan")

smote = SMOTE(k_neighbors=5, random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

print("\n=========================================================")
print(" TAHAPAN 4: DATA TRAINING SETELAH SMOTE (Tabel 2)        ")
print("=========================================================")
print(pd.Series(y_train_resampled).value_counts())
print(f"Total Data Training Akhir: {X_train_resampled.shape[0]} ulasan")

print("\n=========================================================")
print(" TAHAPAN 5: VERIFIKASI DATA TESTING (TETAP ASLI)         ")
print("=========================================================")
print(y_test.value_counts())
print(f"Total Data Testing (Murni): {X_test.shape[0]} ulasan")
print("=========================================================")
