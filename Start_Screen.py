import pygame

import pygame.gfxdraw
import Board_GUI as Board

screen_width, screen_height = 550, 700
pygame.init()
pygame.display.set_caption("AiDoku")
screen = pygame.display.set_mode((screen_width, screen_height))

font_size = 50
font = pygame.font.Font("JetBrainsMono-ExtraBold.ttf", font_size)
sm_font = pygame.font.Font("JetBrainsMono-ExtraBold.ttf", int(font_size / 2))
sx_font = pygame.font.Font("JetBrainsMono-ExtraBold.ttf", int(font_size / 3))

start_title = font.render("Aidoku!", True, (40, 48, 53))
start_title_rect = start_title.get_rect(center=(screen_width / 2, screen_height // 7))

# Buttons to display
# Set the location of button on the screen
play_button = font.render("Play", True, (40, 48, 53))
play_button_rect = play_button.get_rect(center=(screen_width / 2, screen_height // 2.5))


controls_text_2 = sm_font.render("('Q' and 'Esc' to Quit the game)", True, (48, 58, 65))
controls_text_2_rect = controls_text_2.get_rect(midtop=(screen_width / 2, screen_height / 1.08))

# Set the background to the buttons
play_button_bg = play_button_rect.copy()
play_button_bg.width += screen_width / 25
play_button_bg.height += screen_height / 50
play_button_bg.center = (screen_width / 2, screen_height // 2.5)


def start_screen():
    pygame.display.set_caption("AiDoku")
    mouse_pos = pygame.mouse.get_pos()

    button_color = (81, 135, 214)

    pygame.draw.rect(screen, (50, 109, 168), pygame.Rect(0, 0, screen_width, screen_height))
    screen.blit(start_title, start_title_rect)

    # Highlight the button if mouse is hovering over the button.
    if play_button_bg.collidepoint(mouse_pos):
        button_color = (124, 171, 247)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            button_color = (181, 206, 247)

    pygame.draw.rect(screen, button_color, play_button_bg)
    screen.blit(play_button, play_button_rect)
    screen.blit(controls_text_2, controls_text_2_rect)
    pygame.display.update()


screen.fill((49, 73, 125))
game = True
game_screen = "Start_Menu"
while game:
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()

        if game_screen == "Start_Menu":
            pygame.display.update()
            start_screen()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.display.update()
                pygame.quit()
                exit()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if play_button_bg.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                Board.main()
