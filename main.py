import pygame, sys
from sys import exit

# starts pygame
mainClock = pygame.time.Clock()
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
text_font = pygame.font.Font('font/Pixelmania.ttf', 50)
soft_blue = (148, 219, 255)

speed = [2, 2]

# regular display
# to the left -> increase x
# down -> increase y
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = text_font.render('MICHIRUN', False, soft_blue)

#cat1 info
cat1_surface = pygame.image.load('graphics/cats/catGifRight.gif').convert_alpha()
cat1_x_pos = 1
cat1_y_pos = 240
cat1rect = cat1_surface.get_rect()

# put color
# test_surface.fill(soft_blue)


# to play forever
"""while True:
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
    cat1_x_pos += 2
    screen.blit(cat1_surface, (cat1_x_pos,cat1_y_pos))
    if cat1_x_pos > width + 100:
        cat1_x_pos = -200
    #el michi rebota :D
    pygame.display.flip()

    # draw all out elements
    # update everything
    # update the set_mode
    pygame.display.update()
    # not run faster than 60 frame per second
    clock.tick(60)"""

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def main_menu():
    while True:
        screen.fill((0,0,0))
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        draw_text('MICHIRUN', text_font, soft_blue,screen, 120, 40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


        pygame.display.update()
        mainClock.tick(60)

main_menu()
