import pygame


pygame.init()

size = (500, 500)

screen = pygame.display.set_mode(size)

line = [0, 0, 0, 0]
per_line = [0, 0, 0, 0]


def get_per_line(x0, y0, x1, y1, a):
    x_n, y_n = 1, -1  # | * -1

    if x0 == x1 and y0 == y1:
        x_n = 0
        y_n = 0
    elif x0 == x1:
        x_n = 1
        y_n = 0
    elif y0 == y1:
        x_n = 0
        y_n = -1

    if x_n and y_n:
        x_n = 1 / (x1 - x0)
        y_n = -1 / (y1 - y0)

    if x0 > x1:
        x_n *= -1
        y_n *= -1

    if y0 > y1:
        x_n *= -1
        y_n *= -1

    len_n = (x_n ** 2 + y_n ** 2) ** 0.5

    if len_n:
        x_l2 = x_n * a / len_n
        y_l2 = y_n * a / len_n
    else:
        x_l2 = 0
        y_l2 = 0

    x2 = x_l2 + x1
    y2 = y_l2 + y1

    return [x1, y1, x2, y2]


def update_per_line():
    x0, y0, x1, y1 = line

    len1 = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

    per_line[0], per_line[1], per_line[2], per_line[3] = get_per_line(x0, y0, x1, y1, len1)


def mouse_move():
    line[2], line[3] = pygame.mouse.get_pos()


def mouse_button_right():
    line[0], line[1] = pygame.mouse.get_pos()


while True:
    for even in pygame.event.get():
        if even.type == pygame.MOUSEBUTTONUP:
            if even.button == 3:
                mouse_button_right()
                update_per_line()
        elif even.type == pygame.MOUSEMOTION:
            mouse_move()
            update_per_line()
        elif even.type == pygame.QUIT:
            pygame.quit()

    screen.fill('white')
    
    pygame.draw.line(screen, 'red', line[0: 2], line[2: 4])
    pygame.draw.line(screen, 'green', per_line[0: 2], per_line[2: 4])

    pygame.display.flip()
    pygame.time.wait(10)
