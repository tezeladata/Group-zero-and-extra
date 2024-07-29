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

coefficient = [100,98.51851852,98.46153846,98.16793893,97.71428571,96.25,95.55555556,93.65853659,92.78481013,92.63157895,92,91.86440678,91.17647059,90.63492063,90,89.93710692,89.92907801,88.90625,87.9245283,85.84070796,85.44,84.84210526,84.76190476,83.22580645,80,79.15492958,78.75,76.4516129,76.16666667,75.11111111,73.125,70,68.62745098,68.25396825,66.66666667,65.66666667,62.0083682,58.96103896,56.92307692,42.06896552,39.45945946,36.58536585,35,34.83870968,-5.34351145]

Salaries = [152.5,67.5,162.5,327.5,175,160,270,205,395,285,162.5,295,170,315,75,397.5,352.5,320,132.5,282.5,312.5,237.5,52.5,155,45,177.5,160,155,300,112.5,160,90,127.5,157.5,105,300,597.5,192.5,97.5,580,92.5,205,100,155,327.5]

names = ["ისაკაძე","ქიმერიძე","ძინძიბაძე","გურგენიძე","ჟუჟუნაძე","გუჯაბიძე","ყვავაძე","ხუსკივაძე","სამსონიძე","გიორგელაშვილი","მოწონელიძე","კილასონია","ჯახველაძე","ვანიშვილი","ვარაზაშვილი","მოთიაშვილი","ზაბახიძე","ფოფხაძე","ნუცუბიძე","გაგნიძე","შუბითიძე","აბაშიძე","აკოფიანი","ღომიძე","ბექაური","ნავროზაშვილი","პაპუნაშვილი","ნატროშვილი","საზანდრიშვილი","წითლაური","მათე დოლიძე","გვრიტიშვილი","შავაძე","ფილიშვილი","ჯალაღონია","აბრამიანი","გრძელიშვილი","ნუკრაძე","იოანე დოლიძე","ვახტანგაშვილი","თირქია","არღუთაშვილი","ვარადაშვილი","კვარაცხელია","ნარიმანიძე"]

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