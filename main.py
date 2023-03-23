print("Calculation of the daily calorie norm is based on the Mifflin-Geor formula")
male = input("Enter your gender (Male/Female): ")
weight = int(input("Enter your weight in kilograms: "))
height = int(input("Enter your height in centimeters: "))
age = int(input("Enter your age: "))

kdj = 4.1868
if male == 'Male' or 'male':
    man_kcal = (10*weight)+(6.25*height)-(5*age)+5
    kdj_res = man_kcal * kdj
    print("Your basal metabolism: ",man_kcal, "kcal")
    print(kdj_res, 'kJ')
else:
    woman_kcal = (10*weight)+(6.25*height)-(5*age)-161
    kdj_res = woman_kcal * kdj
    print("Your basal metabolism: ",woman_kcal, "kcal")
    print(kdj_res, 'kJ')
#--------------------------------------------------------
print("Calculation of the daily rate of energy consumption")


kfa = input('Coefficient of physical activity (weak; moderate; intense): ')

low = 1
medium = 1.3
hight = 1.5

# drec - daily rate of energy consumption (добова норма енергоспоживання)
if kfa == 'weak':
    if male == 'Male' or 'male':
        if age < 18:
            drec_below18 = (0.063*weight+2.896)*240*1
            print("Your daily calorie allowance: ", drec_below18, 'kcal')
        elif age in range(18,30):
            drec18_30 = (0.063 * weight + 2.896) * 240 * 1
            print("Your daily calorie allowance: ", drec18_30, 'kcal')
        elif age in range(31,60):
            drec31_60 = (0.0484 * weight + 3.653) * 240 * 1
            print("Your daily calorie allowance: ", drec31_60, 'kcal')
        else: # age1 > 60
            drec_highter60 = (0.0491 * weight + 2.459) * 240 * 1
            print("Your daily calorie allowance: ", drec_highter60, 'kcal')
    else:
        if age < 18:
            drec_below18 = (0.062*weight+2.036)*240*1
            print("Your daily calorie allowance: ", drec_below18, 'kcal')
        elif age in range(18,30):
            drec18_30 = (0.062*weight+2.036)*240*1
            print("Your daily calorie allowance: ", drec18_30, 'kcal')
        elif age in range(31,60):
            drec31_60 = (0.034 * weight + 3.538) * 240 * 1
            print("Your daily calorie allowance: ", drec31_60, 'kcal')
        else: # age1 > 60
            drec_highter60 = (0.038 * weight + 2.755) * 240 * 1
            print("Your daily calorie allowance: ", drec_highter60, 'kcal')
elif kfa == 'moderate':
    if male == 'Male' or 'male':
        if age < 18:
            drec_below18 = (0.063*weight+2.896)*240*1.3
            print("Your daily calorie allowance: ", drec_below18, 'kcal')
        elif age in range(18,30):
            drec18_30 = (0.063 * weight + 2.896) * 240 * 1.3
            print("Your daily calorie allowance: ", drec18_30, 'kcal')
        elif age in range(31,60):
            drec31_60 = (0.0484 * weight + 3.653) * 240 * 1.3
            print("Your daily calorie allowance: ", drec31_60, 'kcal')
        else: # age1 > 60
            drec_highter60 = (0.0491 * weight + 2.459) * 240 * 1.3
            print("Your daily calorie allowance: ", drec_highter60, 'kcal')
    else:
        if age < 18:
            drec_below18 = (0.062*weight+2.036)*240*1.3
            print("Your daily calorie allowance: ", drec_below18, 'kcal')
        elif age in range(18,30):
            drec18_30 = (0.062*weight+2.036)*240*1.3
            print("Your daily calorie allowance: ", drec18_30, 'kcal')
        elif age in range(31,60):
            drec31_60 = (0.034 * weight + 3.538) * 240 * 1.3
            print("Your daily calorie allowance: ", drec31_60, 'kcal')
        else: # age1 > 60
            drec_highter60 = (0.038 * weight + 2.755) * 240 * 1.3
            print("Your daily calorie allowance: ", drec_highter60, 'kcal')
else:
    if male == 'Male' or 'male':
        if age < 18:
            drec_below18 = (0.063*weight+2.896)*240*1.5
            print("Your daily calorie allowance: ", drec_below18, 'kcal')
        elif age in range(18,30):
            drec18_30 = (0.063 * weight + 2.896) * 240 * 1.5
            print("Your daily calorie allowance: ", drec18_30, 'kcal')
        elif age in range(31,60):
            drec31_60 = (0.0484 * weight + 3.653) * 240 * 1.5
            print("Your daily calorie allowance: ", drec31_60, 'kcal')
        else: # age1 > 60
            drec_highter60 = (0.0491 * weight + 2.459) * 240 * 1.5
            print("Your daily calorie allowance: ", drec_highter60, 'kcal')
    else:
        if age < 18:
            drec_below18 = (0.062*weight+2.036)*240*1.5
            print("Your daily calorie allowance: ", drec_below18, 'kcal')
        elif age in range(18,30):
            drec18_30 = (0.062*weight+2.036)*240*1.5
            print("Your daily calorie allowance: ", drec18_30, 'kcal')
        elif age in range(31,60):
            drec31_60 = (0.034 * weight + 3.538) * 240 * 1.5
            print("Your daily calorie allowance: ", drec31_60, 'kcal')
        else: # age1 > 60
            drec_highter60 = (0.038 * weight + 2.755) * 240 * 1.5
            print("Your daily calorie allowance: ", drec_highter60, 'kcal')

