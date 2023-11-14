import  pygame,sys
#改变大小同时游戏事件响应

pygame.init()
size = width,height = 300,300
speed = [1,1]
BLACK = 0,0,0

screen = pygame.display.set_mode(size,pygame.RESIZABLE)#屏幕大小和类型设置
pygame.display.set_caption("pygame1")#标题
eye = pygame.image.load("1.png")#surface对象
pygame.display.set_icon(eye)
eyerect = eye.get_rect()
fps = 50
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                eyerect.left = 0
            elif event.key == pygame.K_RIGHT:
                eyerect.right = width
            elif event.key == pygame.K_UP:
                eyerect.top = 0
            elif event.key == pygame.K_DOWN:
                eyerect.bottom = height
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width,height = event.size[0],event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    if pygame.display.get_active():
        eyerect = eyerect.move(speed[0], speed[1])
    eyerect = eyerect.move(speed[0],speed[1])
    if eyerect.left < 0 or eyerect.right > width:
        speed[0] = -speed[0]
    if eyerect.top < 0 or eyerect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(BLACK)
    screen.blit(eye,eyerect)
    pygame.display.update()
    fclock.tick(fps)




