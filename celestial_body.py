import pygame
class Celestial_Body:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    scale = 185/AU
    time_stamp = 3600*24
    def __init__(self,x,y,radius,color,mass,sun) -> None:
        self.x = x
        self.y = y
        self.offset_x = 0
        self.offset_y = 0
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

    def move(self,key) -> None:
        if(key == 'u'):
            self.offset_y -= 5
        elif(key == 'd'):
            self.offset_y += 5
        elif(key == 'r'):
            self.offset_x += 5
        elif(key == 'l'):
            self.offset_x -= 5 
        print(self.x)

    def draw(self,window,zoom_factor):
        height , width = window.get_height(),window.get_width() 
        x = self.x * self.scale * zoom_factor + width//2 + self.offset_x
        y = self.y * self.scale * zoom_factor  + height//2 + self.offset_y
        if(self.has_rings):
            pygame.draw.circle(window,self.color,(x,y),(self.radius + 8)  * zoom_factor)
            pygame.draw.circle(window,(0,0,0,0),(x,y),(self.radius + 5) * zoom_factor)
        
        pygame.draw.circle(window,self.color,(x,y),int(self.radius * zoom_factor))    

