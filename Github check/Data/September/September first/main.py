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

coefficient = [98.28571429,94.28571429,93.91304348,92,91.51515152,90.55555556,89.17431193,86.66666667,85.84615385,85.03703704,84.70588235,84,83.58208955,81.30653266,80,78.88888889,78.51851852,77.5,77.5,77.4789916,75.89041096,75.77777778,74.02597403,73.96825397,71.89873418,70.21276596,69.375,67.24137931,66.2745098,56.92307692,54.71698113,54.28571429,50.32258065,36.98630137,-1.714285714,48]

Salaries = [175,210,115,237.5,82.5,270,272.5,300,162.5,337.5,170,750,335,497.5,95,180,67.5,320,120,595,182.5,450,192.5,315,197.5,235,240,145,255,65,132.5,157.5,155,547.5,87.5,187.5]

names = ["ჯახველაძე","გუჯაბიძე","ვარადაშვილი","ზაბახიძე","ჯიმშიაშვილი","სამსონიძე","ფოფხაძე","ვანიშვილი","სვანიძე","აბრამიანი","ძინძიბაძე","გრძელიშვილი","კილასონია","აბაშიძე","კვარაცხელია","შავაძე","ვარაზაშვილი",
"შუბითიძე","ქიმერიძე","მოთიაშვილი","ხუსკივაძე","პაპუნაშვილი","ჭიტაძე","გურგენიძე","ყვავაძე","გიორგელაშვილი","გვრიტიშვილი","ისაკაძე","დოლიძე","ჯალაღონია","მელიქჯანიანი","ხუბერიშვილი","აკოფიანი","ვახტანტაშვილი","ბექაური", "წითლაური"]

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