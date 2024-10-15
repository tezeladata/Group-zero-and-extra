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

coefficient = [71.46245059,50.22222222,12.97297297,74.94071146,83.51851852,62.45614035,76.27118644,74.33962264,66.77966102,-40.74074074,50.66666667,66.52173913,92.47524752,76.33333333,46.41509434,66.66666667,90.48275862,81.18518519,45.2173913,38.88888889,59.21568627,78.5106383,71.01449275,76.2962963,81.92307692,53.33333333,79.2,89.42857143,79.71830986,84.09638554,88.46846847,90,93.62318841,74.85714286,81.9047619,88.95522388,92.65306122,90.20408163,95.15151515,91.11111111,100,100,100]

Salaries = [632.5,337.5,185,632.5,810,285,442.5,397.5,295,67.5,187.5,230,1010,300,132.5,210,725,337.5,115,90,127.5,235,172.5,202.5,260,90,187.5,350,177.5,207.5,277.5,275,345,87.5,105,167.5,245,122.5,165,22.5,55,105,90]

names = ["პაპუნაშვილი","ლორთქიფანიძე","ედიშერაშვილი","ვახტანგაშვილი","გრძელიშვილი","ვანიშვილი","ძინძიბაძე","აბრამიანი","გურგენიძე","ხუციშვილი","კვინჩია","გუჯაბიძე","მოთიაშვილი","შუბითიძე","ხუსკივაძე","მელიქჯანიანი","აბაშიძე","წითლაური","ბექაური","აკოფიანი","სვანიძე","სამსონიძე","ანდრია კობახიძე","ხუბერიშვილი","ფოფხაძე","ვარაზაშვილი","კოჩალიძე","კვარაცხელია","ქორიძე","ისაკაძე","კილასონია","ჭიტაძე","გვრიტიშვილი","ნუცუბიძე","არახამია","შავაძე","ჯახველაძე","ვარადაშვილი","ქიმერიძე","ღომიძე","ზაბახიძე","ალავიძე","რაზმაძე"]

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