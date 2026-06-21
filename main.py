import pygame
import sys

import os


pygame.init()
print("Game starting...")
screen = pygame.display.set_mode((800, 600))
print("Window created")
pygame.display.set_caption("Event Handling")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)
    
player = None
#MENU & START SCREEN
start_rect = pygame.Rect(300, 250, 200, 60)
player1_rect = pygame.Rect(150,350, 90, 90)
player2_rect = pygame.Rect(240,350, 90, 90)
player3_rect = pygame.Rect(330,350, 90, 90)

#IN GAME

##STRUCTURE
floor = pygame.Rect(0, 500, 800, 200)

##PLAYER
start_x =50
start_y = 200
player_colour = (0,0,0)
player_y = floor.top
player_speed_y = 0
jump_strength = -18
player_x = 0
gravity = 1

##CHARACTER
messi = pygame.Rect(start_x,start_y, 50, 50)
cris = pygame.Rect(start_x,start_y, 70, 50)
neymar = pygame.Rect(start_x,start_y, 50, 50)

##BALL
ball_y = 400
ball_x = 300
radius = 40
bvel_x = 0
bvel_y = -8
bounce = 1
friction = 0.98



running = True
state = "menu"
screen.fill((30, 30, 30))
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          if state == "main_screen":
            if start_rect.collidepoint(event.pos):
                state = "menu"
                
          elif state == "menu":
            if player1_rect.collidepoint(event.pos):
              player = messi
              player_colour = (0, 0, 255)
              state = "game"
              
            elif player2_rect.collidepoint(event.pos):
              player = cris
              player_colour = (255, 0, 0)
              state = "game"
              
            elif player3_rect.collidepoint(event.pos):
              player = neymar
              player_colour = (0, 255, 0)
              state = "game"
         
    #PLAYER MOVILITY & PHYSICS     
    if state == "game":
      
      #PLAYER MOVILITY
      if keys[pygame.K_a] or keys[pygame.K_LEFT] and not player.left <= 0:
        player.x -= 5
          
      if keys[pygame.K_d] or keys[pygame.K_RIGHT] and not player.right >= 800:
        player.x += 5
        
      if keys[pygame.K_SPACE] or keys[pygame.K_UP] and player.bottom >= floor.top:
        player_speed_y = jump_strength
        player.y += player_speed_y
    #PHYSICS     
    ##PLAYER PHYSICS
      if player.bottom >= floor.top:
        player.bottom = floor.top
        player_speed_y = 0
          
      player_speed_y += gravity
      player.y += player_speed_y
      
    ##BALL PHYSICS
    bvel_y += gravity
    ball_x += bvel_x
    ball_y += bvel_y
    
    if ball_y + radius >= 500:
      ball_y = 500 - radius
      bvel_y = -bvel_y * bounce
      bvel_x *= friction
    
    
    
      
      
  #GAME STATE
  ##MAIN SCREEN
    if state == "main_screen":
        pygame.draw.rect(screen, (255, 230, 0), start_rect)
        text = font.render("Start", True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=start_rect.center))
    
    ##MENU
    if state == "menu":
      screen.fill((0, 255, 255))
      pygame.draw.rect(screen, (0, 0, 255), player1_rect)
      pygame.draw.rect(screen, (255, 0, 0), player2_rect)
      pygame.draw.rect(screen, (0, 255, 0), player3_rect)
    
    ##IN GAME
    if state == "game":
      screen.fill((0,255,255))
      pygame.draw.rect(screen, player_colour, player)
      pygame.draw.rect(screen, (50, 255, 50), floor)
      pygame.draw.circle(screen, (255, 255, 250), (ball_x, ball_y), radius)
    pygame.display.flip()
    clock.tick(60)
print("Game Over")
pygame.quit()
sys.exit()