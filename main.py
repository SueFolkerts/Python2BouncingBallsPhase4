from ball import *
balls = []

def main():
    for i in range(10):
        balls.append(Ball((width / 2, height / 2)))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        screen.fill(color)

        for ball in balls:
            ball.update()

        for ball in balls:
            ball.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()