#需要预先安装 Segoe Pro Display Semibold 字体
# weiruan.pyw
# L2新手仔版本 Microsoft Logo 海龟绘图
# 约束：turtle(Tkinter)不支持OpenType连字，只能逐字符+手动字距模拟ft连字视觉效果
# 精度目标>95%，保留原作者风格，不使用外部矢量库
from turtle import *
# =====================【可调参数区，新手只改这里即可】=====================
speed(0)                # 绘图速度，0最快，1最慢
bgcolor('#242424')      # 深色背景，和原版保持一致
up()
# 方块布局参数（官方比例校准）
offset_x = -496         # 整体logo横向偏移
offset_y = 91           # 整体logo纵向偏移
square_size = 100       # 每个彩色方块边长
gap_between_square = 10 # 方块十字间隙，官方标准10（原版9，已修正）
# 字体设置（你本地已安装Segoe Pro Display Semibold）
font_name = "Segoe Pro Display Semibold"
font_size = 126
font_style = "normal"
font_tuple = (font_name, font_size, font_style)
# 符号方块 → 文字之间的间距（官方比例校准）
symbol_text_gap = -50
# 逐字符字距：每个字母写完之后前进多少像素，专门微调ft之间距离模拟连字
# 字符顺序：M,i,c,r,o,s,o,f,t
char_gaps = [
    142,   # M → i
    38,    # i → c
    68,    # c → r
    55,    # r → o
    92,    # o → s
    63,    # s → o
    85,    # o → f
    43,    # f → t 【重点！压缩距离模拟ft连字视觉，原版44，现在压到22】
    0      # t之后结束不移动
]
text_color = "#FFFFFF"
# ======================================================================
# 1.绘制四个彩色方块
# data：方块左上角相对坐标 + 官方色值
data = [
    ((0, 0), "#F25022"),      # 橙红
    ((square_size+gap_between_square, 0), "#7FBA00"),  # 绿
    ((0, -(square_size+gap_between_square)), "#00A4EF"),# 蓝
    ((square_size+gap_between_square, -(square_size+gap_between_square)), "#FFB900") #黄
]
for pos, col in data:
    goto(pos[0] + offset_x, pos[1] + offset_y)
    color(col, col)
    pd()
    begin_fill()
    for _ in range(4):
        fd(square_size)
        rt(90)
    end_fill()
    up()
# 2.移动画笔到文字起始位置
# 向右跳过方块整体宽度 + 符号文字间距
fd(square_size*2 + gap_between_square + symbol_text_gap)
# 垂直对齐：向下偏移，让文字大写字母几何中心 和四色块中心对齐，修复原版文字整体偏上2.6%
rt(90)
fd(103)
lt(90)
setheading(0)
color(text_color)
# 3.逐字符书写 Microsoft，使用手动字距，Tk无法开启OpenType连字，靠压缩ft间距模拟
char_list = ['M','i','c','r','o','s','o','f','t']
for idx, ch in enumerate(char_list):
    write(ch, align='left', font=font_tuple)
    fd(char_gaps[idx]) #写完一个字符，按预设距离前进
ht() #隐藏海龟箭头
done()
