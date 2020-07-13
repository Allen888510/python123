import random
#決定比大(輸入1) 比小(輸入0)

flag = int(input("比大(輸入1)還是比小(輸入0):"))
user = random.randint(1, 6)+random.randint(1, 6)+random.randint(1, 6)
pc = random.randint(1, 6)+random.randint(1, 6)+random.randint(1, 6)
if flag==1:
    winner = "使用者" if user > pc else "電腦"
else:
    winner = "電腦" if pc > user else "使用者"
result = "比{0}, 使用者的點數:{1}, 電腦的點數:{2}, 贏家:{3}"\
    .format("大" if flag==1 else "小", user, pc, winner)
print(result)
