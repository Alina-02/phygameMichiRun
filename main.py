import pygame
from sys import exit

# starts pygame
pygame.init()
# the window to play
width = 800
height = 400
# display surface
screen = pygame.display.set_mode((width, height))
# change title
pygame.display.set_caption('MichiRun')
# control the framerate
clock = pygame.time.Clock()
# create a font
test_font = pygame.font.Font('font/Pixelmania.ttf', 30)
soft_blue = (148, 219, 255)

speed = [2, 2]

# regular display
# to the left -> increase x
# down -> increase y
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('MICHIRUN', False, soft_blue)

cat1_surface = pygame.image.load('graphics/cats/catGif.gif')

cat1rect = cat1_surface.get_rect()

# put color
# test_surface.fill(soft_blue)


# to play forever
while True:
    # event loop, looking all the posibilities of plating inputs
    for event in pygame.event.get():
        # indicate to close the window
        if event.type == pygame.QUIT:
            # opposite to init()
            pygame.quit()
            # close any code (close the while)
            exit()

    cat1rect = cat1rect.move(speed)
    if cat1rect.left < 0 or cat1rect.right > width:
        speed[0] = -speed[0]
    if cat1rect.top < 0 or cat1rect.bottom > height:
        speed[1] = -speed[1]

    # display the surface
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (40, 30))
    screen.blit(cat1_surface, cat1rect)
    #el michi rebota :D
    pygame.display.flip()

    # draw all out elements
    # update everything
    # update the set_mode
    pygame.display.update()
    # not run faster than 60 frame per second
    clock.tick(60)
