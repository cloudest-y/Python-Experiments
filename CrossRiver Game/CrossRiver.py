#coding:utf-8
from prettytable import PrettyTable
#游戏介绍
print"————————————游戏介绍——————————————"
print"| 现在右岸有3名传教士和3名野人，你需要将他们都运送到左岸   |"
print"| 现在又一艘船在右岸，一次最多搭载2人，船上无人不能航行    |"
print"| 任意一岸出现野人数多于传教士人数，则游戏结束。           |"
print"——————————————————————————————"
start = PrettyTable(["左岸传教士", "左岸野人", "船", "右岸传教士", "右岸野人"])
start.align["左岸传教士"] = "l"  # Left align city names
start.padding_width = 1  # One space between column edges and contents (default)
start.add_row([0,0,1,3,3])
print start

#初始状态
c=3#左岸传教士数
w=3#左岸野人数
b=1#左岸有几个船
x,y=(0,0)#船上人数（c,w）
for i in range(15):
    x,y=input("请输入运送的人数：（c,w）\n")
    if b == 1:
        if (c + w) < (x + y) or x + y <= 0 or x + y > 2:
            print "上船人数不合理，请重新输入上船人数"
            x, y = input("请重新输入运送的人数：（c,w）\n")
            # 判断left上船人数合理
    if b == 0:
        if (6 - c - w) < (x + y) or x + y <= 0 or x + y > 2:
            print "上船人数不合理，请重新输入上船人数"
            x, y = input("请重新输入运送的人数：（c,w）\n")
            # 判断right上船人数合理

    m = (i % 2) + 1
    c = ((-1) ** m) * x + c
    w = ((-1) ** m) * y + w
    b = i % 2

    # 判断当前状态合理
    if c == w or c == 3 or c == 0:
        # 显示结果
        table = PrettyTable(["左岸传教士", "左岸野人", "船", "右岸传教士", "右岸野人"])
        table.align["左岸传教士"] = "l"  # Left align city names
        table.padding_width = 1  # One space between column edges and contents (default)
        table.add_row([3 - c, 3 - w, b, c, w])
        print table
        if c + w + b == 0:
            print"**********SUCCESS!**************"
            break
    else:
        print"*********GAME OVER!*************"







