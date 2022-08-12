"""
Copyright (c) 2022.
FileName: drawUkraineFlag.py
Brief: 绘制乌克兰国旗。
Author: 青羽
Blog: https://chen-qingyu.github.io
CreateDate: 2022.05.18
"""

import turtle

# 此变量唯一决定旗面相对大小
UNIT = 25

WIDTH = UNIT * 30  # 旗面宽度
HEIGHT = UNIT * 20  # 旗面高度

# 颜色 https://www.schemecolor.com/ukraine-flag-colors.php
colors = {"Sapphire": "#005BBB", "Cyber Yellow": "#FFD500"}

# Initial
turtle.mode("standard")  # Initial turtle heading: to the right (east), positive angles: counterclockwise
turtle.speed("fast")
turtle.title("乌克兰国旗")
turtle.setup(WIDTH * 1.1, HEIGHT * 1.1)
turtle.bgcolor("#F0F0F0")
turtle.penup()

# Draw
i = 0
for color in colors.keys():
    turtle.goto(-WIDTH / 2, HEIGHT / 2 - (HEIGHT / len(colors)) * i)
    turtle.setheading(0)
    turtle.fillcolor(colors[color])
    turtle.begin_fill()
    for j in range(2):
        turtle.forward(WIDTH)
        turtle.right(90)
        turtle.forward(HEIGHT / len(colors))
        turtle.right(90)
    turtle.end_fill()
    i += 1

turtle.hideturtle()
turtle.mainloop()
