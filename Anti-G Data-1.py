# This data set is measured at 08.07.2024, it measures the stroke and Anti G valve's putput pressure values.
# Test _1 at 16:40
# Test _2 at 17:17
# Test _3 at 17:40



import matplotlib.pyplot as plt
import pandas as pd


# Verilen listeler
stroke_1_1 = [400, 390, 380, 370, 360, 350, 340, 330, 320, 310, 300, 290, 280, 270, 265, 260, 255, 250]
stroke_1_2 = [600-stroke for stroke in stroke_1_1]
stroke_1 =[]
print(stroke_1_2)

stroke_1 = [round(0.0127*stroke,3) for stroke in stroke_1_2]
print(stroke_1)



pressure_1_abs = [0.015, 0.277, 0.931, 2.409, 3.431, 4.200, 4.885, 5.576, 6.293, 6.937, 7.688, 8.426, 9.088, 9.822, 10.130, 10.503, 10.829, 11.269]
pressure_2_abs = [0.01709,0.2103,0.8089,2.2720,3.3851,4.1584,4.8684,5.5483,6.2528,6.9138,7.6052,8.3341,9.0400,9.7939,10.0277,10.4330,10.7284,11.1678]
pressure_3_abs = [0.0062,0.1857,0.7414,2.2230,3.3414,4.0440,4.7908,5.4813,6.1788,6.8659,7.5938,8.2929,9.0033,9.7180,10.0325,10.4289,10.7274,11.1493]
p_atm_1 = (0.00205 + 0.00138) / 2
p_atm_2 = (-0.00504-0.0038)/ 2
p_atm_3 = (-0.00543-0.003523)/ 2
# Her bir sayıdan p_atm'yi çıkaran yeni bir liste oluşturma
pressure_gauge_1 = [pressure - p_atm_1 for pressure in pressure_1_abs]
pressure_gauge_2 = [pressure - p_atm_2 for pressure in pressure_2_abs]
pressure_gauge_3 = [pressure - p_atm_3 for pressure in pressure_3_abs]
print("Atmospheric pressure for Test_1:",p_atm_1)
print("Atmospheric pressure for Test_2:",p_atm_2)
print("Atmospheric pressure for Test_3:",p_atm_3,"\n")

data = {
    'Stroke': stroke_1,
    'Pressure 1 (abs)': pressure_1_abs,
    'Pressure 2 (abs)': pressure_2_abs,
    'Pressure 3 (abs)': pressure_3_abs
}

df = pd.DataFrame(data)

# DataFrame'i görüntüleme
print(df,"\n")


# Drawng plot for first test data
plt.figure(figsize=(18, 8),dpi=200,facecolor='white',frameon=True)
plt.plot(pressure_gauge_1, stroke_1, marker='o', linestyle='-', color='b', label='Test 1',mfc ="r",mec="r")
plt.title('Stroke vs Output Pressure (Gauge) Test-1')
plt.xlabel('Pressure (Psi)')
plt.ylabel('Stroke (mm)')
plt.grid(True)
plt.legend()

#Showing the data points
for pressure, stroke in zip(pressure_gauge_1, stroke_1):
    plt.annotate(f'({pressure:.3f}, {stroke})', (pressure, stroke), textcoords="offset points", xytext=(0,15), ha='center', fontsize=8, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white", alpha=0.7))

plt.show()


# Drawng plot for second data set
plt.figure(figsize=(18, 8),dpi=200,facecolor='white',frameon=True)
plt.plot(pressure_gauge_2, stroke_1, marker='o', linestyle='-', color='k', label='Test 2',mfc ="r",mec="r")
plt.title('Stroke vs Output Pressure (Gauge) Test-2')
plt.xlabel('Pressure (Psi)')
plt.ylabel('Stroke (mm)')
plt.grid(True)
plt.legend()

#Showing the data points
for pressure, stroke in zip(pressure_gauge_2, stroke_1):
    plt.annotate(f'({pressure:.3f}, {stroke})', (pressure, stroke), textcoords="offset points", xytext=(0,15), ha='center', fontsize=8, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white", alpha=0.7))

plt.show()

# Drawng plot for third data set
plt.figure(figsize=(18, 8),dpi=200,facecolor='white',frameon=True)
plt.plot(pressure_gauge_3, stroke_1, marker='o', linestyle='-', color='g', label='Test 3',mfc ="r",mec="r")
plt.title('Stroke vs Output Pressure (Gauge) Test-3')
plt.xlabel('Pressure (Psi)')
plt.ylabel('Stroke (mm)')
plt.grid(True)
plt.legend()

#Showing the data points
for pressure, stroke in zip(pressure_gauge_3, stroke_1):
    plt.annotate(f'({pressure:.3f}, {stroke})', (pressure, stroke), textcoords="offset points", xytext=(0,15), ha='center', fontsize=8, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white", alpha=0.7))

plt.show()


plt.figure(figsize=(18, 8),dpi=300,facecolor='white',frameon=True)
plt.plot(pressure_gauge_1, stroke_1, marker='o', linestyle='-', color='b', label='Test 1',mfc ="r",mec="r")
plt.plot(pressure_gauge_2, stroke_1, marker='*', linestyle='-', color='k', label='Test 2',mfc ="r",mec="r")
plt.plot(pressure_gauge_3, stroke_1, marker='<', linestyle='-', color='g', label='Test 3',mfc ="r",mec="r")
plt.title('Stroke vs Output Pressure (Gauge) ')
plt.xlabel('Pressure (Psi)')
plt.ylabel('Stroke (mm)')
plt.grid(True)
plt.legend()













r = 2  # in meters
g = 9.82508  # in m/s^2, gravitational acceleration
G_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print headers
print("{:<10} {:<15} {:<10}".format("G", "w (rad/s)", "N (rpm)"))

# Lists to store G and N values for plotting
G_values = []
N_values = []
P_values = []
P_max_values = []
P_min_values = []
P_mask_values = []
filtered_G_values = []
filtered_P_values = []
filtered_P_mask_values = []

for G in G_list:
    w = ((G * g) / r) ** 0.5  # in rad/s
    N = w * 9.54929  # converting rad/s to rpm
    G_values.append(G)
    N_values.append(N)

for G in G_list:
    P = 1.5 * G - 2.5
    P_max = 1.5 * G - 1.75
    P_min = 1.5 * G - 3.25
    P_values.append(P)
    P_max_values.append(P_max)
    P_min_values.append(P_min)

for G in G_list:
    P_mask = (G - 4) * 6.4
    if P_mask >= 0:
        filtered_G_values.append(G)
        filtered_P_values.append(1.5 * G - 2.5)
        filtered_P_mask_values.append(P_mask)



plt.figure(figsize=(18,8),dpi=200,facecolor='white',frameon=True)
plt.plot(G_values,P_values, marker='o', linestyle='-', color='g', label='P (psi)',mfc ="r",mec="r",linewidth = '3')
plt.plot(G_values,P_max_values, marker='*', linestyle='-.', color='k', label='P_max (psi)',mfc ="b",mec="b")
plt.plot(G_values,P_min_values, marker='*', linestyle='-.', color='k', label='P_min (psi)',mfc ="b",mec="b")
plt.xlabel('G (dimensionless)')
plt.ylabel('P (psi)')
plt.title('G vs Anti-G pressure (psi)')
plt.grid(True)
plt.legend()
plt.show()