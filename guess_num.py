import random
r = random.randint(1,10)
i = 0
while True:
    num = input("請猜數字:")
    num = int(num)
    i = i + 1
    if num == r:
        print("你猜對了")
        print("共猜了",i,"次")
        break
    else:
        if num > r:
           print("要更小") 
        else:
           print("要更大") 
    print("你猜了第",i,"次")

