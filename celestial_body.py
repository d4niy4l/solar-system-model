import pygame
class Celestial_Body:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    scale = 150/AU
    time_stamp = 3600*24
    def __init__(self,x,y,radius,color,mass,sun) -> None:
        self.x = x
        self.y = y
        self.distance_to_sun = x
        self.color = color  
        self.radius = radius
        self.mass = mass
        self.vx = 0
        self.vy = 0
        self.sun = sun
        self.distance_to_sun = 0
        self.orbit = []
        self.has_rings = False
    def draw(self,window,zoom_factor):
        height , width = window.get_height(),window.get_width() 
        x = self.x * self.scale + width/2
        x = width // 2 + int((x - width // 2) / zoom_factor) - (self.distance_to_sun * zoom_factor)
        y = self.y * self.scale + height/2
        y = height // 2 + int((y - height // 2) / zoom_factor) - (self.distance_to_sun * zoom_factor)
        if(self.has_rings):
            pygame.draw.circle(window,self.color,(x,y),self.radius+7)
            pygame.draw.circle(window,(0,0,0,0),(x,y),self.radius+5)
        
        pygame.draw.circle(window,self.color,(x,y),int(self.radius * zoom_factor))    

