from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_LINE_STRIP)
    for x in np.arange(0.01, 2.0, 0.01):
        y = np.log(x)
        glVertex2f(x, y)
    glEnd()

    glFlush()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 2.0, -5.0, 5.0)


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow("Logarithmic Function")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glClearColor(0.0, 0.0, 0.0, 0.0)
glutMainLoop()