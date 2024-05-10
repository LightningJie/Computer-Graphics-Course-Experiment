from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0.1
        self.height = 0.1

    def draw(self):
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(self.x - self.width / 2, self.y - self.height / 2)
        glVertex2f(self.x + self.width / 2, self.y - self.height / 2)
        glVertex2f(self.x + self.width / 2, self.y + self.height / 2)
        glVertex2f(self.x - self.width / 2, self.y + self.height / 2)
        glEnd()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class Target:
    def __init__(self):
        self.width = 0.2
        self.height = 0.2
        self.generate_random_position()

    def generate_random_position(self):
        self.x = random.uniform(-0.9, 0.9)
        self.y = random.uniform(-0.9, 0.9)

    def draw(self):
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(self.x - self.width / 2, self.y - self.height / 2)
        glVertex2f(self.x + self.width / 2, self.y - self.height / 2)
        glVertex2f(self.x + self.width / 2, self.y + self.height / 2)
        glVertex2f(self.x - self.width / 2, self.y + self.height / 2)
        glEnd()


class Scoreboard:
    def __init__(self):
        self.score = 0

    def update_score(self):
        self.score += 1

    def draw(self):
        glPushMatrix()
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
        glColor3f(1.0, 1.0, 1.0)
        glRasterPos2f(-0.9, 0.9)
        text = "Score: " + str(self.score)
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()


def initialize():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


player = Player(0.0, 0.0)
target = Target()
scoreboard = Scoreboard()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    player.draw()
    target.draw()
    scoreboard.draw()

    glFlush()


def keyboard(key, x, y):
    speed = 0.1
    if key == b'w':
        player.move(0, speed)
    elif key == b's':
        player.move(0, -speed)
    elif key == b'a':
        player.move(-speed, 0)
    elif key == b'd':
        player.move(speed, 0)

    # 检测碰撞
    if abs(player.x - target.x) < player.width / 2 + target.width / 2 and abs(
            player.y - target.y) < player.height / 2 + target.height / 2:
        scoreboard.update_score()
        target.generate_random_position()

    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow("OpenGL Game")
    initialize()
    glutDisplayFunc(draw)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == '__main__':
    main()