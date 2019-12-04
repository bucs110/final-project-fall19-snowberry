import pygame

class player(pygame.sprite.Sprite):
   #constructs/initilizes the bird
   def __init__(self,game,windowWidth=600,windowHeight=600):
      super().__init__()
      self.windowWidth=windowWidth
      self.windowHeight=windowHeight
      self.image=pygame.transform.scale(pygame.image.load('assets/eagle.png'),(100,90))
      self.rect=self.image.get_rect()#variable "rectangle" dosent work well with sprite
      self.rect.center=(self.windowWidth/2,self.windowHeight/2)#variable "rectangle" dosent work well with sprite
      self.position=pygame.math.Vector2(self.rect.center)
      self.acceleration=pygame.math.Vector2(0,0)
      self.velocity=pygame.math.Vector2(0,0)
      
   #controls the movement of teh bird    
   def update(self):
      self.acceleration=pygame.math.Vector2(0,2)
      self.velocity=pygame.math.Vector2(0,0)
      keyPressed=pygame.key.get_pressed()
      if keyPressed[pygame.K_SPACE]:
         self.acceleration.y=-2
      self.velocity=self.velocity+self.acceleration
      self.position=self.position+self.velocity+self.acceleration
      if self.position.y>=self.windowHeight-self.rect.width/2:
         self.position.y=self.windowHeight-self.rect.width/2
      if self.position.y<=self.rect.width/2:
         self.position.y=self.rect.width/2
      self.rect.center=self.position
