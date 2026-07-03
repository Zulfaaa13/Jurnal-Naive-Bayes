from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

teks_kata_kunci = """
privasi privasi privasi bocor bocor bocor data data data aman aman izin izin 
akses akses kebocoran lokasi kamera mikrofon akun akun sadap lacak hack 
secure perlindungan kebijakan tiktok tiktok
"""

wordcloud = WordCloud(
    width=800,          
    height=400,         
    background_color="white",  
    max_words=100,      
    stopwords=None,     
    prefer_horizontal=0.9, 
    collocations=False,
    font_path=None     
).generate(teks_kata_kunci)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # Hilangkan sumbu koordinat

plt.tight_layout()
plt.savefig(
    "Gambar5_WordCloud_TikTok_Privasi.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()