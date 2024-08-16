import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasının tam konumu
#file_path_200 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-3-200 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_200Stroke.xlsx"
#file_path_180 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-4-180 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_180Stroke.xlsx"
#file_path_170 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-5-170 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_170Storek.xlsx"
#file_path_160 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-6-160 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)160Stroke.xlsx"
file_path_150 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-7-150 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_150Stroke.xlsx"







# Verileri Excel dosyasından okuma
data = pd.read_excel(file_path_150, engine='openpyxl')

# X ekseni için K45-K358 hücrelerindeki verileri alma (Türkçe formatını düzeltmek için virgülleri nokta ile değiştiriyoruz)
X_150 = data.loc[0:175, 'J'].apply(lambda x: str(x).replace(',', '.')).astype(float).tolist()

# Y ekseni için B45-B358 hücrelerindeki verileri alma (Türkçe formatını düzeltmek için virgülleri nokta ile değiştiriyoruz)
Y_150 = data.loc[0:175, 'B'].apply(lambda x: str(x).replace(',', '.')).astype(float).tolist()

# X ve Y listelerini kontrol etme
print("X Ekseni:", X_150)
print("Y Ekseni:", Y_150)

# Grafik oluşturma
plt.figure(figsize=(16, 10))
plt.scatter(X_150, Y_150, color="r", s=2)  # s parametresi noktaların boyutunu belirler

# Grafik başlıkları ve etiketleri
plt.title('Time-Pressure Graph in 160 Stroke  w/ _plug2')
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
