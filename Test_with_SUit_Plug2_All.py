import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyalarının tam konumları
file_path_200 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-3-200 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_200Stroke.xlsx"
file_path_180 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-4-180 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_180Stroke.xlsx"
file_path_170 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-5-170 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_170Storek.xlsx"
file_path_160 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-6-160 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)160Stroke.xlsx"
file_path_150 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-7-150 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_150Stroke.xlsx"

# Excel dosyalarını okuma ve verileri listeye çevirme fonksiyonu
def get_data(file_path, row_start, row_end, x_col, y_col):
    data = pd.read_excel(file_path, engine='openpyxl')
    X = data.loc[row_start:row_end, x_col].apply(lambda x: str(x).replace(',', '.')).astype(float).tolist()
    Y = data.loc[row_start:row_end, y_col].apply(lambda x: str(x).replace(',', '.')).astype(float).tolist()
    return X, Y

# Verileri alma
X_200, Y_200 = get_data(file_path_200, 0, 282, 'J', 'B')
X_180, Y_180 = get_data(file_path_180, 0, 204, 'J', 'B')
X_170, Y_170 = get_data(file_path_170, 0, 182, 'J', 'B')
X_160, Y_160 = get_data(file_path_160, 0, 182, 'J', 'B')
X_150, Y_150 = get_data(file_path_150, 0, 175, 'J', 'B')

# Grafik oluşturma (scatter plot)
plt.figure(figsize=(16, 10))

# Her bir veri setini scatter plot olarak ekleme
plt.scatter(X_200, Y_200, label="200 Stroke", s=2)
plt.scatter(X_180, Y_180, label="180 Stroke", s=2)
plt.scatter(X_170, Y_170, label="170 Stroke", s=2)
plt.scatter(X_160, Y_160, label="160 Stroke", s=2)
plt.scatter(X_150, Y_150, label="150 Stroke", s=2)

# Grafik başlıkları ve etiketleri
plt.title('Scatter Plot: Time-Pressure Graph for Different Strokes with Plug 2')
plt.xlabel('Time (Second)')
plt.ylabel('Pressure (psi)')

# Grid çizgileri
plt.grid(True)

# Legend ekleme
plt.legend()

# Grafiği gösterme
plt.show()

# Grafik oluşturma (curve plot)
plt.figure(figsize=(16, 10))

# Her bir veri setini curve (çizgi) olarak ekleme
plt.plot(X_200, Y_200, label="200 Stroke")
plt.plot(X_180, Y_180, label="180 Stroke")
plt.plot(X_170, Y_170, label="170 Stroke")
plt.plot(X_160, Y_160, label="160 Stroke")
plt.plot(X_150, Y_150, label="150 Stroke")

# Grafik başlıkları ve etiketleri
plt.title('Curve Plot: Time-Pressure Graph for Different Strokes with Plug 2')
plt.xlabel('Time (Second)')
plt.ylabel('Pressure (psi)')

# Grid çizgileri
plt.grid(True,alpha=0.5)
# X eksenindeki grid çizgilerinin sayısını azaltma
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=35))

# Y eksenindeki grid çizgilerinin sayısını azaltma
plt.gca().yaxis.set_major_locator(plt.MaxNLocator(nbins=35))


# Legend ekleme
plt.legend()

# Grafiği gösterme
plt.show()