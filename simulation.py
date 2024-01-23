import pygame
import sys
from celestial_body import Celestial_Body
pygame.init()
width,height = 1080, 650
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Planet Simulation")
class simulation:
    
    def __init__(self) -> None:
        #bodies
        sun = Celestial_Body(0,0,60,(255,255,0),1.98892 * 10**30,True,'SUN')
        mercury = Celestial_Body(0.389 * Celestial_Body.AU,0,8,(80,79,81),3.29 * 10**23,False,'MERCURY')    
        mercury.y_vel = -47.9 * 1000
        venus = Celestial_Body(0.732 * Celestial_Body.AU,0,14,(193,143,23),4.8685 * 10**24,False,"VENUS")    
        venus.y_vel = -35.0 * 1000
        earth = Celestial_Body(-1 * Celestial_Body.AU,0,16,(100,149,237),5.9742 * 10**24,False,"EARTH")    
        earth.y_vel = 29.8 * 1000
        mars = Celestial_Body(-1.524 * Celestial_Body.AU,0,12,(188,39,50),6.39 * 10**23,False,'MARS')    
        mars.y_vel = 24.1 * 1000
        jupiter = Celestial_Body(-4.2 * Celestial_Body.AU, 0, 29,(227,220,203),1.89 * 10**27,False,'JUPITER')
        jupiter.y_vel = 13.1 * 1000
        saturn = Celestial_Body(9.5 * Celestial_Body.AU, 0, 26,(206,184,184),5.6 * 10**26,False,'SATURN')
        saturn.y_vel = -9.7 * 1000
        uranus = Celestial_Body(-19.8 * Celestial_Body.AU, 0, 22,(198,211,227),8.61 * 10**25,False,'URANUS')
        uranus.y_vel = 6.8 * 1000
        neptune = Celestial_Body(-30 * Celestial_Body.AU, 0, 21,(91,93,223),1.024 * 10**26,False,'NEPTUNE')
        neptune.y_vel = 5.4* 1000
        pluto = Celestial_Body(39 * Celestial_Body.AU, 0, 6,(150,133,112),1.303 * 10**22,False,'BABY PLUTO')
        pluto.y_vel = 4.64 * 1000
        saturn.has_rings = True
        self.celestial_bodies = [sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune,pluto]
        #zoom
        self.zoom_factor = 1
        self.font = pygame.font.SysFont('comicsans',12)

    def move_screen(self,direction) -> None:
        for planet in self.celestial_bodies:
            planet.move(direction)

    def game_loop(self) -> None:    
        clock = pygame.time.Clock();
        while True:
            clock.tick(60);
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == 61 or event.key == pygame.K_KP_PLUS) and self.zoom_factor < 1.7: 
                        self.zoom_factor += 0.1
                    elif (event.key == 45 or event.key == pygame.K_KP_MINUS) and self.zoom_factor > 0.2:
                        self.zoom_factor -= 0.1
                        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.move_screen('l')
            if keys[pygame.K_RIGHT]:
                self.move_screen('r')
            if keys[pygame.K_UP]:
                self.move_screen('u')
            if keys[pygame.K_DOWN]:
                self.move_screen('d')
            window.fill((0,0,0))
            for bodies in self.celestial_bodies:
                bodies.update_pos(self.celestial_bodies)
                bodies.draw(window,self.zoom_factor,self.font,self.celestial_bodies[0])
            pygame.display.update()

        

