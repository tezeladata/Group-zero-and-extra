import numpy as np
import matplotlib.pyplot as plt

data = [
    ('Grdzelishvili', 98.59375, 320), ('Gagnidze', 97.60683761, 292.5), ('Giorgelashvili', 96.12403101, 322.5), 
    ('Tezelashvili', 95.43307087, 317.5), ('Shavadze', 95.11111111, 337.5), ('Gurgenidze', 100, 177.5), 
    ('Katsarava', 100, 130), ('Varadashvili', 100, 112.5), ('Dekanoidze', 99.33333333, 150), 
    ('Jakhveladze', 99.28571429, 140), ('Kilasonia', 98.29787234, 235), ('Berkacashvili', 96.75675676, 185), 
    ('Motsonelidze', 96.61971831, 177.5), ('Khuskivadze', 96.36363636, 192.5), ('Zhuzhunadze', 93, 200), 
    ('Janezashvili', 91.83333333, 300), ('Zabakhidze', 91.66666667, 420), ('Vanishvili', 91.53846154, 390), 
    ('Vakhtangashvili', 88.50299401, 417.5), ('Ghomidze', 100, 15), ('Tkeshelashvili', 100, 22.5), 
    ('Tarieladze', 100, 15), ('Isakadze', 98.85714286, 87.5), ('Aduashvili', 97.77777778, 45), 
    ('Abramiani', 97.33333333, 75), ('Tavadze', 95.55555556, 22.5), ('Qimeridze', 93.33333333, 60), 
    ('Diasamidze', 91.31578947, 190), ('Shubitidze', 90.52631579, 142.5), ('Tinikashvili', 89.52380952, 210), 
    ('Janashia', 88.46153846, 130), ('Varazashvili', 89.52380952, 52.5), ('Narimanidze', 81.38297872, 470), 
    ('Motiashvili', 78.61386139, 252.5), ('Popkhadze', 71.17647059, 255), ('Bukhrashvili', 69.62566845, 467.5), 
    ('Sazandrishvili', 56.08108108, 370), ('Arghutashvili', 45.10869565, 460), ('Jalagonia', 81.86046512, 107.5), 
    ('Navrozashvili', 80, 185), ('Guntaishvili', 79.40298507, 167.5), ('Kvavadze', 78.37837838, 185), 
    ('Okruashvili', 76.8, 187.5), ('Filishvili', 74.03508772, 142.5), ('Melkadze', 72.83950617, 202.5), 
    ('Tirkia', 66.22222222, 112.5), ('Gvritishvili', 54.66666667, 150), ('Nutsubidze', 48.8372093, 107.5), 
    ('Gogishvili', 28.57142857, 210), ('Khvichia', 26.95652174, 172.5), ('Taktakidze', 20.48192771, 207.5), 
    ('Qartvelishvili', 3.225806452, 155), ('Dolidze', 82.22222222, 45), ('Samsonidze', 81.81818182, 82.5), 
    ('Miruashvili', 80, 75), ('Beridze', 65.92592593, 67.5), ('Leverashvili', 51.11111111, 45), 
    ('Sikharulidze', 36, 37.5), ('Amonashvili', 35.55555556, 45), ('Molodini', 18.33333333, 90), 
    ('Grigolia', 0, 75)
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