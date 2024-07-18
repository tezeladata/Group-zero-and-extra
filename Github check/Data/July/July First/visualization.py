import numpy as np
import matplotlib.pyplot as plt

data = [('Gurgenidze', 97.40458015, 327.5), ('Samsonidze', 96.71052632, 380), ('Shubitidze', 95.36, 312.5), ('Zabakhidze', 95.09433962, 397.5), ('Vanishvili', 94.71428571, 350), ('Kvavadze', 94.07407407, 270), ('Abrahamiani', 100, 165), ('Nutsubidze', 100, 110), ('Jakhveladze', 99.41176471, 170), ('Dzindzibadze', 99.1011236, 222.5), ('Zhuzhunadze', 97.2972973, 185), ('Shavadze', 97.25490196, 127.5), ('Mostonelidze', 95.38461538, 162.5), ('Varazashvili', 92.88888889, 112.5), ('Gagnidze', 92.38938053, 282.5), ('Grdzelishvili', 91.57024793, 605), ('Giorgelashvili', 91.26760563, 355), ('Pofkhadze', 90, 300), ('Narimanidze', 88.71794872, 487.5), ('Motiashvili', 88.29268293, 410), ('Kilasonia', 85.59322034, 295), ('Isakadze', 100, 100), ('Ioane Dolidze', 100, 30), ('Svanidze', 98.75, 80), ('Khuskivadze', 88.37837838, 185), ('Kimeridze', 87.55555556, 112.5), ('Ghomidze', 87.11864407, 147.5), ('Papunashvili', 86.66666667, 37.5), ('Vakhtangashvili', 78.44827586, 580), ('Sazandrishvili', 70.66666667, 300), ('Tirkia', 84.44444444, 112.5), ('Mate Dolidze', 83.46666667, 187.5), ('Natroshvili', 81.4084507, 177.5), ('Navrozashvili', 79.22077922, 192.5), ('Filishvili', 78.13333333, 187.5), ('Gvritishvili', 76.19047619, 105), ('Abashidze', 75, 240), ('Nukradze', 74.05405405, 185), ('Tsitlauri', 70.22222222, 112.5), ('Jalagonia', 69.04761905, 105), ('Okruashvili', 40.63492063, 157.5), ('Katsarava', 26.95652174, 115), ('Arghutashvili', 0, 205), ('Gogishvili', 0, 102.5), ('Varadashvili', 43.5, 100), ('Acofian', 34.81481481, 67.5), ('Bekauri', 28.88888889, 45), ('Kartvelishvili', 0, 72.5)]

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