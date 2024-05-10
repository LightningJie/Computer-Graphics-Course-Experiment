from OpenGL.GL import *
from OpenGL.GLUT import *
import math

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