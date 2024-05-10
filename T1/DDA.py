from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


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

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0,0,1000,800)
    dda_algorithm(20,0,60,120)
    dda_algorithm(60,120,100,0)
    dda_algorithm(100, 0, 0, 80)
    dda_algorithm(0, 80, 120, 80)
    dda_algorithm(120, 80, 20, 0)
def winit():
    glClearColor(0.2, 0.2, 0.2, 1.0)
    #glColor3d(1.0,1.0,1.0)
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

