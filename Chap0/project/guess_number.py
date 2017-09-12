#-*-coding:utf-8 -*-

#程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
#程序根据用户输入，给予一定提示（大了、小了、正确）
#猜对或用完 10 次机会，游戏结束

import random

num = random.randint(0,20)

times = 0
print("***现在开始玩猜数字的游戏！***\n")
print("猜一个大于0小于20的整数!")
print("你只有10次机会！")
guess = int(input(">>> "))
times = times + 1

while 0 <= guess <= 20:
    if times <= 10:
        if guess < num:
            print("小了，再猜一遍！")
        elif guess > num:
            print("大了，再猜一遍！")
        else:
            print("恭喜，你猜对了！")
            print("你一共猜了{}次。".format(times))
            break
        print("再输入一个数：")
        guess = int(input(">>> "))
        times = times + 1
    else:
        print("你猜的次数太多了，游戏结束")
        break

print("你猜的数不在范围以内，游戏结束！")
