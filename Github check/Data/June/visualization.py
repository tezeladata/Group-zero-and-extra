import numpy as np
import matplotlib.pyplot as plt

data = [('Zabakhidze', 95.71428571, 455), ('Giorgelashvili', 94.80916031, 327.5), ('Pophkadze', 93.65384615, 260), ('Vanishvili', 92.69230769, 390),('Dekanoidze', 98.84057971, 172.5), ('Samsonidze', 97.74647887, 177.5), ('Jakhveladze', 97.25, 200), ('Gagnidze', 97.14285714, 245), ('Gurgenidze', 96.52173913, 172.5), ('Abashidze', 94.50980392, 127.5),('Motiashvili', 92, 275), ('Vakhtangashvili', 90.94017094, 585), ('Grdzelishvili', 89.92805755, 347.5), ('Kilasonia', 88.39285714, 280),('Dzindzibadze', 100, 22.5), ('Bendeliani', 100, 22.5), ('Nutsubidze', 100, 87.5), ('Isakadze', 96.84210526, 95), ('Amonashvili', 96.66666667, 30), ('Dolidze', 93.33333333, 45), ('Tarieladze', 93.33333333, 15),('Shubitidze', 89.5890411, 182.5), ('Jalagonia', 87.45098039, 127.5),('Tsitlauri', 86.66666667, 7.5),('Bukhrashvili', 79.36507937, 472.5), ('Narimanidze', 78.86010363, 482.5), ('Janezashvili', 76.5, 300), ('Beridze', 70.4950495, 252.5), ('Janashia', 39.02439024, 307.5),('Motsonelidze', 83.59550562, 222.5), ('Khuskivadze', 82.94117647, 170), ('Arghutashvili', 80.24390244, 205), ('Khvichia', 80.24390244, 205), 
('Melqadze', 80.24390244, 205), ('Navrozashvili', 79.75903614, 207.5), ('Sikharulidze', 79.11111111, 112.5), ('Kvavadze', 77.34939759, 207.5), 
('Qimeridze', 76.61016949, 147.5), ('Berkacashvili', 73.50649351, 192.5), ('Okruashvili', 72.26666667, 187.5), ('Tinikashvili', 71.53846154, 195), ('Qartvelishvili', 58.36734694, 122.5), ('Katsarava', 51.53846154, 130), ('Gogishvili', 50.4, 125), ('Varadashvili', 48.57142857, 105), ('Sazandrishvili', 29.09090909, 165), ('Tirkia', 15.55555556, 112.5),('Shavadze', 78.66666667, 37.5), ('Abramiani', 74.81481481, 67.5), ('Gvritishvili', 51.79487179, 97.5), ('Ghomidze', 51.42857143, 52.5), ('Varazashvili', 51.11111111, 45), ('Akofiani', 45.18518519, 67.5)
]

names = [item[0] for item in data]
coefficients = [item[1] for item in data]
salaries = [item[2] for item in data]

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(names, coefficients, color='#004225')
plt.xlabel('Work Coefficient')
plt.ylabel('Squad Leaders')
plt.title('Work Coefficient by Leader')
plt.suptitle("From best to worst")
plt.gca().invert_yaxis()
plt.grid(axis="x", lw=1)

# Font size
plt.yticks(fontsize=7)

plt.show()