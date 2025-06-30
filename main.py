import pygame
from constants import *
import player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    new_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # 1. Get dt (You have this!)
        dt = clock.tick(60) / 1000

        # 2. Handle events (You have this for the QUIT event!)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 3. Update all game objects (Your player needs to update its state here!)
        #    (Hint: This is where new_player.update(dt) goes)
        new_player.update(dt)

        # 4. Clear the screen (Wipe away the old frame!)
        #    (Hint: This is where screen.fill(...) goes)
        screen.fill(color='black')


        # 5. Draw all game objects (Show the updated state!)
        #    (Hint: This is where new_player.draw(...) goes)
        new_player.draw(screen)

        # 6. Flip the display (You have this!)
        pygame.display.flip() 

if __name__ == "__main__":
    main()
