def calculate_work(work_coefficient, salary, name):
    if salary > 250:
        salary_range = "high_salary"
    elif 100 < salary <= 250:
        salary_range = "mid_salary"
    else:
        salary_range = "low_salary"

    if work_coefficient > 92.5:
        efficiency_range = "high_eff"
    elif 85 < work_coefficient <= 92.5:
        efficiency_range = "mid_eff"
    else:
        efficiency_range = "low_eff"



    if salary_range == "high_salary":
        if efficiency_range == "high_eff":
            high_salary_high_eff.append((name, work_coefficient, salary))
        elif efficiency_range == "mid_eff":
            high_salary_mid_eff.append((name, work_coefficient, salary))
        else:
            high_salary_low_eff.append((name, work_coefficient, salary))
    elif salary_range == "mid_salary":
        if efficiency_range == "high_eff":
            mid_salary_high_eff.append((name, work_coefficient, salary))
        elif efficiency_range == "mid_eff":
            mid_salary_mid_eff.append((name, work_coefficient, salary))
        else:
            mid_salary_low_eff.append((name, work_coefficient, salary))
    else:  # low_salary
        if efficiency_range == "high_eff":
            low_salary_high_eff.append((name, work_coefficient, salary))
        elif efficiency_range == "mid_eff":
            low_salary_mid_eff.append((name, work_coefficient, salary))
        else:
            low_salary_low_eff.append((name, work_coefficient, salary))

    return (salary_range, efficiency_range)

high_salary_high_eff = []
mid_salary_high_eff = []
high_salary_mid_eff = []
low_salary_high_eff = []
mid_salary_mid_eff = []
low_salary_mid_eff = []
high_salary_low_eff = []
mid_salary_low_eff = []
low_salary_low_eff = []

# %, salary, name
# calculate_work(0, 205, "Arghutashvili")

coefficient = [
    0, 0, 0, 78.44827586, 40.63492063, 70.66666667, 26.95652174, 75, 43.5, 
    88.71794872, 91.57024793, 88.29268293, 74.05405405, 34.81481481, 85.59322034, 
    78.13333333, 79.22077922, 70.22222222, 81.4084507, 69.04761905, 28.88888889, 
    91.26760563, 83.46666667, 90, 76.19047619, 92.38938053, 88.37837838, 95.09433962, 
    87.11864407, 94.71428571, 84.44444444, 94.07407407, 95.36, 87.55555556, 
    96.71052632, 97.40458015, 92.88888889, 95.38461538, 97.2972973, 86.66666667, 
    97.25490196, 99.1011236, 98.75, 99.41176471, 100, 100, 100, 100
]

Salaries = [
    205, 102.5, 72.5, 580, 157.5, 300, 115, 240, 100, 487.5, 605, 410, 185, 
    67.5, 295, 187.5, 192.5, 112.5, 177.5, 105, 45, 355, 187.5, 300, 105, 
    282.5, 185, 397.5, 147.5, 350, 112.5, 270, 312.5, 112.5, 380, 327.5, 112.5, 
    162.5, 185, 37.5, 127.5, 222.5, 80, 170, 165, 110, 100, 30
]

names = [
    "Arghutashvili", "Gogishvili", "Kartvelishvili", "Vakhtangashvili", "Okruashvili", 
    "Sazandrishvili", "Katsarava", "Abashidze", "Varadashvili", "Narimanidze", 
    "Grdzelishvili", "Motiashvili", "Nukradze", "Acofian", "Kilasonia", 
    "Filishvili", "Navrozashvili", "Tsitlauri", "Natroshvili", "Jalagonia", 
    "Bekauri", "Giorgelashvili", "Mate Dolidze", "Pofkhadze", "Gvritishvili", 
    "Gagnidze", "Khuskivadze", "Zabakhidze", "Ghomidze", "Vanishvili", 
    "Tirkia", "Kvavadze", "Shubitidze", "Kimeridze", "Samsonidze", "Gurgenidze", 
    "Varazashvili", "Mostonelidze", "Zhuzhunadze", "Papunashvili", "Shavadze", 
    "Dzindzibadze", "Svanidze", "Jakhveladze", "Abrahamiani", "Nutsubidze", 
    "Isakadze", "Ioane Dolidze"
]

[calculate_work(coefficient[i], Salaries[i], names[i]) for i in range(len(names))]

high_salary_high_eff.sort(key=lambda x: x[1], reverse=True)
mid_salary_high_eff.sort(key=lambda x: x[1], reverse=True)
high_salary_mid_eff.sort(key=lambda x: x[1], reverse=True)
low_salary_high_eff.sort(key=lambda x: x[1], reverse=True)
mid_salary_mid_eff.sort(key=lambda x: x[1], reverse=True)
low_salary_mid_eff.sort(key=lambda x: x[1], reverse=True)
high_salary_low_eff.sort(key=lambda x: x[1], reverse=True)
mid_salary_low_eff.sort(key=lambda x: x[1], reverse=True)
low_salary_low_eff.sort(key=lambda x: x[1], reverse=True)

print(
    high_salary_high_eff,
    mid_salary_high_eff,
    high_salary_mid_eff,
    low_salary_high_eff,
    mid_salary_mid_eff,
    low_salary_mid_eff,
    high_salary_low_eff,
    mid_salary_low_eff,
    low_salary_low_eff,
    sep="\n"
)