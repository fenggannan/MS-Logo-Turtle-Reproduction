from turtle import *
speed(0)
up()
bgcolor('#242424')
offset_x = -496
offset_y = 91
data = [((0,0),"#F25022"), ((110,0),"#7FBA00"), ((0,-110),"#00A4EF"), ((110,-110),"#FFB900")]
for pos, col in data:
    goto(pos[0] + offset_x, pos[1] + offset_y)
    color(col, col)
    pd()
    begin_fill()
    for _ in range(4):
        fd(100)
        rt(90)
    end_fill()
    up()
fd(151)
rt(90)
fd(96)
setheading(0)
color('#FFFFFF')
write('Microsof', align='left', font=('Segoe UI Semibold', 126, 'normal'))
fd(664)
write('t', align='left', font=('Segoe UI Semibold', 126, 'normal'))
ht()
done()
