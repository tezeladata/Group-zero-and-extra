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

calculate_work(77.17647059, 212.5, "გაგნიძე")
calculate_work(75.40540541, 185, "ბერიძე")    
calculate_work(87.3015873, 315, "ჯანეზაშვილი") 
calculate_work(91.29251701, 367.5, "გიორგელაშვილი") 
calculate_work(69.75609756, 102.5, "თინიკაშვილი")
calculate_work(58.66666667, 75, "ამონაშვილი")   
calculate_work(52.38095238, 52.5, "თაქთაქიძე")   
calculate_work(87.04225352, 177.5, "ნავროზაშვილი")
calculate_work(92.30769231, 292.5, "ვანიშვილი")  
calculate_work(93.39622642, 265, "ზაბახიძე")      
calculate_work(91.89189189, 185, "რაზმაძე")     
calculate_work(92.7027027, 185, "ვახტანგაშვილი") 
calculate_work(95.96330275, 272.5, "მოთიაშვილი")
calculate_work(94.83870968, 155, "დიასამიძე") 
calculate_work(96.09756098, 205, "ჯანაშია")      
calculate_work(70.90909091, 27.5, "არღუთაშვილი") 
calculate_work(96.20253165, 197.5, "ფოფხაძე")   
calculate_work(93.33333333, 112.5, "თირქია")     
calculate_work(84.44444444, 45, "ლევერაშვილი")    
calculate_work(93.63636364, 110, "ნუცუბიძე")    
calculate_work(97.10843373, 207.5, "საზანდრიშვილი")
calculate_work(95.55555556, 90, "მოლოდინი")    
calculate_work(97.77777778, 180, "ბაბაჯანაშვილი") 
calculate_work(99.05405405, 370, "გრძელიშვილი")  
calculate_work(80, 15, "დოლიძე")              
calculate_work(96.96969697, 82.5, "ბერკაცაშვილი")  
calculate_work(99.33884298, 302.5, "თეზელაშვილი") 
calculate_work(73.33333333, 7.5, "ტყეშელაშვილი")  
calculate_work(96.19047619, 52.5, "ქიმერიძე")    
calculate_work(100, 85, "გურგენიძე")           
calculate_work(100, 30, "შავაძე")           
calculate_work(100, 7.5, "სიხარულიძე")         
calculate_work(100, 7.5, "მოწონელიძე")      
calculate_work(100, 37.5, "ხუსკივაძე")       
calculate_work(100, 37.5, "სვანიძე") 
calculate_work(73.33333333, 142.5, "ფილიშვილი")          

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