from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
a=0 #Times
import sys
sys.setrecursionlimit(1000000) #Crack recursion limit

def draw():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-30, 30)
    glVertex2f(-30, 20)
    glVertex2f(-30, 20)
    glVertex2f(0, 20)
    glVertex2f(0, 20)
    glVertex2f(0, 10)
    glVertex2f(0, 10)
    glVertex2f(-30, 10)
    glVertex2f(-30, 10)
    glVertex2f(-30, 0)
    glVertex2f(-30, 0)
    glVertex2f(0, 0)
    glVertex2f(0, 0)
    glVertex2f(0, -10)
    glVertex2f(0, -10)
    glVertex2f(-30, -10)
    glVertex2f(-30, -10)
    glVertex2f(-30, -20)
    glVertex2f(-30, -20)
    glVertex2f(40, -20)
    glVertex2f(-30, 30)
    glVertex2f(40, 30)
    glVertex2f(40, 30)
    glVertex2f(40, 20)
    glVertex2f(40, 20)
    glVertex2f(10, 20)
    glVertex2f(10, 20)
    glVertex2f(10, 10)
    glVertex2f(10, 10)
    glVertex2f(40, 10)
    glVertex2f(40, 10)
    glVertex2f(40, 0)
    glVertex2f(40, 0)
    glVertex2f(10, 0)
    glVertex2f(10, 0)
    glVertex2f(10, -10)
    glVertex2f(10, -10)
    glVertex2f(40, -10)
    glVertex2f(40, -10)
    glVertex2f(40, -20)
    glEnd()
    fill(-5,20,255)


def fill(x,y,boundaryvalue):
    global a
    a=a+1
    print(a)
    if getpixel(x,y)!=boundaryvalue:
        setpixel(x,y)
        fill(x,y-1,boundaryvalue)
        fill(x,y+1,boundaryvalue)
        fill(x-1,y,boundaryvalue)
        fill(x+1,y,boundaryvalue)

def setpixel(x,y):
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(x,y)
    glEnd()
    glFlush()
def getpixel(x,y):
    a = (GLuint * 1)(0)
    glReadPixels(x+100, y+100, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, a)
    return int(a[0])

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(200,200)
glutCreateWindow("HiddenStrawberry")
glLoadIdentity()
gluOrtho2D(-100,100,-100,100)
glutDisplayFunc(draw)
glutMainLoop()