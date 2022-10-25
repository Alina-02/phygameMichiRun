import pygame
import sys

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
font = pygame.font.SysFont("Arial",20)
soft_blue = (148, 219, 255)

speed = [2, 2]

# regular display
# to the left -> increase x
# down -> increase y
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = text_font.render('MICHIRUN', False, soft_blue)
profile_background = pygame.image.load('graphics/profile_background.jpg').convert()

#cat1 info
cat1_surface = pygame.image.load('graphics/cats/catGifRight.gif').convert_alpha()
cat1_x_pos = 1
cat1_y_pos = 240
cat1rect = cat1_surface.get_rect()

# put color
# test_surface.fill(soft_blue)

click = False

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

#menú principal
def main_menu():
    global click
    while True:
        screen.fill((0,0,0))
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        draw_text('MICHIRUN', text_font, soft_blue,screen, 120, 40)

        mx, my = pygame.mouse.get_pos()

        button_start_carrera = pygame.Rect(330, 150, 150, 50)
        buttom_top = pygame.Rect(330, 210, 150, 50)
        buttom_profile = pygame. Rect(330, 270, 150, 50)
        if button_start_carrera.collidepoint((mx, my)):
            if click:
                game()
        if buttom_top.collidepoint((mx, my)):
            if click:
                top()
        if buttom_profile.collidepoint((mx, my)):
            if click:
                profile()
        pygame.draw.rect(screen, soft_blue, button_start_carrera)
        pygame.draw.rect(screen, soft_blue, buttom_top)
        pygame.draw.rect(screen, soft_blue, buttom_profile)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
#menú de start
def game():
    running = True
    while running:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

#top de jugadores
def top():
    running = True
    while running:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

#perfil del jugador
def profile():
    #hacer un botón para volver a la pantalla principal
    running = True

    while running:

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        mx, my = pygame.mouse.get_pos()
        buttom_back = pygame.Rect(330, 150, 150, 50)
        if buttom_back.collidepoint(mx, my):
            if click:
                main_menu()
        pygame.draw.rect(screen, soft_blue, buttom_back)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


main_menu()

#diseñar botones decentes
"""class Button:
    Create a button, then blit the surface in the while loop

    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "uwu"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        Change the text when you click
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(button_start_carrera.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")

button_start_carrera = Button("Start", (330, 150), font=30, bg="navy", feedback="uwu")
"""

