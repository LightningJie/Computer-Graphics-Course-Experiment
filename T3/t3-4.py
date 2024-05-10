import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
import random
from math import pi as PI
from math import sin, cos
from math import sqrt
import numpy as np
# 游戏窗口大小
WIDTH = 800
HEIGHT = 600

# 玩家坐标
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_speed = 5

# 子弹坐标和速度
bullet_x = 0
bullet_y = -1
bullet_speed = 10
bullet_radius = 5
bullet_fired = False

# 敌人坐标和速度
enemy_x = 0
enemy_y = 0
enemy_speed = 3

# 打中敌人计数
score = 0


# 绘制玩家角色
def draw_player():
    glColor3f(1, 0, 0)  # 设置颜色为红色
    glBegin(GL_TRIANGLES)
    glVertex2f(player_x, player_y - 25)
    glVertex2f(player_x - 25, player_y + 25)
    glVertex2f(player_x + 25, player_y + 25)
    glEnd()


# 绘制子弹
def draw_bullet():
    global bullet_fired, bullet_x, bullet_y

    if bullet_fired:
        glColor3f(0, 0, 1)  # 设置颜色为蓝色
        num_segments = 50
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(bullet_x, bullet_y)
        for i in range(num_segments + 1):
            theta = 2.0 * math.pi * float(i) / float(num_segments)
            x = bullet_x + bullet_radius * math.cos(theta)
            y = bullet_y + bullet_radius * math.sin(theta)
            glVertex2f(x, y)
        glEnd()

        bullet_y -= bullet_speed

        # 子弹超出屏幕范围则停止绘制
        if bullet_y < 0:
            bullet_fired = False


# 绘制敌人
def draw_enemy():
    glColor3f(0, 1, 0)  # 设置颜色为绿色
    glRectf(enemy_x - 25, enemy_y - 25, enemy_x + 25, enemy_y + 25)


# 检测碰撞
def check_collision():
    global bullet_fired, bullet_x, bullet_y, enemy_x, enemy_y, score

    if bullet_fired and bullet_x >= enemy_x - 25 and bullet_x <= enemy_x + 25 and bullet_y >= enemy_y - 25 and bullet_y <= enemy_y + 25:
        bullet_fired = False
        score += 1
        print("命中敌人！得分:", score)
        reset_enemy()


# 重置敌人位置
def reset_enemy():
    global enemy_x, enemy_y
    enemy_x = random.randint(50, WIDTH - 50)
    enemy_y = 0


# 移动敌人
def move_enemy(value):
    global enemy_x, enemy_y

    if enemy_y > HEIGHT:
        reset_enemy()

    enemy_y += enemy_speed

    glutPostRedisplay()
    glutTimerFunc(30, move_enemy, 0)


# 绘制回调函数
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_player()
    draw_bullet()
    draw_enemy()
    check_collision()
    glutSwapBuffers()


# 设置窗口和回调函数
def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"123")
    gluOrtho2D(0, WIDTH, 0, HEIGHT)
    glutDisplayFunc(draw)
    glutKeyboardFunc(handle_keys)


# 更新窗口内容
def update(value):
    glutPostRedisplay()
    glutTimerFunc(30, update, 0)


# 处理键盘事件
def handle_keys(key, x, y):
    global player_x, bullet_fired, bullet_x, bullet_y

    if key == b'a':
        player_x -= player_speed
    elif key == b'd':
        player_x += player_speed
    elif key == b'j' and not bullet_fired:
        bullet_fired = True
        bullet_x = player_x
        bullet_y = player_y



def a1():
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
def a2():
    # 主循环
    def main():
        init()
        reset_enemy()
        glutTimerFunc(30, update, 0)
        glutTimerFunc(30, move_enemy, 0)
        glutMainLoop()

    if __name__ == "__main__":
        main()
def a3():
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
def draw_colorful_cube():
    angle = 0.0  # 旋转角度

    def init():
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def draw_cube():
        vertices = [
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, -1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, -1, 1],
            [-1, 1, 1]
        ]

        colors = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1],
            [1, 0.5, 0],
            [0, 0.5, 1]
        ]

        faces = [
            [0, 1, 2, 3],
            [3, 2, 7, 6],
            [6, 7, 5, 4],
            [4, 5, 1, 0],
            [1, 5, 7, 2],
            [4, 0, 3, 6]
        ]

        glBegin(GL_QUADS)
        for face in faces:
            for i, vertex in enumerate(face):
                glColor3fv(colors[i])
                glVertex3fv(vertices[vertex])
        glEnd()

    def draw_scene():
        nonlocal angle

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluPerspective(45, 1, 0.1, 50)
        glTranslatef(0.0, 0.0, -5.0)
        glRotatef(angle, 1.0, 1.0, 1.0)

        draw_cube()

        glutSwapBuffers()

    def animate(value):
        nonlocal angle
        angle += 1.0
        glutPostRedisplay()
        glutTimerFunc(30, animate, 0)

    def run_animation():
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 800)
        glutCreateWindow("Colorful Cube Animation")

        init()

        glutDisplayFunc(draw_scene)
        glutTimerFunc(0, animate, 0)
        glutMainLoop()

    run_animation()


def play_ball_game():
    # 球的初始位置和大小
    ball_position = [0, -0.8]
    ball_radius = 0.05

    # 球的速度和方向
    ball_speed = [0.01, 0.02]

    # 板的初始位置和大小
    paddle_position = [0, -0.9]
    paddle_width = 0.4
    paddle_height = 0.05

    # 游戏界面大小
    window_width = 800
    window_height = 600

    # 渲染函数
    def render():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # 绘制球
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 0, 0)  # 设置球的颜色为红色
        glVertex2f(ball_position[0], ball_position[1])
        num_segments = 100
        for i in range(num_segments + 1):
            theta = 2.0 * math.pi * float(i) / float(num_segments)
            x = ball_radius * math.cos(theta) + ball_position[0]
            y = ball_radius * math.sin(theta) + ball_position[1]
            glVertex2f(x, y)
        glEnd()

        # 绘制板
        glBegin(GL_QUADS)
        glColor3f(0, 0, 1)  # 设置板的颜色为蓝色
        glVertex2f(paddle_position[0] - paddle_width / 2, paddle_position[1])
        glVertex2f(paddle_position[0] + paddle_width / 2, paddle_position[1])
        glVertex2f(paddle_position[0] + paddle_width / 2, paddle_position[1] + paddle_height)
        glVertex2f(paddle_position[0] - paddle_width / 2, paddle_position[1] + paddle_height)
        glEnd()

        # 刷新缓冲区
        glFlush()
        glutSwapBuffers()

    # 更新球的位置
    def update_ball_position():
        ball_position[0] += ball_speed[0]
        ball_position[1] += ball_speed[1]

        # 球与界面边缘的碰撞检测
        if ball_position[0] + ball_radius >= 1.0 or ball_position[0] - ball_radius <= -1.0:
            ball_speed[0] = -ball_speed[0]
        if ball_position[1] + ball_radius >= 1.0 or ball_position[1] - ball_radius <= -1.0:
            ball_speed[1] = -ball_speed[1]

        # 球与板的碰撞检测
        if ball_position[1] - ball_radius <= paddle_position[1] + paddle_height:
            if paddle_position[0] - paddle_width / 2 <= ball_position[0] <= paddle_position[0] + paddle_width / 2:
                ball_speed[1] = -ball_speed[1]
            else:
                # 当球与板没有碰撞时，游戏结束
                print("Game Over")
                sys.exit(0)

        # 重新绘制
        glutPostRedisplay()

    # 键盘事件处理函数
    def keyboard(key, x, y):
        if key == b'q':
            sys.exit(0)

    # 移动板的方向
    def move_paddle(direction):
        speed = 0.1
        if direction == "left" and paddle_position[0] - paddle_width / 2 > -1.0:
            paddle_position[0] -= speed
        elif direction == "right" and paddle_position[0] + paddle_width / 2 < 1.0:
            paddle_position[0] += speed

    # 特殊按键事件处理函数
    def special_keyboard(key, x, y):
        if key == GLUT_KEY_LEFT:
            move_paddle("left")
        elif key == GLUT_KEY_RIGHT:
            move_paddle("right")

    # 定时器
    def timer(value):
        update_ball_position()
        glutTimerFunc(10, timer, 0)

    def main():
        glutInit()
        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
        glutInitWindowSize(window_width, window_height)
        glutCreateWindow("2D Ball Game")
        glutDisplayFunc(render)
        glutSpecialFunc(special_keyboard)
        glutKeyboardFunc(keyboard)
        glutTimerFunc(10, timer, 0)
        glutMainLoop()

    if __name__ == "__main__":
        main()



objects = {
    0: {
        'position': (0.0, 0.9),
        'size': (0.6, 0.3),
        'color': (0.0, 0.0, 1.0),
        'default_color':  (1.0, 1.0, 0.0),
        'flash_color': (1.0, 1.0, 0.0),
        'text': 'wangwenjie',
        'program': lambda: print("欢迎"),
        'clicked': False,
    },
    1: {
        'position': (0.0, 0.6),
        'size': (0.4, 0.1),
        'color': (1.0, 0.0, 0.0),
        'default_color': (1.0, 1.0, 0.0),
        'flash_color': (0.0, 1.0, 0.0),
        'text': 'Greedy Snake',
        'program': lambda: a1(),
        'clicked': False,
    },
    2: {
        'position': (0.0, 0.4),
        'size': (0.4, 0.1),
        'color': (0.0, 1.0, 0.0),
        'default_color':  (1.0, 1.0, 0.0),
        'flash_color': (1.0, 0.0, 0.0),
        'text': 'biubiubiu~',
        'program': lambda: a2(),
        'clicked': False,
    },
    3: {
        'position': (0.0, 0.2),
        'size': (0.4, 0.1),
        'color': (0.0, 0.0, 1.0),
        'default_color':  (1.0, 1.0, 0.0),
        'flash_color': (1.0, 1.0, 0.0),
        'text': 'play ball game',
        'program': lambda: play_ball_game(),
        'clicked': False,
    },
    4: {
        'position': (0.0, 0),
        'size': (0.4, 0.1),
        'color': (0.0, 0.0, 1.0),
        'default_color':  (1.0, 1.0, 0.0),
        'flash_color': (1.0, 1.0, 0.0),
        'text': 'cube',
        'program': lambda: draw_colorful_cube(),
        'clicked': False,
    },
    5: {
        'position': (0.0, -0.2),
        'size': (0.4, 0.1),
        'color': (0.0, 0.0, 1.0),
        'default_color':  (1.0, 1.0, 0.0),
        'flash_color': (1.0, 1.0, 0.0),
        'text': ' spider web',
        'program': lambda: a3(),
        'clicked': False,
    }


}


def draw_object(obj):
    if obj['clicked']:
        glColor3f(*obj['color'])
    else:
        glColor3f(*obj['default_color'])
    glRectf(
        obj['position'][0] - obj['size'][0]/2,
        obj['position'][1] - obj['size'][1]/2,
        obj['position'][0] + obj['size'][0]/2,
        obj['position'][1] + obj['size'][1]/2
    )

    glColor3f(0.0, 0.0, 1.0)  # 设置文字颜色为白色
    glRasterPos2f(obj['position'][0] - 0.1, obj['position'][1] - 0.025)  # 设置文字位置
    for c in obj['text']:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(c))  # 使用Helvetica字体渲染文字



def display():
    glClear(GL_COLOR_BUFFER_BIT)
    for obj in objects.values():
        draw_object(obj)
    glutSwapBuffers()


def flash_button(obj_id):
    objects[obj_id]['clicked'] = True
    display()
    glutPostRedisplay()
    time.sleep(0.5)  # 延时0.5秒
    objects[obj_id]['clicked'] = False
    display()
    glutPostRedisplay()


def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        window_width = glutGet(GLUT_WINDOW_WIDTH)
        window_height = glutGet(GLUT_WINDOW_HEIGHT)
        normalized_x = (x/window_width)*2 - 1
        normalized_y = ((window_height - y)/window_height)*2 - 1
        for obj_id, obj in objects.items():
            if (
                obj['position'][0] - obj['size'][0]/2 <= normalized_x <= obj['position'][0] + obj['size'][0]/2
                and obj['position'][1] - obj['size'][1]/2 <= normalized_y <= obj['position'][1] + obj['size'][1]/2
            ):
                obj['program']()
                flash_button(obj_id)
                break


def main():
    glutInit()
    glutInitWindowSize(600, 400)
    glutCreateWindow(b"Object Click")
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMainLoop()


if __name__ == '__main__':
    main()