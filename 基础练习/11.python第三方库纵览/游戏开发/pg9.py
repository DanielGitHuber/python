import pygame
import sys


# 改变大小同时游戏事件响应
# mouse version
def RgbChannel(a):
    return 0 if a < 0 else (255 if a > 255 else int(a))


pygame.init()
size = width, height = 300, 300
speed = [1, 1]
BLACK = 0, 0, 0
bgc = pygame.Color("green")

screen = pygame.display.set_mode(size, pygame.RESIZABLE)  # 屏幕大小和类型设置
pygame.display.set_caption("pygame1")  # 标题
eye = pygame.image.load("1.png")  # surface对象
pygame.display.set_icon(eye)
erect = eye.get_rect()
fps = 50
f_clock = pygame.time.Clock()

still = False  #

while True:
    erect = erect.move(speed[0], speed[1])  # 初始的surface对象的运动
    for event in pygame.event.get():  # 判断事件行为
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:  # 退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 键的按下
            if event.key == pygame.K_LEFT:
                erect.left = 0
            elif event.key == pygame.K_RIGHT:
                erect.right = width
            elif event.key == pygame.K_UP:
                erect.top = 0
            elif event.key == pygame.K_DOWN:
                erect.bottom = height
        elif event.type == pygame.VIDEORESIZE:  # 屏幕的大小变动后设置使屏幕跟随
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.buttons == 1:
                erect = erect.move(event.pos[0] - erect.left, event.pos[1] - erect.top)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.buttons[0] == 1:
                erect = erect.move(event.pos[0] - erect.left, event.pos[1] - erect.top)
    if pygame.display.get_active() and not still:  # 感知窗口变动后重新设置erect的运动
        erect = erect.move(speed[0], speed[1])
    if erect.left < 0 or erect.right > width:  # 判断erect达到左右边界后速度取反
        speed[0] = -speed[0]
        if (erect.right > width) and (erect.right + speed[0] > erect.right):
            speed[0] = - speed[0]
    if erect.top < 0 or erect.bottom > height:  # 判断erect达到上下边界后速度取反
        speed[1] = -speed[1]
        if (erect.bottom > height) and (erect.bottom + speed[1] > erect.bottom):
            speed[1] = - speed[1]

    bgc.r = RgbChannel(erect.left * 255 / width)
    bgc.g = RgbChannel(erect.top * 255 / height)
    bgc.b = RgbChannel(min(speed[0], speed[1]) * 255 / max(speed[0], speed[1], 1))

    screen.fill(BLACK)  # 使运动后的区域变黑
    screen.blit(eye, erect)  # 绑定surface对象与erect
    pygame.display.update()  # 屏幕刷新成运动后的图像
    f_clock.tick(fps)
