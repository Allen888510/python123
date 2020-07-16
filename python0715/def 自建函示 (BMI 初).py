def BMI():
    h = float(input("請輸入身高:"))
    w = float(input("請輸入體重:"))
    bmi = w/ ((h/100)**2)
    print("%6.3f"%bmi)

BMI()