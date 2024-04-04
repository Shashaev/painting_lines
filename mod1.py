import pygame


pygame.init()

size = (500, 500)

screen = pygame.display.set_mode(size)
line = [0, 0, 0, 0]


def mouse_button_left():
    x0, y0, x1, y1 = line

    n1 = [1 / (x1 - x0), -1 / (y1 - y0)]  # | * -1
    len1 = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    len2 = (n1[0] ** 2 + n1[1] ** 2) ** 0.5
    l2 = [n1[0] * len1 / len2, n1[1] * len1 / len2]

    x2 = l2[0] + x1
    y2 = l2[1] + y1

    pygame.draw.line(screen, 'red', (x1, y1), (x2, y2))

    print('1111111111')
    print((x1, y1), (x2, y2))


def mouse_move():
    line[2], line[3] = pygame.mouse.get_pos()


def mouse_button_right():
    line[0], line[1] = pygame.mouse.get_pos()


while True:
    for even in pygame.event.get():
        if even.type == pygame.MOUSEBUTTONUP:
            if even.button == 1:
                mouse_button_left()
            elif even.button == 3:
                mouse_button_right()
        elif even.type == pygame.MOUSEMOTION:
            mouse_move()
        elif even.type == pygame.QUIT:
            pygame.quit()

    # screen.fill('white')

    pygame.draw.line(screen, 'red', line[0: 2], line[2: 4])
    pygame.display.flip()
    pygame.time.wait(10)
