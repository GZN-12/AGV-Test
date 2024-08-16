import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasının tam konumu
file_path = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-2-400 stroke-70psi-plug 1\AGV_Test_with_Suit-1(08.08.2024).xlsx"

# Verileri Excel dosyasından okuma
data = pd.read_excel(file_path, engine='openpyxl')

# X ekseni için K45-K358 hücrelerindeki verileri alma (Türkçe formatını düzeltmek için virgülleri nokta ile değiştiriyoruz)
X = data.loc[44:357, 'K'].apply(lambda x: str(x).replace(',', '.')).astype(float).tolist()

# Y ekseni için B45-B358 hücrelerindeki verileri alma (Türkçe formatını düzeltmek için virgülleri nokta ile değiştiriyoruz)
Y = data.loc[44:357, 'B'].apply(lambda x: str(x).replace(',', '.')).astype(float).tolist()

# X ve Y listelerini kontrol etme
print("X Ekseni:", X)
print("Y Ekseni:", Y)

# Grafik oluşturma
plt.figure(figsize=(16, 10))
plt.scatter(X, Y, color="r", s=2)  # s parametresi noktaların boyutunu belirler

# Grafik başlıkları ve etiketleri
plt.title('Time-Pressure Graph')
plt.xlabel('Time (Second)')
plt.ylabel('Pressure (psi)')

# Grid çizgileri
plt.grid(True)


# X eksenindeki grid çizgilerinin sayısını azaltma
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=28))

# Y eksenindeki grid çizgilerinin sayısını azaltma
plt.gca().yaxis.set_major_locator(plt.MaxNLocator(nbins=28))

# Grafiği gösterme
plt.show()
