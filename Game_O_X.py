import pygame
import sys

# COLORS
bgcolor = (66,135,245)
X_color = (53, 13, 77)
O_color = (121, 94, 138)
line_color = (255,0,0)
turn_color = (255,255,255)
border_color = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((800, 800))
font = pygame.font.SysFont("Lucida Console", 100)
font2 = pygame.font.SysFont("Verdana Pro", 70)

text = ("", "X", "O")
screen.fill(bgcolor)
pygame.display.update()

position = -1
center = []
flag = False
turn = 1
win = False
Draw = False
winner2 = False

memory = [[""], ["", ((125+293)/2, (125+293)/2)], ["", ((318+484)/2, (125+293)/2)], ["", ((511+677)/2, (125+293)/2)], ["", ((125+293)/2, (318+484)/2)],["", ((318+484)/2, (318+484)/2)], ["", ((511+677)/2, (318+484)/2)], ["", ((125+293)/2, (511+677)/2)], ["", ((318+484)/2, (511+677)/2)], ["", ((511+677)/2, (511+677)/2)]]


def ttt_layout():
    img = pygame.image.load("ttt_image2.png")
    image = img.get_rect()
    image.center = (400, 400)
    screen.blit(img, image)
    pygame.draw.rect(screen,border_color,image,2)

    for i in range(1, 10):
        if memory[i][0] == text[1]:
            color = X_color
        else:
            color = O_color
        img_x = font.render(memory[i][0], True, color)
        img_x_rect = img_x.get_rect()
        img_x_rect.center = memory[i][1]
        screen.blit(img_x, img_x_rect)

    pygame.display.update()


def check_win():
    global win, Draw, screen
    result = ""
    start_position = [0, 0]
    end_position = [0, 0]
    x = 0
    y = 0
    for i in range(1, 4):
        if memory[i][0] == memory[i+3][0] == memory[i+6][0] != '':
            win = True
            winner = memory[i][0]
            start_position = list(memory[i][1])
            end_position = list(memory[i+6][1])
            x = 0
            y = 50
            break

    for i in range(1, 8, 3):
        if memory[i][0] == memory[i+1][0] == memory[i+2][0] != '':
            win = True
            winner = memory[i][0]
            start_position = list(memory[i][1])
            end_position = list(memory[i+2][1])
            x = 50
            y = 0
            break
    if (memory[1][0] == memory[5][0] == memory[9][0] != ''):
        win = True
        winner = memory[5][0]
        start_position = list(memory[1][1])
        end_position = list(memory[9][1])
        x = 50
        y = 50

    if (memory[7][0] == memory[5][0] == memory[3][0] != ''):
        win = True
        winner = memory[5][0]
        start_position = list(memory[3][1])
        end_position = list(memory[7][1])
        x = -50
        y = 50
    start_position[0] -= x
    start_position[1] -= y
    end_position[0] += x
    end_position[1] += y

    count = 0
    for i in range(1, 10):
        if memory[i][0] == '':
            count += 1
    if count == 0:
        Draw = True

    if win:
        result = f"Winner is {winner}"
        colour = (240,172,0) # (43, 35, 89)
    elif Draw:
        result = f"Draw"
        colour = (43, 35, 89)
    if win or Draw:
        r_img = font2.render(result, True, colour)
        r_img_rect = r_img.get_rect()
        r_img_rect.top = 720
        r_img_rect.centerx = 400

        pygame.draw.rect(screen,bgcolor,[0,720,800,80],0)
        screen.blit(r_img, r_img_rect)
        pygame.draw.line(screen, line_color, start_position, end_position, 4)
        pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                memory = [[""], ["", ((125 + 293) / 2, (125 + 293) / 2)], ["", ((318 + 484) / 2, (125 + 293) / 2)],
                          ["", ((511 + 677) / 2, (125 + 293) / 2)], ["", ((125 + 293) / 2, (318 + 484) / 2)],
                          ["", ((318 + 484) / 2, (318 + 484) / 2)], ["", ((511 + 677) / 2, (318 + 484) / 2)],
                          ["", ((125 + 293) / 2, (511 + 677) / 2)], ["", ((318 + 484) / 2, (511 + 677) / 2)],
                          ["", ((511 + 677) / 2, (511 + 677) / 2)]]
                win = False
                Draw = False
                pygame.draw.rect(screen, bgcolor, [0, 720, 800, 80], 0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] in range(125, 293) and event.pos[1] in range(125, 293):
                    position = 1
                    pygame.draw.rect(screen, (0, 0, 0), (125, 125, 293 - 125, 293 - 125), 3)

                elif event.pos[0] in range(125, 293) and event.pos[1] in range(318, 484):
                    ttt_layout()
                    pygame.draw.rect(screen, (0, 0, 0),(125, 318, 293-125, 293-125), 3)
                    position = 4
                    center = [(125+293)/2, (318+484)/2]
                    flag = True
                elif event.pos[0] in range(125, 293) and event.pos[1] in range(511, 677):
                    ttt_layout()
                    pygame.draw.rect(screen, (0, 0, 0),(125, 511, 293-125, 293-125), 3)
                    position = 7
                    center = [(125+293)/2, (511+677)/2]
                    flag = True
                elif event.pos[0] in range(318, 484) and event.pos[1] in range(125, 293):
                    ttt_layout()
                    pygame.draw.rect(screen, (0, 0, 0),(318, 125, 293-125, 293-125), 3)
                    position = 2
                    center = [(318+484)/2, (125+293)/2]
                    flag = True
                elif event.pos[0] in range(318, 484) and event.pos[1] in range(318, 484):
                    ttt_layout()
                    pygame.draw.rect(screen, (0, 0, 0),(318, 318, 293-125, 293-125), 3)
                    position = 5
                    center = [(318+484)/2, (318+484)/2]
                    flag = True
                elif event.pos[0] in range(318, 484) and event.pos[1] in range(511, 677):
                    ttt_layout()
                    pygame.draw.rect(screen, (0, 0, 0),(318, 511, 293-125, 293-125), 3)
                    position = 8
                    center = [(318+484)/2, (511+677)/2]
                elif event.pos[0] in range(511, 677) and event.pos[1] in range(125, 293):
                    ttt_layout()
                    pygame.draw.rect(screen, (0, 0, 0),(511, 125, 293-125, 293-125), 3)
                    position = 3
                    center = [(511+677)/2, (125+293)/2]
                elif event.pos[0] in range(511, 677) and event.pos[1] in range(318, 484):
                    ttt_layout()
                    pygame.draw.rect(screen, (0, 0, 0),(511, 318, 293-125, 293-125), 3)
                    position = 6
                    center = [(511+677)/2, (318+484)/2]
                elif event.pos[0] in range(511, 677) and event.pos[1] in range(511, 677):
                    ttt_layout()
                    pygame.draw.rect(screen, (0, 0, 0),(511, 511, 293-125, 293-125), 3)
                    position = 9
                    center = [(511+677)/2, (511+677)/2]

    if position != -1:
        if len(memory[position][0]) != 1:
            memory[position][0] = text[turn]
            turn *= -1
        position = -1
    ttt_layout()
    check_win()
    turn_img = font2.render("YOUR TURN - "+text[turn], True, turn_color)
    turn_img_rect = turn_img.get_rect()
    turn_img_rect.center = (400, 50)
    pygame.draw.rect(screen, bgcolor, [0, 0, 800, 95])
    screen.blit(turn_img, turn_img_rect)

    if win or Draw:
        pygame.time.delay(2000)
        memory = [[""], ["", ((125 + 293) / 2, (125 + 293) / 2)], ["", ((318 + 484) / 2, (125 + 293) / 2)],
                  ["", ((511 + 677) / 2, (125 + 293) / 2)], ["", ((125 + 293) / 2, (318 + 484) / 2)],
                  ["", ((318 + 484) / 2, (318 + 484) / 2)], ["", ((511 + 677) / 2, (318 + 484) / 2)],
                  ["", ((125 + 293) / 2, (511 + 677) / 2)], ["", ((318 + 484) / 2, (511 + 677) / 2)],
                  ["", ((511 + 677) / 2, (511 + 677) / 2)]]
        win = False
        Draw = False
        pygame.draw.rect(screen,bgcolor,[0,720,800,80],0)

    pygame.display.update()