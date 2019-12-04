import pygame

class upperPipe(pygame.sprite.Sprite):
   #constructor for top pipe
   def __init__(self,x,h1): 
      super().__init__()
      self.image=pygame.transform.scale(pygame.image.load('assets/topPipe.png'),(30,h1))
      self.rect=self.image.get_rect()
      self.rect.x=x
      self.rect.y=0
      
   #updates obstacle by moving it horizontally
   def update(self):
      self.rect.x=self.rect.x-2
