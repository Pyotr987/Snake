import pygame


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "Retro.ttf"
background = pygame.image.load("img/asteroids.jpg").convert()


clock = pygame.time.Clock()
FPS = 30


# Main Menu
def main_menu():
    menu = True
    selected = "start"
    sel = 0
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sel -= 1

                elif event.key == pygame.K_DOWN:
                    sel += 1


                if sel%3 == 0:
                    selected = "start"
                elif sel%3 == 1:
                    selected = "settings"
                elif sel%3 == 2:
                    selected = "quit"

                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        print("Start")
                    if selected == "settings":
                        print("settings")
                    if selected == "quit":
                        pygame.quit()
                        quit()
        # Main Menu UI
        screen.blit(background, [0, 0])
        title = text_format("ASTEROIDS", font, 90, blue)
        if selected == "start":
            text_start = text_format("START", font, 75, red)
        else:
            text_start = text_format("START", font, 75, white)
        if selected == "settings":
            text_settings = text_format("SETTINGS", font, 75, red)
        else:
            text_settings = text_format("SETTINGS", font, 75, white)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, red)
        else:
            text_quit = text_format("QUIT", font, 75, white)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        settings_rect = text_settings.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 240))
        screen.blit(text_settings, (screen_width / 2 - (settings_rect[2] / 2), 300))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Asteroids")


main_menu()
pygame.quit()
quit()