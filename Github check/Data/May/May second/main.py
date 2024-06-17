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

calculate_work(45.10869565, 460, "Arghutashvili")
calculate_work(20.48192771, 207.5, "Taktakidze")
calculate_work(56.08108108, 370, "Sazandrishvili")
calculate_work(3.225806452, 155, "Qartvelishvili")
calculate_work(28.57142857, 210, "Gogishvili")
calculate_work(69.62566845, 467.5, "Bukhrashvili")
calculate_work(26.95652174, 172.5, "Khvichia")
calculate_work(0, 75, "Grigolia")
calculate_work(81.38297872, 470, "Narimanidze")
calculate_work(71.17647059, 255, "Popkhadze")
calculate_work(18.33333333, 90, "Molodini")
calculate_work(54.66666667, 150, "Gvritishvili")
calculate_work(48.8372093, 107.5, "Nutsubidze")
calculate_work(72.83950617, 202.5, "Melkadze")
calculate_work(78.61386139, 252.5, "Motiashvili")
calculate_work(88.50299401, 417.5, "Vakhtangashvili")
calculate_work(76.8, 187.5, "Okruashvili")
calculate_work(78.37837838, 185, "Kvavadze")
calculate_work(66.22222222, 112.5, "Tirkia")
calculate_work(80, 185, "Navrozashvili")
calculate_work(74.03508772, 142.5, "Filishvili")
calculate_work(91.66666667, 420, "Zabakhidze")
calculate_work(79.40298507, 167.5, "Guntaishvili")
calculate_work(91.53846154, 390, "Vanishvili")
calculate_work(35.55555556, 45, "Amonashvili")
calculate_work(91.83333333, 300, "Janezashvili")
calculate_work(36, 37.5, "Sikharulidze")
calculate_work(65.92592593, 67.5, "Beridze")
calculate_work(89.52380952, 210, "Tinikashvili")
calculate_work(51.11111111, 45, "Leverashvili")
calculate_work(81.86046512, 107.5, "Jalagonia")
calculate_work(91.31578947, 190, "Diasamidze")
calculate_work(95.11111111, 337.5, "Shavadze")
calculate_work(88.46153846, 130, "Janashia")
calculate_work(81.81818182, 82.5, "Samsonidze")
calculate_work(80, 75, "Miruashvili")
calculate_work(95.43307087, 317.5, "Tezelashvili")
calculate_work(93, 200, "Zhuzhunadze")
calculate_work(90.52631579, 142.5, "Shubitidze")
calculate_work(96.12403101, 322.5, "Giorgelashvili")
calculate_work(82.22222222, 45, "Dolidze")
calculate_work(97.60683761, 292.5, "Gagnidze")
calculate_work(96.36363636, 192.5, "Khuskivadze")
calculate_work(96.61971831, 177.5, "Motsonelidze")
calculate_work(96.75675676, 185, "Berkacashvili")
calculate_work(89.52380952, 52.5, "Varazashvili")
calculate_work(98.59375, 320, "Grdzelishvili")
calculate_work(93.33333333, 60, "Qimeridze")
calculate_work(98.29787234, 235, "Kilasonia")
calculate_work(97.33333333, 75, "Abramiani")
calculate_work(98.85714286, 87.5, "Isakadze")
calculate_work(99.28571429, 140, "Jakhveladze")
calculate_work(97.77777778, 45, "Aduashvili")
calculate_work(99.33333333, 150, "Dekanoidze")
calculate_work(95.55555556, 22.5, "Tavadze")
calculate_work(100, 15, "Ghomidze")
calculate_work(100, 177.5, "Gurgenidze")
calculate_work(100, 22.5, "Tkeshelashvili")
calculate_work(100, 15, "Tarieladze")
calculate_work(100, 130, "Katsarava")
calculate_work(100, 112.5, "Varadashvili")

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