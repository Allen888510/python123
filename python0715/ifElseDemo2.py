def getBMI(h, w):
    bmi = w/((h/100)**2)
    result = "過重" if bmi>23 else "過輕" if bmi<18 else "正常"
    return bmi, result, h, w

bmi, result, h, w = getBMI(181.2, 75)
print("身高為%.fcm, 體重為%.fkg, bmi值為%.2f,(%s)"%(h, w, bmi, result))