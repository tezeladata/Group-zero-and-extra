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

calculate_work(52.62135922, 257.5, 'ბაბაჯანაშვილი')
calculate_work(75.23809524, 315, 'ჯანეზაშვილი')
calculate_work(0, 60, 'დოლიძე')
calculate_work(38.53658537, 102.5, 'ნუცუბიძე')
calculate_work(76.76767677, 247.5, 'საზანდრიშვილი')
calculate_work(81.06666667, 187.5, 'ნავროზაშვილი')
calculate_work(76.84210526, 142.5, 'ფილიშვილი')
calculate_work(80.61538462, 162.5, 'ვახტანგაშვილი')
calculate_work(87.90697674, 215, 'ბერიძე')
calculate_work(86.83544304, 197.5, 'ჯანაშია')
calculate_work(80.37735849, 132.5, 'თირქია')
calculate_work(79.18367347, 122.5, 'თინიკაშვილი')
calculate_work(75.33333333, 75, 'ლევერაშვილი')
calculate_work(95.13513514, 370, 'გიორგელაშვილი')
calculate_work(93.6, 250, 'რაზმაძე')
calculate_work(91.89873418, 197.5, 'ფოფხაძე')
calculate_work(94.87179487, 292.5, 'ვანიშვილი')
calculate_work(95.34883721, 322.5, 'გაგნიძე')
calculate_work(96.875, 400, 'გრძელიშვილი')
calculate_work(95.71428571, 280, 'ზაბახიძე')
calculate_work(96.36363636, 302.5, 'თეზელაშვილი')
calculate_work(94.52054795, 182.5, 'მოთიაშვილი')
calculate_work(80.95238095, 52.5, 'ქიმერიძე')
calculate_work(96.12903226, 155, 'დიასამიძე')
calculate_work(95.55555556, 90, 'მოლოდინი')
calculate_work(92.38095238, 52.5, 'ამონაშვილი')
calculate_work(89.09090909, 27.5, 'არღუთაშვილი')
calculate_work(97.57575758, 82.5, 'ბერკაცაშვილი')
calculate_work(100, 52.5, 'ბაკურაძე')
calculate_work(100, 85, 'გურგენიძე')
calculate_work(100, 50, 'შავაძე')
calculate_work(100, 22.5, 'მოწონელიძე')
calculate_work(100, 22.5, 'ხუსკივაძე')
calculate_work(100, 22.5, 'სვანიძე')
calculate_work(100, 15, 'კილასონია')
calculate_work(100, 7.5, 'ტყეშელაშვილი')
calculate_work(100, 7.5, 'სიხარულიძე')

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