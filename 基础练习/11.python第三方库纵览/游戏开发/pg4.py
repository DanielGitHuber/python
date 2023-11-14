import  pygame,sys
#键盘操作

pygame.init()
size = width,height = 600,600
speed = [1,1]
BLACK = 0,0,0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame写轮眼")
eye = pygame.image.load("1.png")#surface对象
eyerect = eye.get_rect()
fps = 300
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
                speed[0] = speed[0] -5 if speed[0] == 0 else (abs(speed[0]) - 5)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] +5 if speed[0] > 0 else speed[0] - 5
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] +5 if speed[1] > 0 else speed[1] - 5
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] -5 if speed[1] == 0 else (abs(speed[1]) - 5)*int(speed[1]/abs(speed[1]))
    screen.fill(BLACK)
    screen.blit(eye,eyerect)
    pygame.display.update()
    fclock.tick(fps)




