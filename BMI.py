# function for calculating BMI based on inputted weight in lbs and height in inches
def BMI(h, w):
    w *= 0.45
    h *= 0.025
    h2 = h * h
    bmi = round(w / h2, 1)

    cat = 'NONE'

    if bmi < 18.5:
        cat = 'Underweight'

    elif bmi >= 18.5 and bmi <= 24.9:
        cat = 'Normal'

    elif bmi > 24.9 and bmi <= 29.9:
        cat = 'Overweight'

    else:
        cat = 'Obese'

    out_list = [bmi, cat]

    return out_list
