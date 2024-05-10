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
def dda_algorithm(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1

  if abs(dx) > abs(dy):
    step = abs(dx)
  else:
    step = abs(dy)
  glBegin(GL_POINTS)
  xincr = float(dx) / step
  yincr = float(dy) / step
  x = float(x1)
  y = float(y1)

  for i in range(step):
    x += xincr
    y += yincr
    glVertex2f(x,y)
  glEnd()
  glFlush()
def bresenham_algorithm(x1, y1, x2, y2):
    glBegin(GL_POINTS)
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    if dx > 0:
        xi = 1
    else:
        xi = -1

    if dy > 0:
        yi = 1
    else:
        yi = -1

    if abs(dx) > abs(dy):
        ai = (abs(dy) - abs(dx)) * 2 #确定下一个d y+1
        bi = abs(dy) * 2 #确定下一个d  y
        d = bi - abs(dx) #判断条件 >0+1 <0 y

        while abs(x - x2) > 0:
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                x += xi
            glVertex2f(x, y)
    else:
        ai = (abs(dx) - abs(dy)) * 2
        bi = abs(dx) * 2
        d = bi - abs(dy)

        while abs(y - y2) > 0:
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                y += yi
            glVertex2f(x, y)
    glEnd()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0,0,1000,800)

    dda_algorithm(20, 0, 60, 120)
    dda_algorithm(60, 120, 100, 0)
    dda_algorithm(100, 0, 0, 80)
    dda_algorithm(0, 80, 120, 80)
    dda_algorithm(120, 80, 20, 0)

    bresenham_algorithm(140, 0, 180, 120)
    bresenham_algorithm(180, 120, 220, 0)
    bresenham_algorithm(220, 0, 120, 80)
    bresenham_algorithm(120, 80, 240, 80)
    bresenham_algorithm(240, 80, 140, 0)

    dda_algorithm(70, 100, 110, 220)
    dda_algorithm(110, 220, 150, 100)
    dda_algorithm(150, 100, 50, 180)
    dda_algorithm(50, 180, 170, 180)
    dda_algorithm(170, 180, 70, 100)
    #mid_point_algorithm(100, 0, 100, 500)
def winit():
    glClearColor(0.2, 0.2, 0.2, 1.0)
    glColor3d(1.0,1.0,1.0)
    gluOrtho2D(0.0,500.0,0.0,500.0)
    glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 400)
glutInitWindowPosition(500,250)
glutCreateWindow("123")
glutDisplayFunc(display)
winit()
glutMainLoop()

