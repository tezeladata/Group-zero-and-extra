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
calculate_work(39.02439024, 307.5, "Janashia")
calculate_work(29.09090909, 165, "Sazandrishvili")
calculate_work(78.86010363, 482.5, "Narimanidze")
calculate_work(79.36507937, 472.5, "Bukhrashvili")
calculate_work(15.55555556, 112.5, "Tirkia")
calculate_work(70.4950495, 252.5, "Beridze")
calculate_work(76.5, 300, "Janezashvili")
calculate_work(51.53846154, 130, "Katsarava")
calculate_work(50.4, 125, "Gogishvili")
calculate_work(71.53846154, 195, "Tinikashvili")
calculate_work(48.57142857, 105, "Varadashvili")
calculate_work(90.94017094, 585, "Vakhtangashvili")
calculate_work(72.26666667, 187.5, "Okruashvili")
calculate_work(58.36734694, 122.5, "Qartvelishvili")
calculate_work(73.50649351, 192.5, "Berkacashvili")
calculate_work(77.34939759, 207.5, "Kvavadze")
calculate_work(51.79487179, 97.5, "Gvritishvili")
calculate_work(79.75903614, 207.5, "Navrozashvili")
calculate_work(80.24390244, 205, "Arghutashvili")
calculate_work(80.24390244, 205, "Khvichia")
calculate_work(80.24390244, 205, "Melqadze")
calculate_work(45.18518519, 67.5, "Akofiani")
calculate_work(83.59550562, 222.5, "Motsonelidze")
calculate_work(89.92805755, 347.5, "Grdzelishvili")
calculate_work(76.61016949, 147.5, "Qimeridze")
calculate_work(88.39285714, 280, "Kilasonia")
calculate_work(82.94117647, 170, "Khuskivadze")
calculate_work(92.69230769, 390, "Vanishvili")
calculate_work(51.42857143, 52.5, "Ghomidze")
calculate_work(79.11111111, 112.5, "Sikharulidze")
calculate_work(92, 275, "Motiashvili")
calculate_work(51.11111111, 45, "Varazashvili")
calculate_work(95.71428571, 455, "Zabakhidze")
calculate_work(89.5890411, 182.5, "Shubitidze")
calculate_work(94.80916031, 327.5, "Giorgelashvili")
calculate_work(74.81481481, 67.5, "Abramiani")
calculate_work(93.65384615, 260, "Pophkadze")
calculate_work(87.45098039, 127.5, "Jalagonia")
calculate_work(78.66666667, 37.5, "Shavadze")
calculate_work(97.14285714, 245, "Gagnidze")
calculate_work(94.50980392, 127.5, "Abashidze")
calculate_work(96.52173913, 172.5, "Gurgenidze")
calculate_work(97.25, 200, "Jakhveladze")
calculate_work(97.74647887, 177.5, "Samsonidze")
calculate_work(93.33333333, 45, "Dolidze")
calculate_work(96.84210526, 95, "Isakadze")
calculate_work(98.84057971, 172.5, "Dekanoidze")
calculate_work(96.66666667, 30, "Amonashvili")
calculate_work(86.66666667, 7.5, "Tsitlauri")
calculate_work(93.33333333, 15, "Tarieladze")
calculate_work(100, 22.5, "Dzindzibadze")
calculate_work(100, 22.5, "Bendeliani")
calculate_work(100, 87.5, "Nutsubidze")

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