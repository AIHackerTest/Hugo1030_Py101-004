#-*-coding:utf-8 -*-

import random

#用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零
def get_num():
    num = random.sample(range(10), 4)
    while num[0] == 0: #如果首位为0将再次循环，直到首位不为0
        num = random.sample(num, 4)
    return num

#输入4位数，并把该数按位分离
def get_answer():
    print("猜个4位数:")
    answer = int(input(">>> "))
    if 1000 <= answer <= 9999:
        a = int (answer / 1000)
        b = int (answer % 1000 / 100)
        c = int (answer % 100 / 10)
        d = int (answer % 10)

        answer = [a, b, c, d]
        return answer

#返回 A 和 B 的个数   
def check_num(num, answer):
    x = 0
    y = 0
    for i in range(4):
        if answer[i] == num[i]:
            x += 1
    for n in answer:
        if n in num:
            y += 1
    z = y - x
    return x, z

def main():
    try:
        print("***欢迎来玩'猜数字xAyB游戏' V1.0！***")
        times = 0
        num = get_num()
        while True:
            print("这是你第{}次猜数字。".format(times + 1))
            answer = get_answer()
            times += 1
            x, z = check_num(num, answer)
            print("{}A{}B".format(x, z))
            if times > 10:
                print("你猜的次数太多了！")
                break
            elif x == 4:
                print("恭喜你！猜对了！")
                print("你一共猜了{}次。".format(times))
                break
    except Exception as e:
        print("数据异常！")
        
if __name__ == '__main__':
    main()
