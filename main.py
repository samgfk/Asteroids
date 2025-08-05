import pygame
import constants
import player   
def main():
            pygame.init()   
            Clock = pygame.time.Clock()
            dt = 0
            ship = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
            
           
            print("Starting Asteroids!")
            print(f"Screen width: {constants.SCREEN_WIDTH}",)
            print(f"Screen height: {constants.SCREEN_HEIGHT}")
            screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
            black = "#000000"
            while True:
                dt = Clock.tick(60)/1000  # dt is set each frame
                screen.fill(black)

                ship.__draw__(screen)

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