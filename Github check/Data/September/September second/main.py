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

coefficient = [92.02247191,82.50460405,67.78350515,88.42364532,90.99378882,78.44611529,92.76595745,78.83165829,83.50515464,66.66666667,37.88819876,67.66169154,72.47706422,70.23809524,41.26213592,81.94444444,58.64197531,88.61256545,88.87195122,98.75,60.29411765,0,89.93902439,76.55172414,79.41176471,85.71428571,73.52941176,90.90909091,91.17647059,67.22689076,100,24.13793103,49.18032787,95.76719577,40.27777778,90.98143236,84.12698413,78.62068966,89.38992042,86.07594937,87.5,0]

Salaries = [890,543,194,812,161,399,235,796,194,189,161,201,218,168,206,72,81,382,328,320,68,191,164,145,68,161,238,66,34,238,21,145,61,189,72,377,189,145,1131,79,48,7]

names = ["მოთიაშვილი","პაპუნაშვილი","წითლაური","აბაშიძე","ხუბერიშვილი","აბრამიანი","სამსონიძე","ვახტანგაშვილი","გიორგელაშვილი","ისაკაძე","კვინჩია","ზაბახიძე","გვრიტიშვილი","შავაძე","დოლიძე","ვარადაშვილი","ქიმერიძე","შუბითიძე","ვანიშვილი","გურგენიძე","მელიქჯანიანი","ყვავაძე","ჯახველაძე","ძინძიბაძე","ჯიმშიაშვილი","ჭიტაძე","ფოფხაძე","ალავიძე","რაზმაძე","ხუსკივაძე","ლორთქიფანიძე","აკოფიანი","ვარაზაშვილი","კვარაცხელია","ქორიძე","კილასონია","გუჯაბიძე","სვანიძე","გრძელიშვილი","ბექაური","ნუცუბიძე","ღომიძე"]

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