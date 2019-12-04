import pygame
import random
from player import player
from lowerPipe import lowerPipe
from upperPipe import upperPipe


class controller:
   #constructor
   def __init__(self,windowWidth=600,windowHeight=600):
      pygame.init()
      pygame.mixer.init()
      pygame.display.set_caption('Jumpy Eagle')
      self.screen=pygame.display.set_mode([windowWidth,windowHeight])
      self.windowWidth=windowWidth
      self.windowHeight=windowHeight  
      self.backDropX=0
      self.x=0
      self.upperHeight=0
      self.lowerHeight=0
      self.scoreKeeper=0
      pygame.mixer.music.load("assets/Music.mp3")
      pygame.mixer.music.play()
      self.startScreenImage=pygame.image.load("assets/startScreen.png")
      self.helpScreenImage=pygame.image.load("assets/helpScreen.png")
      self.gameOverScreenImage=pygame.image.load("assets/gameOverScreen.png")
      self.state="GAME"
      self.rhighscore=0
      
   #generates the obstacles thats the eagle has to avoid in order to keep playing
   def blockgen(self):
      pipeDimensions=[[40,320],[50,310],[60,300],[70,290],[80,280],[90,270],[100,260],[110,250],[120,240],[130,230],[140,220],[150,210],[160,200],[170,190],[180,180]
             ,[190,170],[200,160],[210,150],[220,140],[230,130],[240,120],[250,110],[260,100],[270,90],[280,80],[290,70],[300,60],[310,50],[320,40]]
      pipeInterval=random.randint(600,650)
      height=random.choice(pipeDimensions)
      upperHeight=height[0]
      lowerHeight=height[1]
      self.upperpipe=upperPipe(pipeInterval,upperHeight)
      self.upperpipesprite=pygame.sprite.Group()
      self.upperpipesprite.add(self.upperpipe)
      self.all_sprites.add(self.upperpipe)
      self.lowerpipe=lowerPipe(pipeInterval,lowerHeight)
      self.lowerpipesprite=pygame.sprite.Group()
      self.lowerpipesprite.add(self.lowerpipe)
      self.all_sprites.add(self.lowerpipe)#watch cases and s's
      
   #initilizes/gets everything ready
   def new(self):
      self.player=player(self)
      self.all_sprites=pygame.sprite.Group()
      self.all_sprites.add(self.player)
      self.upperpipe=upperPipe(self.x,self.upperHeight)
      self.upperpipesprite=pygame.sprite.Group()
      self.upperpipesprite.add(self.upperpipe)
      self.lowerpipe=lowerPipe(self.x,self.lowerHeight)
      self.lowerpipesprite=pygame.sprite.Group()
      self.lowerpipesprite.add(self.lowerpipe)
      self.scoreKeeper=0 #resets score to 0 after you lose
      
   #makes it easier to give information to the player
   def msg(self,text,x,y,color,size):
      self.font=pygame.font.SysFont('garamond',size,bold=1)
      msgtxt=self.font.render(text,1,color)
      msgrect=msgtxt.get_rect()
      msgrect.center=x/2,y/2
      self.screen.blit(msgtxt,(msgrect.center))
      
   #pauses the game momentarily if the user presses enter
   def pause(self):
      wait=True
      while wait:
         for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()
               quit()
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RETURN:
                  wait=0
         self.msg("Game Has Been Paused !",self.windowWidth-400,self.windowHeight-200,(255,0,255),40)
         self.msg("(Press [ENTER] To Continue)",self.windowWidth-400,self.windowHeight-100,(255,255,255),35)
         pygame.display.flip()
         
   #ends the game if the eagle collides with a pipe
   def over(self):
      wait=True
      while wait:
         for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()
               quit()
            self.gameOverScreen()
            '''if event.type==pygame.KEYDOWN: #alternative game over screen
               if event.key==pygame.K_RETURN:
                  wait=0
         self.msg("You Lose!",self.windowWidth-200,self.windowHeight-200,(255,0,0),40)
         self.msg("Press [ENTER] To Restart",self.windowWidth-450,self.windowHeight-100,(255,0,0),40)'''
         addhsfile=open("highScore.txt","a")
         addhsfile.write(str(self.scoreKeeper)+ '\n')
         addhsfile.close()
         with open("highScore.txt") as f:
            lines=f.read().splitlines()
         highscore=max(lines)
         rhighscore=int(highscore)
         if self.scoreKeeper>rhighscore:
            rhighscore=self.scoreKeeper
         self.msg("You Tried!",self.windowWidth-150,self.windowHeight-400,(255,0,0),40)
         self.msg("Highscore: "+str(rhighscore),self.windowWidth-200,self.windowHeight,(255,255,255),50)
         f.close()
         pygame.display.flip()
      self.new()
      
   #dispplayes the players score
   def scores(self):
         self.msg("Score: "+str(self.scoreKeeper),self.windowWidth-550,self.windowHeight-550,(255,255,255),50)
         
   #updates the game "scene" by checking if there was a collision 
   def update(self):
     backDrop=pygame.image.load('assets/sky.png') 
     self.all_sprites.update()
     hitB=pygame.sprite.spritecollide(self.player,self.lowerpipesprite,False,pygame.sprite.collide_mask)
     hitT=pygame.sprite.spritecollide(self.player,self.upperpipesprite,False,pygame.sprite.collide_mask)
     if hitB or hitT:
        self.over()       
     screenResetter=self.backDropX%backDrop.get_width()
     self.screen.blit(backDrop,(screenResetter-backDrop.get_width(),0))
     if screenResetter<self.windowWidth:
        self.screen.blit(backDrop,(screenResetter,0))
     self.backDropX=self.backDropX-2
     if self.lowerpipe.rect.x<self.windowWidth/2 and self.upperpipe.rect.x<self.windowWidth/2:
        self.blockgen()
        self.scoreKeeper=self.scoreKeeper+1
        
   #puts stuff on the screen
   def draw(self):
      self.all_sprites.draw(self.screen)
      self.scores()
      
   #pauses and quits the game if neccesary     
   def event(self):
      for event in pygame.event.get():
         if event.type==pygame.QUIT:
            pygame.quit()
            quit()
         if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RETURN:
                  self.pause()
                  
   #keeps track fo what scene the game is in                   
   def run(self):
      while True:
         if self.state == "GAME":
                self.startScreen()
         elif self.state == "GAMEOVER":
                self.gameOver()

   #try and make into func
         '''self.event()
         self.update()
         self.draw()
         pygame.display.flip()'''
         
   #landing screen for when the game first starts 
   def startScreen(self):
        start="True"
        while start=="True":
            for event in pygame.event.get():
               if event.type==pygame.QUIT:
                     pygame.quit()
                     quit()
               if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE: 
                        while True:
                           pygame.display.flip()
                           self.event()
                           self.update()
                           self.draw()
                           start="False"
                           pygame.display.flip()
                    if event.key==pygame.K_h:
                        self.helpScreen()
                        start="False"
            self.screen.blit(self.startScreenImage,(0,0))
            pygame.display.flip()
            
   #provides instructions for the user
   def helpScreen(self):
        help="True"
        while help=="True":
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        self.startScreen()
                        help="False"
            self.screen.blit(self.helpScreenImage,(0,0))
            pygame.display.flip()
            
   #diplays screen for when the player loses
   def gameOverScreen(self):
        gameOver="True"
        while gameOver=="True":
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                     if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                        self.state="GAMEOVER"
            self.screen.blit(self.gameOverScreenImage,(0,0))
            pygame.display.flip()
            
