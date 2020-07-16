def printBMI(h, w):
    bmi = w/((h/100)**2)
    result = "過重" if bmi>23 else "過輕" if bmi<18 else "正常"
    print("身高為%.1f, 體重為%.1f, bmi值為%.2f, (%s)"%(h, w, bmi, result))

printBMI(181, 50)