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

calculate_work(75.15789474, 237.5, "Vakhtangashvili")
calculate_work(88.33333333, 330, "Janezashvili")
calculate_work(88.59649123, 285, "Vanishvili")
calculate_work(74, 125, "Tinikashvili")
calculate_work(39.04761905, 52.5, "Buxrashvili")
calculate_work(83.38028169, 177.5, "Navrozashvili")
calculate_work(84.53333333, 187.5, "Sazandrishvili")
calculate_work(69.72972973, 92.5, "Arghutashvili")
calculate_work(89.8, 250, "Zabakhidze")
calculate_work(55.23809524, 52.5, "Guntaishvili")
calculate_work(93.65079365, 315, "Giorgelashvili")
calculate_work(91.70212766, 235, "Gagnidze")
calculate_work(93.08411215, 267.5, "Motiashvili")
calculate_work(80, 80, "Janashia")
calculate_work(92.65822785, 197.5, "Popkhadze")
calculate_work(96.64122137, 327.5, "Grdzelishvili")
calculate_work(88.88888889, 90, "Molodini")
calculate_work(96.69421488, 302.5, "Tezelashvili")
calculate_work(94.28571429, 140, "Diasamidze")
calculate_work(0, 7.5, "Sikharulidze")
calculate_work(94.73684211, 142.5, "Filishvili")
calculate_work(94.07407407, 67.5, "Berkacashvili")
calculate_work(97.77777778, 112.5, "Tirkia")
calculate_work(95.83333333, 60, "Svanidze")
calculate_work(98.70967742, 155, "Razmadze")
calculate_work(98.04878049, 102.5, "Nutsubidze")
calculate_work(97.5, 80, "Qimeridze")
calculate_work(96.66666667, 60, "Khuskivadze")
calculate_work(96.66666667, 30, "Shavadze")
calculate_work(98.66666667, 0.1, "Dekanoidze")
calculate_work(100, 45, "Leverashvili")
calculate_work(100, 70, "Gurgenidze")
calculate_work(100, 37.5, "Taktakidze")
calculate_work(100, 7.5, "Tkeshelashvili")
calculate_work(20, 15, "Amonashvili")

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