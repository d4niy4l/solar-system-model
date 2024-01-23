import pygame
import math
class Celestial_Body:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    scale = 200/AU
    time_stamp = 3600*24
    def __init__(self,x,y,radius,color,mass,sun,name) -> None:
        self.x = x
        self.y = y
        self.offset_x = 0
        self.offset_y = 0
        self.distance_to_sun = 0
        self.color = color  
        self.radius = radius
        self.mass = mass
        self.sun = sun
        self.distance_to_sun = 0
        self.orbit = []
        self.has_rings = False
        self.x_vel = 0
        self.y_vel = 0
        self.name = name

    def move(self,key) -> None:
        if(key == 'u'):
            self.offset_y += 5
        elif(key == 'd'):
            self.offset_y -= 5
        elif(key == 'r'):
            self.offset_x -= 5
        elif(key == 'l'):
            self.offset_x += 5
        

    def attraction(self,other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y **2)
        if other.sun:
            self.distance_to_sun = distance
        force = ( self.G * self.mass * other.mass) / distance**2
        angle = math.atan2(distance_y,distance_x)
        force_x = math.cos(angle) * force
        force_y = math.sin(angle) * force
        return force_x,force_y

    def update_pos(self,planets) -> None:
        total_fx = total_fy = 0
        for planet in planets:  
            if self == planet:  
                continue
            fx,fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        
        self.x_vel += total_fx/self.mass * self.time_stamp
        self.y_vel += total_fy/self.mass * self.time_stamp
        self.x += self.x_vel * self.time_stamp
        self.y += self.y_vel  * self.time_stamp
        self.orbit.append((self.x,self.y))
    
    def draw(self,window,zoom_factor,font : pygame.font,sun) -> None:
        height , width = window.get_height(),window.get_width() 
        x = self.x * self.scale * zoom_factor + width//2 + self.offset_x*zoom_factor
        y = self.y * self.scale * zoom_factor  + height//2 + self.offset_y*zoom_factor
        if(self.has_rings):
            pygame.draw.circle(window,self.color,(x,y),(self.radius + 8)  * zoom_factor)
            pygame.draw.circle(window,(0,0,0,0),(x,y),(self.radius + 5) * zoom_factor)

        if len(self.orbit) > 2:    
            updated_points = []
            for point in self.orbit:
                x,y = point
                x = x * self.scale * zoom_factor + width/2  + self.offset_x*zoom_factor
                y = y * self.scale * zoom_factor + height/2 + self.offset_y*zoom_factor
                updated_points.append((x,y))
            pygame.draw.lines(window,self.color,False,updated_points)
        sun_x = sun.x * sun.scale * zoom_factor + width//2 + sun.offset_x*zoom_factor
        sun_y = sun.y * sun.scale * zoom_factor  + height//2 + sun.offset_y*zoom_factor
        pygame.draw.line(window, self.color, (sun_x,sun_y), (x,y), 2)  # 2 is the line thickness
        pygame.draw.circle(window,self.color,(x,y),int(self.radius * zoom_factor))    
        name = font.render(f"{self.name}",1,(0,0,0) if self.sun else (255, 255, 255))
        window.blit(name,(x - name.get_width(),y - name.get_height()) if not self.sun else (x,y))

