import pygame
import math
import sys
from celestial_body import Celestial_Body
pygame.init()
width,height = 1800, 964
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Planet Simulation")
class simulation:
    
    def __init__(self) -> None:
        self.bg = pygame.image.load("./images/bg.jpg")
        sun = Celestial_Body(0,0,40,(255,255,0),1.98892 * 10**30,True)
        earth = Celestial_Body(-1 * Celestial_Body.AU,0,14,(100,149,237),5.9742 * 10**24,False)    
        mars = Celestial_Body(-1.524 * Celestial_Body.AU,0,10,(188,39,50),6.39 * 10**23,False)    
        mercury = Celestial_Body(0.387 * Celestial_Body.AU,0,7,(80,79,81),3.29 * 10**23,False)    
        venus = Celestial_Body(0.732 * Celestial_Body.AU,0,12,(188,39,50),4.8685 * 10**24,False)    
        saturn = Celestial_Body(5.5 * Celestial_Body.AU, 0, 20,(188,39,50),5.6 * 10**26,False)
        saturn.has_rings = True
        self.celestial_bodies = [sun,earth,mars,mercury,venus,saturn]
        self.zoom_factor = 1
    
    def game_loop(self):    
        clock = pygame.time.Clock();
        while True:
            clock.tick(60);
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:  # Corrected line
                        self.zoom_factor += 0.1
                    elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                        self.zoom_factor -= 0.1
            window.blit(self.bg,(0,0))
            for bodies in self.celestial_bodies:
                bodies.draw(window,self.zoom_factor)
            pygame.display.flip()
        

