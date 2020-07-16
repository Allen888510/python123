#完整的BMI計算系統

def calc():
    h = float(input("請輸入身高:"))
    w = float(input("請輸入體重:"))
    bmi = w/((h/100)**2)
    result = "過重" if bmi>23 else "過輕" if bmi<18 else "正常"
    print("身高為%.1f, 體重為%.1f, bmi值為%.2f, (%s)"%(h, w, bmi, result))

def menu():
    print("BMI計算系統")
    print("---------")
    print("1. 輸入身高與體重")
    print("2. 離開系統")
    id = int(input("請選擇:"))
    if id == 1:
        calc()
        menu()
    elif id == 2:
        print("謝謝您的使用")
    else:
        print("選擇錯誤")
        menu()

menu()