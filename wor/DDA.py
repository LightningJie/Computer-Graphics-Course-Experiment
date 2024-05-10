#import pygame
from OpenGL.GL import *

def draw_line_DDA(x1, y1, x2, y2):
    glBegin(GL_POINTS)

    # 计算直线斜率
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    x_increment = dx / steps
    y_increment = dy / steps
    x = x1
    y = y1

    # 生成每个坐标点的值
    for i in range(steps):
        glVertex2fv((x, y))
        x += x_increment
        y += y_increment

    glEnd()