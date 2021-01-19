import pygame 
from plane_sprites import *

class PlaneGame():
    """Game Class"""

    def __init__(self):
        print("Game Initialization")
        pygame.init()
        # 1. set up the game window
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. create a game clock
        self.clock = pygame.time.Clock()
        # 3. initialize sprites and sprite groups by calling the private method
        self.__create_sprites()
        # 4. set timer event - create enemies
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):
        # create background sprite and corresponding group
        bg1 = Background()
        bg2 = Background(True)
        self.background_group = pygame.sprite.Group(bg1,bg2)

        # create enemy sprite group
        self.enemy_group = pygame.sprite.Group()

        # create hero sprite and corresponding group
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("Game Starts")
        while True:
            # 1. set the frame rate
            self.clock.tick(FRAME_RATE)
            # 2. listen to the events
            self.__event_handler()
            # 3. check for collision
            self.__check_collision()
            # 4. update and draw the sprite group
            self.__update_sprites()
            # 5. update/show the screen
            pygame.display.update()
            pass
    
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("Moving right")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 1.5
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -1.5
        else:
            self.hero.speed = 0
                

    def __check_collision(self):
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        collided_enemy_list = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if collided_enemy_list:
            self.hero.kill()
            PlaneGame.__game_over()


    def __update_sprites(self):

        for group in [self.background_group,self.enemy_group,self.hero_group,self.hero.bullets]:
            group.update()
            group.draw(self.screen)


    @staticmethod
    def __game_over():
        print("Game Over")
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
