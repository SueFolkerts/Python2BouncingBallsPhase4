import sys
import pygame
from pygame.locals import *
from ball import *

pygame.init()
screen_info = pygame.display.Info()
# set the width and height to the size of the screen
size = (width, height) = (screen_info.current_w - 20, screen_info.current_h - 20)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (26, 255, 255)

# NEW FOLLOWS *******************************************************************
balls = []
# NEW ABOVE *******************************************************************


def main():
    # NEW FOLLOWS *******************************************
    for i in range(10):
        balls.append(Ball((width / 2, height / 2)))
    # NEW ABOVE ********************************************

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        screen.fill(color)

        # NEW FOLLOWS *****************************************
        for ball in balls:
            ball.update()

        for ball in balls:
            ball.draw(screen)
        # NEW ABOVE *******************************************

        pygame.display.flip()

if __name__ == '__main__':
    main()