import random
import pygame
import requests

screen_width, screen_height = 550, 700
font_size = 50
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
buffer = 5
global grid, grid_original, ran_diff

def import_grid():
    difficulty = {1: "https://sugoku.herokuapp.com/board?difficulty=easy",
                  2: "https://sugoku.herokuapp.com/board?difficulty=easy",
                  3: "https://sugoku.herokuapp.com/board?difficulty=easy"}
    global ran_diff
    ran_diff = random.randint(1, 3)
    response_easy = requests.get(difficulty[ran_diff])
    global grid
    grid = response_easy.json()['board']
    global grid_original

    length = len(grid[0])
    grid_original = [[grid[row][col] for col in range(length)] for row in range(length)]


def insert(win, position):
    try:
        i, j = position[1] - 1, position[0] - 1
        sm_font = pygame.font.Font("JetBrainsMono-ExtraBold.ttf", int(font_size / 1.47))
        sx_font = pygame.font.Font("JetBrainsMono-ExtraBold.ttf", int(font_size / 3))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if grid_original[i][j] != 0:
                        return
                    num_entered = event.key - 48
                    if num_entered == 0:
                        grid[i][j] = num_entered
                        pygame.draw.rect(win, background_color, (
                            (j + 1) * 50 + .5 * buffer, (i + 1) * 50 + .5 * buffer, 50 - 1.2 * buffer,
                            50 - 1.2 * buffer))
                        pygame.display.update()
                        return

                    if 0 < num_entered < 10:
                        if isValid((i, j), num_entered, win):
                            pygame.draw.rect(win, background_color, (
                                (j + 1) * 50 + .8 * buffer, (i + 1) * 50 + .8 * buffer, 50 - 1.4 * buffer,
                                50 - 1.4 * buffer))
                            value = sm_font.render(str(num_entered), True, (49, 73, 125))
                            win.blit(value, (position[0] * 50 + 15, position[1] * 50))
                            grid[i][j] = event.key - 48

                            pygame.draw.rect(win, (49, 73, 125), (
                                0, 5, 550, 24))
                            pygame.display.update()
                            return

                        else:
                            pygame.draw.rect(win, (49, 73, 125), (
                                0, 5, 550, 24))

                            if not valid_row((i, j), event.key - 48, win):
                                error_grid = sx_font.render(
                                    "Invalid Input, " + str(event.key - 48) + " already in Row!",
                                    True, (40, 48, 53))

                            elif not valid_col((i, j), event.key - 48, win):
                                error_grid = sx_font.render(
                                    "Invalid Input, " + str(event.key - 48) + " already in Column!",
                                    True, (40, 48, 53))

                            elif not valid_grid((i, j), event.key - 48, win):
                                error_grid = sx_font.render(
                                    "Invalid Input, " + str(event.key - 48) + " already in Grid!",
                                    True, (40, 48, 53))

                            else:
                                error_grid = sx_font.render(
                                    "Invalid Input, " + str(event.key - 48) + " already in Grid/Row/Col!",
                                    True, (40, 48, 53))

                            error_grid_rect = error_grid.get_rect(center=(screen_width / 2, 20))
                            win.blit(error_grid, error_grid_rect)
                            pygame.display.update()
                    return

                if event.type == pygame.QUIT:
                    return
    except:
        print("Put values in Table")


def isEmpty(num):
    if num == 0:
        return True
    return False

def isValid(row_col, num, win):
    row = row_col[0]
    col = row_col[1]

    # Checking row
    for i in range(0, len(grid[0])):
        if grid[row][i] == num:
            print(num, "Already in same Row at (", row, " ,", i, ") = ", grid[row][i])

            return False

    # Checking column
    for i in range(0, len(grid[0])):
        if grid[i][col] == num:
            print(num, "Already in same column at (", i, " ,", col, ")= ", grid[i][col])

            return False

    # Check sub-grid
    x = row_col[0] // 3 * 3
    y = row_col[1] // 3 * 3
    # Gives us the box number

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x + i][y + j] == num:
                print(num, "Already in same grid at (", x + i, " ,", y + j, ")")

                return False
    return True


def valid_row(row_col, num, win):
    row = row_col[0]
    col = row_col[1]

    # Checking row
    for i in range(0, len(grid[0])):
        if grid[row][i] == num:
            print(num, "Already in same Row at (", row, " ,", i, ") = ", grid[row][i])

            return False

    return True


def valid_col(row_col, num, win):
    row = row_col[0]
    col = row_col[1]

    # Checking column
    for i in range(0, len(grid[0])):
        if grid[i][col] == num:
            print(num, "Already in same column at (", i, " ,", col, ")= ", grid[i][col])

            return False

    return True


def valid_grid(row_col, num, win):
    # Check sub-grid
    row = row_col[0] // 3 * 3
    col = row_col[1] // 3 * 3

    # Gives us the box number
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[row + i][col + j] == num:
                print(num, "Already in same grid at (", row + i, " ,", col + j, ")")

                return False

    return True


solved = 0


def sudoku_solver(win):
    sm_font = pygame.font.Font("JetBrainsMono-ExtraBold.ttf", int(font_size / 1.47))
    length = len(grid[0])
    for i in range(0, length):
        for j in range(0, length):
            if isEmpty(grid[i][j]):
                for k in range(1, 10):
                    if isValid((i, j), k, win):
                        grid[i][j] = k

                        pygame.draw.rect(win, background_color, (
                            (j + 1) * 50 + .8 * buffer, (i + 1) * 50 + .8 * buffer, 50 - 1.4 * buffer,
                            50 - 1.4 * buffer))
                        value = sm_font.render(str(k), True, (49, 73, 125))
                        win.blit(value, (50*(j+1)+buffer*3, 50*(i+1)))
                        pygame.display.update()

                        if ran_diff == 1:
                            pygame.time.delay(2)

                        elif ran_diff == 2:
                            pygame.time.delay(1)

                        else:
                            pygame.time.delay(0)

                        sudoku_solver(win)

                        # Exit condition
                        global solved
                        if solved == 1:
                            return

                        # if sudoku_solver returns, there's a mismatch
                        grid[i][j] = 0
                        pygame.draw.rect(win, background_color, (
                            (j + 1) * 50 + .8 * buffer, (i + 1) * 50 + .8 * buffer, 50 - 1.4 * buffer,
                            50 - 1.4 * buffer))
                        pygame.display.update()

                return
    solved = 1


def reset_puzzle(win):
    # grid = [[grid_original[x][y] for y in range(len(grid_original[0]))] for x in range(len(grid_original))]

    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            grid[i][j] = grid_original[i][j]

    global solved
    solved = 0
    display_grid(win)


def display_grid(win):
    font = pygame.font.Font("JetBrainsMono-ExtraBold.ttf", int(font_size / 1.47))

    for i in range(0, len(grid[0])):
        print(grid[i])
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):

                value = font.render(str(grid[i][j]), True, (49, 73, 125))
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))

            else:
                pygame.draw.rect(win, background_color, (
                    (j + 1) * 50 + .8 * buffer, (i + 1) * 50 + .8 * buffer, 50 - 1.4 * buffer, 50 - 1.4 * buffer))
                pygame.display.update()
        print("\n")
    pygame.display.update()


def main():
    import_grid()
    pygame.init()
    font = pygame.font.Font("JetBrainsMono-ExtraBold.ttf", int(font_size / 1.47))
    sm_font = pygame.font.Font("JetBrainsMono-ExtraBold.ttf", int(font_size / 4))

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("AiDoku")
    screen.fill((50, 109, 167))

    solve_button = font.render("Solve", True, (40, 48, 53))
    reset_button = font.render("Reset", True, (40, 48, 53))
    rules_text = sm_font.render("(Rule: repetition of numbers (1-9) in row, col or grid is not allowed)", True,
                                (48, 58, 65))
    rules_text_todo = sm_font.render("('Q' to Quit, Space to generate new board)", True,
                                     (48, 58, 65))

    # Set the location of button on the screen

    solve_button_rect = solve_button.get_rect(center=(screen_width / 1.5, screen_height // 1.2))
    reset_button_rect = reset_button.get_rect(center=(screen_width / 2.5, screen_height // 1.2))
    rules_text_rect = rules_text.get_rect(midtop=(screen_width / 2, screen_height / 1.08))
    rules_text_todo_rect = rules_text_todo.get_rect(midtop=(screen_width / 2, screen_height / 1.1))

    solve_button_bg = solve_button_rect.copy()
    solve_button_bg.width += screen_width / 25
    solve_button_bg.height += screen_height / 50
    solve_button_bg.center = (screen_width / 1.5, screen_height // 1.2)

    reset_button_bg = reset_button_rect.copy()
    reset_button_bg.width += screen_width / 25
    reset_button_bg.height += screen_height / 50
    reset_button_bg.center = (screen_width / 2.5, screen_height // 1.2)

    screen.blit(rules_text, rules_text_rect)
    screen.blit(rules_text_todo, rules_text_todo_rect)

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    display_grid(screen)

    while True:
        button_color = (81, 135, 214)
        option_button_color = (81, 135, 214)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos[1] // 50, pos[0] // 50 )

                if (0 < pos[0] // 50 < 10) and (0 < pos[1] // 50 < 10):
                    insert(screen, (pos[0] // 50, pos[1] // 50))

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                    # return "Start Menu"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        main()

        mouse_pos = pygame.mouse.get_pos()
        if solve_button_bg.collidepoint(mouse_pos):
            button_color = (124, 171, 247)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                button_color = (181, 206, 247)
                reset_puzzle(screen)
                sudoku_solver(screen)
        if reset_button_bg.collidepoint(mouse_pos):
            option_button_color = (124, 171, 247)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                reset_puzzle(screen)

        pygame.draw.rect(screen, button_color, solve_button_bg)
        screen.blit(solve_button, solve_button_rect)

        pygame.draw.rect(screen, option_button_color, reset_button_bg)
        screen.blit(reset_button, reset_button_rect)
        pygame.display.update()

# main()
