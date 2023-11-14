import  pygame,sys
#增加了帧率的设置

pygame.init()
size = width,height = 600,600
speed = [1,1]
BLACK = 0,0,0

screen = pygame.display.set_mode(size)#窗口大小
pygame.display.set_caption("pygame1")#窗口标题
eye = pygame.image.load("1.png")#surface对象
eyerect = eye.get_rect()#surface对象固定
fps = 100#帧
fclock = pygame.time.Clock()#跟踪时间

while True:
    eyerect = eyerect.move(speed[0],speed[1])
    if eyerect.left < 0 or eyerect.right > width:
        speed[0] = -speed[0]
    if eyerect.top < 0 or eyerect.bottom > height:
        speed[1] = -speed[1]
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
    screen.fill(BLACK)#小球移动后填满
    screen.blit(eye,eyerect)#绑定？
    pygame.display.update()#刷新屏幕
    fclock.tick(fps)#调整每秒刷新帧数




