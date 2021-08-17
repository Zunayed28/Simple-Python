def bmi_calculator(weight, height):
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        a = 'Score is {0:3.1f}. You are Underwight'.format(bmi)
        return a
    elif bmi >= 18.5 and bmi <= 24.9:
        a = 'Score is {0:3.1f}. You are Normal'.format(bmi)
        return a
    elif bmi >= 25 and bmi <= 30:
        a = 'Score is {0:3.1f}. You are Overwight'.format(bmi)
        return a
    else:
        a = 'Score is {0:3.1f}. You are Obese'.format(bmi)
        return a


print(bmi_calculator(height = float(input()), weight = float(input())))
