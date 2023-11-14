import  pygame,sys
#图形导入运动

pygame.init()
size = width,height = 1200,1200
speed = [10,10]
BLACK = 0,0,0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame写轮眼")
eye = pygame.image.load("eye.png")#surface对象
eyerect = eye.get_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    eyerect = eyerect.move(speed[0],speed[1])
    if eyerect.left < 0 or eyerect.right > width:
        speed[0] = -speed[0]
    if eyerect.top < 0 or eyerect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(BLACK)
    screen.blit(eye,eyerect)
    pygame.display.update()




