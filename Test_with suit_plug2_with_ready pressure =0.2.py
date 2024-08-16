import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyalarının tam konumları
file_path_200 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-3-200 stroke-70psi-plug 2 with reaady pressure=0.2\200 Stroke_Read pressure0.22_(12.08.2024).xlsx"
file_path_180 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-4-180 stroke-70psi-plug 2 with ready pressure =0,2\180 Stroke_Read pressure0.22_(12.08.2024).xlsx"
file_path_170 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-5-170 stroke-70psi-plug 2 with ready pressure 0.22\170 Stroke_Read pressure0.22_(12.08.2024).xlsx"
file_path_160 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-6-160 stroke-70psi-plug 2 with ready pressure 0.22\160 Stroke_Read pressure0.22_(12.08.2024).xlsx"
file_path_150 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-7-150 stroke-70psi-plug 2 with ready pressure 0.22\150 Stroke_Read pressure0.22_(12.08.2024).xlsx"
file_path_150_2=  r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-7-150 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_150Stroke.xlsx"
file_path_200_2 = r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-3-200 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_200Stroke.xlsx"
file_path_180_2= r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-4-180 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_180Stroke.xlsx"
file_path_170_2= r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-5-170 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)_170Storek.xlsx"
file_path_160_2= r"C:\Users\hakan\OneDrive\Masaüstü\AGV_Test\AGV Test with Suit\AGV Test with suit-6-160 stroke-70psi-plug 2\AGV_Test_with_Suit-1(09.08.2024)160Stroke.xlsx"

# Excel dosyalarını okuma ve verileri listeye çevirme fonksiyonu
def get_data(file_path, row_start, row_end, x_col, y_col):
    data = pd.read_excel(file_path, engine='openpyxl')
    X = data.loc[row_start:row_end, x_col].apply(lambda x: str(x).replace(',', '.')).astype(float).tolist()
    Y = data.loc[row_start:row_end, y_col].apply(lambda x: str(x).replace(',', '.')).astype(float).tolist()
    return X, Y

# Verileri alma
X_200, Y_200 = get_data(file_path_200, 0, 685, 'J', 'B')
X_180, Y_180 = get_data(file_path_180, 0, 195, 'J', 'B')
X_170, Y_170 = get_data(file_path_170, 0, 277, 'J', 'B')
X_160, Y_160 = get_data(file_path_160, 0, 169, 'J', 'B')
X_150, Y_150 = get_data(file_path_150, 0, 295, 'J', 'B')
X_150_2, Y_150_2 = get_data(file_path_150_2, 0, 295, 'J', 'B')
X_160_2, Y_160_2 = get_data(file_path_160_2, 0, 295, 'J', 'B')
X_170_2, Y_170_2 = get_data(file_path_170_2, 0, 295, 'J', 'B')
X_180_2, Y_180_2 = get_data(file_path_180_2, 0, 295, 'J', 'B')
X_200_2, Y_200_2 = get_data(file_path_200_2, 0, 295, 'J', 'B')
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


# Her bir veri setini curve (çizgi) olarak ekleme
#plt.plot(X_200, Y_200, label="200 Stroke")
#plt.plot(X_180, Y_180, label="180 Stroke")
#plt.plot(X_170, Y_170, label="170 Stroke")
#plt.plot(X_160, Y_160, label="160 Stroke")


plt.figure(figsize=(16, 10))
plt.plot(X_150, Y_150, label="150 Stroke")
plt.plot(X_150_2, Y_150_2, label="150_ Stroke")
# Grafik başlıkları ve etiketleri
plt.title('Time-Pressure Graph for Different Strokes with Ready pressure')
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



plt.figure(figsize=(16, 10))
plt.plot(X_160, Y_160, label="160 Stroke")
plt.plot(X_160_2, Y_160_2, label="160_ Stroke")
# Grafik başlıkları ve etiketleri
plt.title('Time-Pressure Graph for Different Strokes with Ready pressure')
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

plt.figure(figsize=(16, 10))
plt.plot(X_170, Y_170, label="170 Stroke")
plt.plot(X_170_2, Y_170_2, label="170_ Stroke")
# Grafik başlıkları ve etiketleri
plt.title('Time-Pressure Graph for Different Strokes with Ready pressure')
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


plt.figure(figsize=(16, 10))
plt.plot(X_180, Y_180, label="180 Stroke")
plt.plot(X_180_2, Y_180_2, label="180_ Stroke")
# Grafik başlıkları ve etiketleri
plt.title('Time-Pressure Graph for Different Strokes with Ready pressure')
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



plt.figure(figsize=(16, 10))
plt.plot(X_200, Y_200, label="200 Stroke")
plt.plot(X_200_2, Y_200_2, label="180_ Stroke")
# Grafik başlıkları ve etiketleri
plt.title('Time-Pressure Graph for Different Strokes with Ready pressure')
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