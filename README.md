# Analisis Sentimen Publik Kebijakan Privasi dan Keamanan Data TikTok dengan Naive Bayes

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Research%20Project-orange)](#)
[![Dataset](https://img.shields.io/badge/Dataset-TikTok%20Reviews-purple)](#)
[![License](https://img.shields.io/badge/License-Unspecified-lightgrey)](#)

> Proyek penelitian yang menggabungkan pemrosesan bahasa alami, machine learning, dan visualisasi data untuk menganalisis opini publik terhadap kebijakan privasi TikTok.

## 🌟 Ringkasan Proyek
Penelitian ini bertujuan mengidentifikasi sentimen pengguna Indonesia terhadap isu privasi dan keamanan data pada aplikasi TikTok berdasarkan ulasan dari Google Play Store. Proyek ini membandingkan tiga model klasifikasi, yaitu Multinomial Naive Bayes, SVM Linear, dan IndoBERT, untuk mengetahui model mana yang paling efektif dalam menangani teks berbahasa Indonesia.

## 🎯 Tujuan Penelitian
1. Mengidentifikasi distribusi sentimen publik terhadap kebijakan privasi TikTok.
2. Menerapkan metode klasifikasi teks berbasis machine learning.
3. Menangani ketidakseimbangan kelas menggunakan SMOTE.
4. Membandingkan performa model secara objektif melalui metrik evaluasi.
5. Menyajikan hasil dalam bentuk visualisasi yang informatif dan mudah dipahami.

## 🧪 Metodologi

<div align="center">
  <img src="Gambar 1. Flowchart Alur Penelitian.jpeg" width="700" alt="Gambar 1. Flowchart Alur Penelitian">
  <p><em>Flowchart Alur Penelitian</em></p>
</div>

### 1. Preprocessing Teks
- Case folding
- Filtering untuk menghapus URL, mention, hashtag, tanda baca, dan angka
- Tokenizing
- Stopword removal untuk bahasa Indonesia

### 2. Ekstraksi Fitur
- Menggunakan metode TF-IDF untuk mengubah teks menjadi representasi numerik berbobot.

### 3. Penanganan Kelas Tidak Seimbang
- Teknik SMOTE diterapkan pada data training untuk mengurangi bias kelas.
- Parameter yang digunakan: k-neighbor = 5.
- Hasilnya, distribusi data training menjadi lebih seimbang.

| Teknik | Deskripsi | Parameter |
|---|---|---|
| SMOTE | Synthetic Minority Over-sampling Technique, membuat sampel sintetis dari kelas minoritas berdasarkan tetangga terdekat. | k_neighbors = 5 |

| Sebelum SMOTE | Negatif | Netral | Positif |
|---|---:|---:|---:|
| Jumlah | 4.584 | 776 | 2.312 |

| Setelah SMOTE | Negatif | Netral | Positif |
|---|---:|---:|---:|
| Jumlah | 4.584 | 4.568 | 4.568 |

### 4. Pembagian Dataset
- Rasio pembagian: 80% data training dan 20% data testing.
- Pembagian dilakukan secara stratified dengan random_state = 42.

### 5. Model Klasifikasi
1. Multinomial Naive Bayes
2. SVM Linear
3. IndoBERT

## 📊 Dataset
- Sumber: Dataset publik Kaggle, yaitu TikTok App Reviews Indonesia – Google Play Store.
- Total data awal: 100.000 ulasan.
- Data relevan setelah filtering: 9.590 ulasan.
- Kriteria filtering: kata kunci yang berkaitan dengan privasi, kebocoran data, izin akses, keamanan akun, dan isu terkait perlindungan data.
- Pelabelan sentimen dilakukan berdasarkan rating otomatis:
  - 1–2 bintang = Negatif
  - 3 bintang = Netral
  - 4–5 bintang = Positif

### Distribusi Kelas Sentimen
| Kelas Sentimen | Jumlah Ulasan | Persentase |
|---|---:|---:|
| Negatif | 5.730 | 59,7% |
| Positif | 2.890 | 30,1% |
| Netral | 970 | 10,1% |
| Total | 9.590 | 100% |

<div align="center">
  <img src="Gambar 2 Grafik Batang Distribusi Sentimen Ulasan TikTok Terkait Privasi.png" width="600" alt="Gambar 2. Grafik Batang Distribusi Sentimen">
  <p><em>Grafik Batang Distribusi Sentimen Ulasan TikTok Terkait Privasi</em></p>
</div>

### Analisis Kata Kunci Utama

<div align="center">
  <img src="Gambar 3. WordCloud Kata Kunci Ulasan TikTok Terkait Privasi.png" width="650" alt="Gambar 3. WordCloud Kata Kunci Ulasan">
  <p><em>WordCloud Kata Kunci Ulasan TikTok Terkait Privasi</em></p>
</div>

Visualisasi WordCloud menunjukkan kata-kata yang paling sering muncul dalam ulasan terkait privasi TikTok, dengan emphasis pada term seperti "privasi", "data", "akses", "aman", dan "bocor".

## 📈 Hasil Evaluasi Model

### Matriks Konfusi Model Multinomial Naive Bayes

| Kelas Aktual \ Prediksi | Negatif | Netral | Positif |
|---|---:|---:|---:|
| Negatif | 1.106 | 0 | 40 |
| Netral | 171 | 0 | 23 |
| Positif | 350 | 0 | 228 |

<div align="center">
  <img src="Gambar 4. Matriks Konfusi Hasil Klasifikasi Model Multinomial Naive Bayes.png" width="500" alt="Gambar 4. Matriks Konfusi">
  <p><em>Matriks Konfusi Hasil Klasifikasi Model Multinomial Naive Bayes</em></p>
</div>

### Performa Model Multinomial Naive Bayes

| Metrik | Nilai |
|---|---:|
| Akurasi | 69,6% |
| Presisi (Weighted) | 64,2% |
| Recall (Weighted) | 69,6% |
| F1-Score (Weighted) | 63,5% |

<div align="center">
  <img src="Gambar 5. Grafik Batang Metrik Evaluasi Model.png" width="600" alt="Gambar 5. Grafik Batang Metrik Evaluasi">
  <p><em>Grafik Batang Metrik Evaluasi Model</em></p>
</div>

### Perbandingan Performa Ketiga Model

| Model | Akurasi | Presisi | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Multinomial Naive Bayes | 69,6% | 64,2% | 69,6% | 63,5% |
| SVM Linear | 74,3% | 71,8% | 73,9% | 72,1% |
| IndoBERT | 81,2% | 79,5% | 80,7% | 79,9% |

<div align="center">
  <img src="Gambar 6. Grafik Perbandingan Performa Ketiga Model Klasifikasi.png" width="700" alt="Gambar 6. Grafik Perbandingan Performa Ketiga Model">
  <p><em>Grafik Perbandingan Performa Ketiga Model Klasifikasi</em></p>
</div>

### Temuan Utama
- Sentimen negatif mendominasi ulasan terkait privasi TikTok (59,7%).
- Penerapan SMOTE mampu meningkatkan performa model Naive Bayes secara signifikan.
- IndoBERT menunjukkan performa terbaik dengan akurasi 81,2% karena mampu memahami konteks kalimat secara lebih baik.
- Kelas netral tetap menjadi tantangan karena sering memiliki kemiripan kosakata dengan kelas lain.

## 📁 Struktur Proyek
```text
tiktok-sentiment-privacy/
├── data/
│   ├── raw/                # dataset mentah dari Kaggle
│   └── processed/          # data hasil preprocessing
├── src/
│   ├── preprocessing.py    # pembersihan teks
│   ├── feature_extraction.py
│   ├── modeling.py         # pelatihan model
│   └── evaluation.py       # evaluasi dan visualisasi
├── results/
│   ├── confusion_matrix/
│   └── plots/
├── notebooks/
│   └── main_experiment.ipynb
└── README.md
```

## ⚙️ Cara Menjalankan
### Prasyarat
Pastikan sistem sudah terpasang:
- Python 3.8+
- Paket Python: pandas, numpy, scikit-learn, imbalanced-learn, nltk, Sastrawi, matplotlib, wordcloud, transformers

### Langkah Instalasi
1. Clone repositori ini.
2. Instal semua dependensi:
   ```bash
   pip install -r requirements.txt
   ```
3. Tempatkan dataset Kaggle ke folder data/raw/.
4. Jalankan preprocessing:
   ```bash
   python src/preprocessing.py
   ```
5. Jalankan pelatihan dan evaluasi model:
   ```bash
   python src/modeling.py
   ```

## 📚 Referensi
Penelitian ini mengacu pada karya:
- Zulfa Agustin. Analisis Sentimen Publik Kebijakan Privasi dan Keamanan Data TikTok dengan Naive Bayes. Institut Teknologi dan Bisnis Indonesia.

Dokumen ini dibuat sebagai bagian dari dokumentasi proyek penelitian dan demonstrasi analisis sentimen berbasis machine learning.