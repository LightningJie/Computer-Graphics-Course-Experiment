from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# 全局变量
rotation = 0.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 800, 0, 600)

def draw():
    global rotation

    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glTranslatef(400, 300, 0)
    glRotatef(rotation, 0.0, 0.0, 1.0)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-50, -50)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0, 50)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(50, -50)
    glEnd()

    glPopMatrix()

    glFlush()

def animate(value):
    global rotation

    rotation += 1.0

    glutPostRedisplay()
    glutTimerFunc(1000//60, animate, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow("OpenGL Animation")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

if __name__ == '__main__':
    main()