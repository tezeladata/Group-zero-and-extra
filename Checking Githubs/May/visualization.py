import numpy as np
import matplotlib.pyplot as plt

data = [
('Tezelashvili', 96.69421488, 302.5), ('Grdzelishvili', 96.64122137, 327.5), ('Giorgelashvili', 93.65079365, 315), ('Motiashvili', 93.08411215, 267.5), ('Razmadze', 98.70967742, 155), ('Nutsubidze', 98.04878049, 102.5), ('Tirkia', 97.77777778, 112.5), ('Filishvili', 94.73684211, 142.5), ('Diasamidze', 94.28571429, 140), ('Popkhadze', 92.65822785, 197.5), ('Vanishvili', 88.59649123, 285), ('Janezashvili', 88.33333333, 330), ('Leverashvili', 100, 45), ('Gurgenidze', 100, 70), ('Taktakidze', 100, 37.5), ('Tkeshelashvili', 100, 7.5), ('Dekanoidze', 98.66666667, 0.1), ('Qimeridze', 97.5, 80), ('Khuskivadze', 96.66666667, 60), ('Shavadze', 96.66666667, 30), ('Svanidze', 95.83333333, 60), ('Berkacashvili', 94.07407407, 67.5), ('Gagnidze', 91.70212766, 235), ('Zabakhidze', 89.8, 250), ('Molodini', 88.88888889, 90), ('Sazandrishvili', 84.53333333, 187.5), ('Navrozashvili', 83.38028169, 177.5), ('Vakhtangashvili', 75.15789474, 237.5), ('Tinikashvili', 74, 125), ('Janashia', 80, 80), ('Arghutashvili', 69.72972973, 92.5), ('Guntaishvili', 55.23809524, 52.5), ('Buxrashvili', 39.04761905, 52.5), ('Amonashvili', 20, 15), ('Sikharulidze', 0, 7.5)
]

# Extracting individual lists from the data
names = [item[0] for item in data]
coefficients = [item[1] for item in data]
salaries = [item[2] for item in data]

# Plotting
plt.figure(figsize=(12, 8))
plt.barh(names, coefficients, color='#634234')
plt.xlabel('Work Coefficient')
plt.ylabel('Squad Leaders')
plt.title('Work Coefficient by Leader')
plt.suptitle("From best to worst")
plt.gca().invert_yaxis()
plt.grid(axis="x", lw=1)
plt.show()