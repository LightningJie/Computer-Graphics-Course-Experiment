from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
import random

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


# 主循环
def main():
    init()
    reset_enemy()
    glutTimerFunc(30, update, 0)
    glutTimerFunc(30, move_enemy, 0)
    glutMainLoop()


if __name__ == "__main__":
    main()