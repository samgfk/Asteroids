import pygame
import constants   
def main():
            print("Starting Asteroids!")
            print(f"Screen width: {constants.SCREEN_WIDTH}",)
            print(f"Screen height: {constants.SCREEN_HEIGHT}")
            screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
            black = "#000000"
            while True:
                screen.fill(black) 

                pygame.display.flip()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                          return 
                        

        
        

'''
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return
'''          
          
if __name__ == "__main__":
    main()