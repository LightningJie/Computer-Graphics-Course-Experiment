from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def mid_point_algorithm(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if dx == 0:
        # 处理斜率为0的情况
        k = 0
    else:
        k = dy / dx

    # 计算中点画线算法所需参数
    x = x0
    y = y0
    dx = abs(dx)
    dy = abs(dy)
    s1 = 1 if x1 > x0 else -1
    s2 = 1 if y1 > y0 else -1
    swapped = False
    if dy > dx:
        # 如果斜率大于1，则交换x轴和y轴
        dx, dy = dy, dx
        swapped = True

    # 初始化中点参数
    p = 2 * dy - dx
    glBegin(GL_POINTS)
    if not swapped:
        # 绘制x轴增加方向的直线
        while x != x1:
            glVertex2f(x, y)
            if p >= 0:
                y += s2
                p -= 2 * dx
            x += s1
            p += 2 * dy
    else:
        # 绘制y轴增加方向的直线
        while y != y1:
            glVertex2f(x, y)
            if p >= 0:
                x += s1
                p -= 2 * dx
            y += s2
            p += 2 * dy
    glEnd()
    glFlush()
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0,0,1000,800)
    # mid_point_algorithm(20,0,20,120)
    # mid_point_algorithm(20, 120, 100, 120)
    # mid_point_algorithm(100, 120, 100, 0)
    # mid_point_algorithm(100, 0, 20, 0)
    mid_point_algorithm(0, 5, 9, 0)
def winit():
    glClearColor(0.2, 0.2, 0.2, 1.0)
    glColor3d(1.0,1.0,1.0)
    gluOrtho2D(0.0,500.0,0.0,500.0)
    glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(100, 80)
glutInitWindowPosition(50,25)
glutCreateWindow("123")
glutDisplayFunc(display)
winit()
glutMainLoop()

