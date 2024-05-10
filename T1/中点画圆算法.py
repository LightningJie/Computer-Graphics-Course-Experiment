from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# 定义圆的属性
circle_radius = 0.5
circle_precision = 100
circle_center = [0.0, 0.0]

# 定义正多边形的属性
n = 8
polygon_radius = 1.0
polygon_center = [0.0, 0.0]
polygon_angles = [2 * math.pi * i / n for i in range(n)]

# 进行一些 OpenGL 初始化工作
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)

# 绘制中点画圆算法生成的圆
def draw_circle_midpoint(radius, precision):
    glBegin(GL_LINE_LOOP)
    angle_step = 2 * math.pi / precision
    angle = angle_step
    x, y = radius, 0
    for _ in range(precision):
        glVertex2f(x + circle_center[0], y + circle_center[1])
        x, y = x * math.cos(angle) - y * math.sin(angle), \
               x * math.sin(angle) + y * math.cos(angle)
        angle += angle_step
    glEnd()

# 绘制 Bresenham 画圆算法生成的圆
def draw_circle_bresenham(radius, precision):
    glBegin(GL_LINE_LOOP)
    angle_step = 2 * math.pi / precision
    angle = 0
    for _ in range(precision):
        x, y = radius * math.cos(angle), radius * math.sin(angle)
        glVertex2f(x + circle_center[0], y + circle_center[1])
        angle += angle_step
    glEnd()

# 绘制正多边形
def draw_polygon(n, radius, angles):
    glBegin(GL_LINE_LOOP)
    for angle in angles:
        x, y = radius * math.cos(angle), radius * math.sin(angle)
        glVertex2f(x + polygon_center[0], y + polygon_center[1])
    glEnd()

# 绘制函数
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 绘制中点画圆算法生成的圆
    glColor3f(1.0, 0.0, 0.0)
    draw_circle_midpoint(circle_radius, circle_precision)

    # 绘制 Bresenham 画圆算法生成的圆
    glColor3f(0.0, 1.0, 0.0)
    draw_circle_bresenham(2 * circle_radius, circle_precision)

    # 绘制正多边形
    glColor3f(0.0, 0.0, 1.0)
    draw_polygon(n, polygon_radius, polygon_angles)

    glFlush()

# 进行绘制相关的初始化工作
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(400, 400)
glutCreateWindow("OpenGL Test")

# 注册绘制函数
glutDisplayFunc(display)

# 初始化 OpenGL
init()
glutMainLoop()