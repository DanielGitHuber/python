import  pygame,sys
#改变屏幕的显示类型

pygame.init()
vinfo = pygame.display.Info()
size = width,height = vinfo.current_w,vinfo.current_h
#size = width,height = 600,600
speed = [1,1]
BLACK = 0,0,0
#screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode(size,pygame.RESIZABLE)
screen = pygame.display.set_mode(size,pygame.NOFRAME)
#screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption("pygame1")
eye = pygame.image.load("1.png")#surface对象
eyerect = eye.get_rect()
fps = 100
fclock = pygame.time.Clock()

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
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
    screen.fill(BLACK)
    screen.blit(eye,eyerect)
    pygame.display.update()
    fclock.tick(fps)




