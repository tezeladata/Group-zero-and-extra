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

calculate_work(39.31034483, 217.5, 'Beridze')
calculate_work(59.49579832, 297.5, 'Razmadze')
calculate_work(67.72727273, 220, 'Janashia')
calculate_work(55.25423729, 147.5, 'Tirkia')
calculate_work(62.81690141, 177.5, 'Tarieladze')
calculate_work(79.36507937, 315, 'Janezashvili')
calculate_work(64.78873239, 177.5, 'Leverashvili')
calculate_work(81.12903226, 310, 'Motiashvili')
calculate_work(72.63157895, 190, 'Sazandrishvili')
calculate_work(83.90243902, 307.5, 'Gagnidze')
calculate_work(53.33333333, 90, 'Nutsubidze')
calculate_work(43.7037037, 67.5, 'Amonashvili')
calculate_work(73.33333333, 142.5, 'Filishvili')
calculate_work(68.8372093, 107.5, 'Tinikashvili')
calculate_work(91.97278912, 367.5, 'Giorgelashvili')
calculate_work(64.84848485, 82.5, 'Vakhtangashvili')
calculate_work(90.29126214, 257.5, 'Babajanashvili')
calculate_work(72.97297297, 92.5, 'Fofxadze')
calculate_work(94.6961326, 452.5, 'Grdzelishvilli')
calculate_work(95.15625, 320, 'Vanishvili')
calculate_work(94.87179487, 292.5, 'Zabakhidze')
calculate_work(71.42857143, 52.5, 'Kimeridze')
calculate_work(93.5, 200, 'Khoperia')
calculate_work(92.61538462, 162.5, 'Navrozashvili')
calculate_work(97.27891156, 367.5, 'Tezelashvili')
calculate_work(46.66666667, 15, 'Katsarava')
calculate_work(6.666666667, 7.5, 'Tkeshelashvili')
calculate_work(90.66666667, 37.5, 'Adamia')
calculate_work(96.66666667, 90, 'Molodini')
calculate_work(100, 7.5, 'Sikharulidze')
calculate_work(100, 15, 'Bakuradze')
calculate_work(100, 60, 'Berkacashvili')
calculate_work(100, 320, 'Diasamidze')



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