import matplotlib.pyplot as plt
import numpy as np

models = ['Multinomial Naive Bayes', 'SVM Linear', 'IndoBERT']
metrics = ['Akurasi', 'Presisi', 'Recall', 'F1-Score']
colors = ['#3794db', '#37d06b', '#f79d1c', '#ed4c40']  
data = [
    [69.6, 64.2, 69.6, 63.5],   
    [74.3, 71.8, 73.9, 72.1],   
    [81.2, 79.5, 80.7, 79.9]    
]

fig, ax = plt.subplots(figsize=(14, 8))
x = np.arange(len(models))  
width = 0.2  

rects_list = []
for i in range(len(metrics)):
    rects = ax.bar(
        x + i * width,         
        [row[i] for row in data],
        width,
        label=metrics[i],
        color=colors[i],
        edgecolor='black'     
    )
    rects_list.append(rects)

def tambah_label(rects):
    for rect in rects:
        tinggi = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            tinggi + 0.5,
            f"{tinggi:.1f}".replace(".", ","),  
            ha='center', va='bottom',
            fontsize=11, fontweight='bold'
        )

for rects in rects_list:
    tambah_label(rects)

ax.set_ylabel('Nilai Metrik (%)', fontsize=14, fontweight='normal')
ax.set_xlabel('Model Klasifikasi', fontsize=16, fontweight='normal')
ax.set_xticks(x + width * 1.5) 
ax.set_xticklabels(models, fontsize=12)
ax.set_ylim(0, 90)  

ax.grid(False)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(loc='lower right', fontsize=12)

fig.tight_layout()
plt.show()