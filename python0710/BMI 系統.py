#可輸入 (人名, 身高, 體重)
#可算出BMI值
#資料呈現 ___的身高為___._cm 體重為___._kg bmi值為__.__ (正常 , 過高 , 過低 )

print("BMI系統")
Name = input("請輸入姓名:")
h = float(input("請輸入身高:"))
w = float(input("請輸入體重:"))
bmi = w/((h/100)**2)
#print(bmi) (基本)

result = "正常" if 18<bmi<=23 else "過高" if bmi>23 else "過輕"
print("%s的身高%5.1f, 體重為%5.1f, bmi值為%5.2f (%s)"%
      (Name, h, w, bmi, result))  #(進階)