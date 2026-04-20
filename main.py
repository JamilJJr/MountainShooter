import pygame

print('Setup Start')
pygame.init()

print('Janela')
window = pygame.display.set_mode(size=(600, 480))

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit() # Close Window
            quit() # Encerra a inicialização do PyGame
