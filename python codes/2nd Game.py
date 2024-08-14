import pygame
import random
import os
pygame.font.init()
pygame.init()
i=0
mouse_pos= pygame.mouse.get_pos()
screen= pygame.display.set_mode((1080,720))
pygame.display.set_caption(':Game:')

#Rectangles:
background= pygame.image.load(os.path.join('python codes', 'files', 'background.webp'))
background_new = pygame.transform.scale(background,(1080,720))
dialog= pygame.image.load(os.path.join('python codes', 'files', 'dialog.png'))
dialog_N= pygame.transform.scale(dialog,(1000,500))


CLOCK = pygame.time.Clock()
surface=pygame.Surface((1080,720))

   
while True:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
       pygame.quit()
       exit()
    
  


   

  
  
   



  pygame.time.get_ticks()
  screen.blit(surface,(0,0))
  screen.blit(background_new,(0,0))
  screen.blit(dialog_N,(20,400))
  CLOCK.tick(60)
  surface.fill((255,255,255))
  CLOCK.tick(0)
  pygame.display.update()

