#雞加兔共83隻，雞的腳加兔的腳共240隻，求雞和兔個幾隻？

#設全部為雞 共2x83=166隻腳
#240-166=74隻腳
#兔子共有74/2=37隻
#雞共有83-37=46隻

def calc(x, y):
    a = 2 * x
    b = y - a
    rabbit = b/2
    return x - rabbit, rabbit

chicken, rabbit = calc(83, 240)
print("雞共有%d隻, 兔子共有%d隻"%(chicken,rabbit))

