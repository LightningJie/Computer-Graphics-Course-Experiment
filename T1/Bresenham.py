from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


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
    # bresenham_algorithm(20,0,60,120)
    # bresenham_algorithm(60, 120, 100, 0)
    # bresenham_algorithm(100, 0, 20, 0)
    bresenham_algorithm(1, 0, 10, 4)
def winit():
    glClearColor(0.2, 0.2, 0.2, 1.0)
    glColor3d(1.0,1.0,1.0)
    gluOrtho2D(0.0,300.0,0.0,300.0)
    glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(200, 160)
glutInitWindowPosition(500,250)
glutCreateWindow("123")
glutDisplayFunc(display)
winit()
glutMainLoop()

