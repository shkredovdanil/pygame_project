import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    end = pygame.display.get_window_size()
    f = (end[0],0)
    s = (0,end[1])
    pygame.draw.line(screen, (255,255,255), (0,0), end, width=5)
    pygame.draw.line(screen, (255,255,255), f, s, width=5)

if __name__ == '__main__':
    pygame.init()
    try: 
        width = int(input())
        height = int(input())
        if  0 > width or 0 > height:
            raise Exception
    except Exception:
        print('Неправильный формат ввода')
        exit()
    size = width, height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Крест")
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()