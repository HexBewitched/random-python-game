import pygame, sprite
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('pygame has opened')

def main():
    window = pygame.display.set_mode((640,480))
    window.fill((255,255,255))
    running = True
    sprites = {}
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for sprite in sprites:
            sprite.update()
        

if __name__ == '__main__':
    main()