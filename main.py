
from constants import *
from player import Player 
from asteroid import Asteroid  
from AsteroidField import *
from shot import Shot
def main():
            pygame.init()   
            Clock = pygame.time.Clock()
            
            updateable = pygame.sprite.Group()
            drawable = pygame.sprite.Group()
            asteroids = pygame.sprite.Group()
            shots = pygame.sprite.Group()



            Shot.containers = (shots,updateable,drawable)
            AsteroidField.containers = (updateable,)
            Player.containers = (updateable, drawable)
            Asteroid.containers = (asteroids, updateable, drawable)
            

            dt = 0
            ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            field = AsteroidField()
            
            

            print("Starting Asteroids!")
            print(f"Screen width: {SCREEN_WIDTH}",)
            print(f"Screen height: {SCREEN_HEIGHT}")
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            black = "#000000"

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                
                dt = Clock.tick(60)/1000  # dt is set each frame
                screen.fill(black)

                updateable.update(dt)
                
                

                      
                for asteroid in asteroids:
                      if asteroid.collision(ship):
                            print("Game over!")
                            exit()
                
                for asteroid in asteroids:
                   for bullet in shots:
                        if asteroid.collision(bullet):
                             asteroid.split()
                             bullet.kill() 
                            
                for obj in drawable:
                    obj.draw(screen)
                
                
               
                
                pygame.display.flip()
                


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                          return
                
                
            
                

                        

        
        
if __name__ == "__main__":
    main()