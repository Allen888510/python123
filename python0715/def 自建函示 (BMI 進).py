def BMI(h, w):
    bmi = w/((h/100)**2)
    return bmi

bmi = BMI(180, 75)
print("%.2f" % bmi)

bmi = BMI(150, 30)
print(bmi)

bmi = BMI(160, 50)
print("%.3f" % bmi)

