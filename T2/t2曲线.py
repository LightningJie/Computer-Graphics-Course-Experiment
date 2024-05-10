from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
# control_points =np.array()
control_points1 = np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0]])#直线
control_points2 = np.array([[0.0, 0.0], [1.0, 1.0], [2.0, -1.0], [3.0, 0.0]])#平滑弯曲
control_points3 = np.array([[0.0, 0.0], [1.0, 1.5], [2.0, 0.5], [3.0, 2.0], [4.0, 1.0], [5.0, 1.5], [6.0, 0.0]])#尖锐弯曲
a=int(input('请输入测试用例编号'))
print(type(a))
if a==1:
    print(11)
    control_points=control_points1
elif a==2:
    print(22)
    control_points=control_points2
elif a==3:
    print(33)
    control_points = control_points3
print(control_points)
def draw_bezier_curve(control_points):
    glPointSize(5.0)
    glColor3f(1.0, 0.0, 0.0)  # 设置点的颜色为红色
    glBegin(GL_POINTS)
    for point in control_points:
        glVertex2f(point[0], point[1])  # 绘制控制点
    glEnd()

    glColor3f(0.0, 1.0, 0.0)  # 设置曲线的颜色为绿色
    glBegin(GL_LINE_STRIP)
    steps = 1000  # 绘制曲线点的数量
    for i in range(steps + 1):
        t = i / float(steps)
        point = bezier_curve_point(control_points, t)
        glVertex2f(point[0], point[1])  # 绘制曲线点
    glEnd()


def bezier_curve_point(control_points, t):
    n = len(control_points) - 1
    point = np.zeros(2)
    for i in range(n + 1):
        point += binomial_coefficient(n, i) * (1 - t) ** (n - i) * t ** i * control_points[i]
    return point


def binomial_coefficient(n, k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_bezier_curve(control_points)

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1600, 800)
    glutCreateWindow(b"Bezier Curve")
    glutDisplayFunc(draw)
    glutMainLoop()


if __name__ == "__main__":
    main()