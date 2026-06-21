import pygame
import sys

import os

import ballphysics
import player

pygame.init()
print("Game starting...")
screen = pygame.display.set_mode((800, 600))
print("Window created")
pygame.display.set_caption("Event Handling")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)
    
player_pos = None
selected_player = None
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

messi = player.Player('messi',650,200,(0,0,255),floor.top)
cris = player.Player('bicho',50,200,(255,0,0),floor.top)
#neymar = pygame.Rect(start_x,start_y, 50, 50)

##BALL
ball_y = 400
ball_x = 300


running = True
state = "menu1"
screen.fill((30, 30, 30))


my_ball=ballphysics.Ball(ball_x,ball_y)
santy_ball=ballphysics.Ball(600,0)

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
                state = "menu1"
                
          elif state == "menu1":
            if player1_rect.collidepoint(event.pos):
              selected_player = messi
              state = "menu2"
              
            elif player2_rect.collidepoint(event.pos):
              selected_player = cris
              state = "menu2"
          
            elif state == "menu2":
                if player1_rect.collidepoint(event.pos):
                    rival_player = messi
                    state = "game"
                
                elif player2_rect.collidepoint(event.pos):
                    rival_player = cris
                    state = "game"
              

         
    #PLAYER MOVILITY & PHYSICS     
    if state == "game":
      
      #PLAYER MOVILITY
      if keys[pygame.K_LEFT] and selected_player.rect.left > 0:
        selected_player.rect.x -= 5
          
      if keys[pygame.K_RIGHT] and selected_player.rect.right < 800:
        selected_player.rect.x += 5

      if keys[pygame.K_a] and rival_player.rect.left > 0:
        rival_player.rect.x -= 5
          
      if keys[pygame.K_d] and rival_player.rect.right < 800:
        rival_player.rect.x += 5
    
    #PHYSICS     
    ##PLAYER PHYSICS
      if selected_player.rect.bottom >= floor.top:
        selected_player.rect.bottom = floor.top
        selected_player.player_speed_y = 0

      selected_player.player_speed_y += selected_player.gravity
      selected_player.rect.y += selected_player.player_speed_y

      if rival_player.rect.bottom >= floor.top:
        rival_player.rect.bottom = floor.top
        rival_player.player_speed_y = 0

      rival_player.player_speed_y += cris.gravity
      rival_player.rect.y += cris.player_speed_y
      
    ##BALL PHYSICS
    
    my_ball.bouncing()
    santy_ball.bouncing()
    
      
      
  #GAME STATE
  ##MAIN SCREEN
    if state == "main_screen":
        pygame.draw.rect(screen, (255, 230, 0), start_rect)
        text = font.render("Start", True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=start_rect.center))
    
    ##MENU
    if state == "menu1":
      screen.fill((0, 255, 255))
      pygame.draw.rect(screen, messi.player_colour, player1_rect)
      pygame.draw.rect(screen, cris.player_colour, player2_rect)
    if state == "menu2":
      screen.fill((0, 255, 255))
      pygame.draw.rect(screen, messi.player_colour, player1_rect)
      pygame.draw.rect(screen, cris.player_colour, player2_rect)
      #pygame.draw.rect(screen, (0, 255, 0), player3_rect)
    
    ##IN GAME
    if state == "game":
      screen.fill((0,255,255))
      pygame.draw.rect(screen, messi.player_colour, messi.rect)
      pygame.draw.rect(screen, cris.player_colour, cris.rect)
      pygame.draw.rect(screen, (50, 255, 50), floor)
      pygame.draw.circle(screen, (255, 255, 250), (my_ball.ball_x, my_ball.ball_y), my_ball.getRedius())
      pygame.draw.circle(screen, (123, 123, 123), (santy_ball.ball_x,santy_ball.ball_y), santy_ball.getRedius())
    pygame.display.flip()
    clock.tick(60)
print("Game Over")
pygame.quit()
sys.exit()
