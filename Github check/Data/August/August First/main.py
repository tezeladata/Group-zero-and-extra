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

coefficient = [52.53164557,70,10.625,38.57142857,72.0610687,44.51612903,82.26190476,78.11965812,37.94871795,49.52380952,64.52830189,79.54545455,52.43243243,85.5,70.87719298,82.79569892,80.97560976,88.23529412,60,92,66.66666667,92.72727273,93.49593496,92.32323232,94.44444444,95.03875969,88.57142857,88.23529412,83.88888889,92,86.28571429,93.01587302,95.65217391,90.52631579,97.4137931,90.47619048,100,100]

Salaries = [790,560,160,210,327.5,155,420,292.5,97.5,105,132.5,220,92.5,300,142.5,232.5,205,297.5,72.5,362.5,75,330,307.5,247.5,315,322.5,140,127.5,90,175,87.5,157.5,230,95,290,52.5,200,117.5]

names = ["გრძელიშვილი","ვახტანგაშვილი","აკოფიანი","მათე დოლიძე","ნარიმანიძე","ნავროზაშვილი","პაპუნაშვილი","აბაშიძე","წითლაური","ჯალაღონია","ხუსკივაძე","ყვავაძე","ვარადაშვილი","ფოფხაძე","იოანე დოლიძე","კილასონია","შავაძე","მოთიაშვილი","ბექაური","სამსონიძე","ვარაზაშვილი","აბრამიანი","გურგენიძე","შუბითიძე","ვანიშვილი","ზაბახიძე","ნუკრაძე","ფილიშვილი","გვრიტიშვილი","გუჯაბიძე","სვანიძე","მოწონელიძე","ძინძიბაძე","კვარაცხელია","გიორგელაშვილი","თირქია","ისაკაძე","ნუცუბიძე"]

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