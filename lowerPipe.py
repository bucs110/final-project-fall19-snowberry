import pygame

class lowerPipe(pygame.sprite.Sprite):
   #constructor for bottom pipe
   def __init__(self,x,h2,windowHeight=600):
      super().__init__()
      self.windowHeight=windowHeight
      self.image=pygame.transform.scale(pygame.image.load('assets/bottomPipe.png'),(30,h2))
      self.rect=self.image.get_rect()
      self.rect.x=x
      self.rect.y=self.windowHeight-self.rect.height
      
   #updates the bottom pipe by moving it horizonatlly
   def update(self):
      self.rect.x=self.rect.x-2
