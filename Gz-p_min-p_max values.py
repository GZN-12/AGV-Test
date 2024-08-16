Gz = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9]

y_min = []
y = []
y_max = []

# Hesaplamaları yapalım
for i in Gz:
    y_min.append(1.5 * i - 3.25)
    y.append(1.5 * i - 2.5)
    y_max.append(1.5 * i - 1.75)

# Başlıkları yazdıralım
print(f"{'No':<3} {'Gz':<5} {'P_min':<10} {'P (psig)':<10} {'P_max':<10}")

# Listeleri numaraları ile birlikte tablo halinde yazdıralım
for index, (gz_val, min_val, mid_val, max_val) in enumerate(zip(Gz, y_min, y, y_max), start=1):
    print(f"{index:<3} {gz_val:<5} {min_val:<10.2f} {mid_val:<10.2f} {max_val:<10.2f}")
