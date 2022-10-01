import pygame

class PhysicsObject:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = [0, 0]
    
    def move(self, physics_objects):
        self.rect.x += self.vel[0]
        for physics_object in physics_objects:
            if physics_object.rect.colliderect(self.rect):
                if self.vel[0] > 0:
                    self.rect.right = physics_object.rect.left
                else:
                    self.rect.left = physics_object.rect.right
                break
        
        self.rect.y += self.vel[1]
        for physics_object in physics_objects:
            if physics_object.rect.colliderect(self.rect):
                if self.vel[1] > 0:
                    self.rect.bottom = physics_object.rect.top
                else:
                    self.rect.top = physics_object.rect.bottom
                break
