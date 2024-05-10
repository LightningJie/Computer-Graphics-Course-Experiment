from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time


def draw_celestial_body(distance, radius, angle, color):
    glPushMatrix()
    glRotatef(angle, 0, 1, 0)
    glTranslatef(distance, 0, 0)
    glColor3fv(color)
    glutWireSphere(radius, 20, 20)
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_celestial_body(0, 1, 0, (1, 1, 0))  # sun
    draw_celestial_body(5, 0.3, time.time() * 10, (0, 0, 1))  # earth
    glTranslatef(5, 0, 0)
    glRotatef(time.time() * 20, 0, 1, 0)
    draw_celestial_body(1, 0.1, time.time() * 30, (0.7, 0.7, 0.7))  # moon

    glutSwapBuffers()


def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 50)
    glMatrixMode(GL_MODELVIEW)


def update(value):
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Solar System Animation")

    glutDisplayFunc(display)
    glutTimerFunc(10, update, 0)

    init()

    glutMainLoop()


if __name__ == "__main__":
    main()