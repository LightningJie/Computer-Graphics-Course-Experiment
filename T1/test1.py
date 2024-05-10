import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *

control_points = np.array([
    [[-1.5, -1.5, 4.0], [-0.5, -1.5, 2.0], [0.5, -1.5, -1.0], [1.5, -1.5, 2.0]],
    [[-1.5, -0.5, 1.0], [-0.5, -0.5, 3.0], [0.5, -0.5, 0.0], [1.5, -0.5, -1.0]],
    [[-1.5, 0.5, 4.0], [-0.5, 0.5, 0.0], [0.5, 0.5, 3.0], [1.5, 0.5, 4.0]],
    [[-1.5, 1.5, -2.0], [-0.5, 1.5, -2.0], [0.5, 1.5, 0.0], [1.5, 1.5, -1.0]]
])

rotate_x = 0
rotate_y = 0
mouse_pressed = False
last_x = 0
last_y = 0


def draw_bezier_surface():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -7.0)
    glRotatef(rotate_x, 1.0, 0.0, 0.0)
    glRotatef(rotate_y, 0.0, 1.0, 0.0)

    glColor3f(1.0, 1.0, 1.0)

    num_steps = 50

    for i in range(num_steps + 1):
        glBegin(GL_LINE_STRIP)
        for j in range(num_steps + 1):
            u = i / num_steps
            v = j / num_steps
            point = np.zeros(3)
            for k in range(4):
                for l in range(4):
                    point += control_points[k][l] * pow(u, k) * pow(1 - u, 3 - k) * pow(v, l) * pow(1 - v, 3 - l)
            glVertex3fv(point)
        glEnd()

        glBegin(GL_LINE_STRIP)
        for j in range(num_steps + 1):
            u = i / num_steps
            v = j / num_steps
            point = np.zeros(3)
            for k in range(4):
                for l in range(4):
                    point += control_points[l][k] * pow(u, l) * pow(1 - u, 3 - l) * pow(v, k) * pow(1 - v, 3 - k)
            glVertex3fv(point)
        glEnd()

    glutSwapBuffers()


def display():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_bezier_surface()
    glFlush()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    near = 1.0
    far = 100.0
    fov = 45.0
    aspect = width / height
    f_h = np.tan(np.radians(fov / 2.0)) * near
    f_w = f_h * aspect
    glFrustum(-f_w, f_w, -f_h, f_h, near, far)
    glMatrixMode(GL_MODELVIEW)


def special_keys(key, x, y):
    global rotate_x, rotate_y

    if key == GLUT_KEY_UP:
        rotate_x -= 5
    elif key == GLUT_KEY_DOWN:
        rotate_x += 5
    elif key == GLUT_KEY_LEFT:
        rotate_y -= 5
    elif key == GLUT_KEY_RIGHT:
        rotate_y += 5
    elif key == GLUT_KEY_HOME:
        rotate_x = 0
        rotate_y = 0

    glutPostRedisplay()


def mouse(button, state, x, y):
    global mouse_pressed, last_x, last_y

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            mouse_pressed = True
            last_x = x
            last_y = y
        elif state == GLUT_UP:
            mouse_pressed = False

    glutPostRedisplay()


def mouse_motion(x, y):
    global rotate_x, rotate_y, last_x, last_y

    if mouse_pressed:
        rotate_x += (y - last_y) * 0.1
        rotate_y += (x - last_x) * 0.1
        last_x = x
        last_y = y

    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Bezier Surface")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(special_keys)
    glutMouseFunc(mouse)
    glutMotionFunc(mouse_motion)
    glutMainLoop()


if __name__ == '__main__':
    main()