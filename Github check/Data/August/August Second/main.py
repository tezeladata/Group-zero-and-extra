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

coefficient = [100,100,98.88888889,98.37398374,98.28571429,97.07317073,95.45454545,94.76923077,94.08695652,92.47058824,92.38095238,91.75257732,91.70212766,91.56862745,91.48387097,90.66666667,88.57142857,88.52459016,86.05042017,85.29411765,85,84.35897436,82.47619048,80.83333333,79.31034483,77.2972973,77.00598802,73.79746835,72.30769231,71.84,69.19642857,67.33333333,66.06060606,62.66666667,62.55319149,59.11111111,58.0952381,50.52631579,45.33333333,42.90322581]

Salaries = [7.5,50,180,307.5,175,102.5,165,162.5,287.5,212.5,315,242.5,235,255,387.5,75,140,305,297.5,340,80,195,262.5,180,72.5,92.5,417.5,790,65,312.5,560,75,82.5,75,117.5,225,52.5,95,112.5,155]

names = ["ხმალაძე","ჭიტაძე","ისაკაძე","გურგენიძე","ძინძიბაძე","მელიქჯანიანი","მოწონელიძე","გუჯაბიძე","ზაბახიძე","ყვავაძე","ვანიშვილი","ფოფხაძე","შავაძე","გიორგელაშვილი","მოთიაშვილი","ქიმერიძე","ნუკრაძე","სამსონიძე","აბაშიძე","აბრამიანი","სვანიძე","კილასონია","შუბითიძე","ხუსკივაძე","ბექაური","ვარადაშვილი","პაპუნაშვილი","გრძელიშვილი","ჯალაღონია","ნარიმანიძე","ვახტანგაშვილი","წითლაური","გვრიტიშვილი","ვარაზაშვილი","აკოფიანი","დოლიძე","თირქია","კვარაცხელია","ფილიშვილი","ნავროზაშვილი"]

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