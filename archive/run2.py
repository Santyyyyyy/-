import pygame
import sys

import os

import ballphysics
import player
#run v.2
pygame.init()
print("Game starting...")
screen = pygame.display.set_mode((800, 600))
print("Window created")
pygame.display.set_caption("Event Handling")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

cris_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets","cristiano", "cristiano.png")).convert_alpha(),
    (70, 96)
)
cris_run_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets","cristiano", "cristiano_run.png")).convert_alpha(),
    (70, 96)
)
cris_goal_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets","cristiano", "cristiano_goal.png")).convert_alpha(),
    (70, 96)
)
messi_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "messi", "messi.png")).convert_alpha(),
    (50, 96)
)
messi_run_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "messi", "messi_run.png")).convert_alpha(),
    (50, 96)
)
messi_goal_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "messi", "messi_goal.png")).convert_alpha(),
    (50, 96)
)
stadium_background = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "stadium_background2.jpg")).convert(),
    (800, 600)
)
grass_layer = pygame.Surface((800, 100), pygame.SRCALPHA)
grass_layer.fill((50, 255, 50, 30))
    
player_pos = None
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
#cris = pygame.Rect(start_x,start_y, 50, 50)
cris = player.Player('bicho',50,200,(255,0,0),floor.top,70,96)
#neymar = pygame.Rect(start_x,start_y, 50, 50)

##BALL
ball_y = 400
ball_x = 300

cris_score = 0
messi_score = 0
cris_goal_timer = 0
cris_is_running = False
messi_is_running = False
messi_goal_timer = 0
def reset_ball(ball):
  ball.ball_x = 400
  ball.ball_y = 200
  ball.bvel_x = 0
  ball.bvel_y = -8


running = True
state = "menu"
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
                state = "menu"
                
          elif state == "menu":
            if player1_rect.collidepoint(event.pos):
              state = "game"
              
            elif player2_rect.collidepoint(event.pos):
              state = "game"
              
            elif player3_rect.collidepoint(event.pos):
              #player_pos = neymar
              pass
         
    #PLAYER MOVILITY & PHYSICS     
    if state == "game":
      cris_is_running = False
      messi_is_running = False

      #PLAYER MOVILITY
      if keys[pygame.K_LEFT] and messi.rect.left > 0:
        messi.rect.x -= 5
        messi_is_running = True
          
      if keys[pygame.K_RIGHT] and messi.rect.right < 800:
        messi.rect.x += 5
        messi_is_running = True

      if keys[pygame.K_UP]: 
        messi.rect.y -= 50  

        #and player.bottom >= floor.top:
        #player_speed_y = jump_strength
        #player.y += player_speed_y

      if keys[pygame.K_a] and cris.rect.left > 0:
        cris.rect.x -= 5
        cris_is_running = True
          
      if keys[pygame.K_d] and cris.rect.right < 800:
        cris.rect.x += 5
        cris_is_running = True

      if keys[pygame.K_w]: 
        cris.rect.y -= 50   

      # Simple player collision: stop them from overlapping.
      if messi.rect.colliderect(cris.rect):
        if messi.rect.centerx < cris.rect.centerx:
          messi.rect.right = cris.rect.left
        else:
          messi.rect.left = cris.rect.right
    
    #PHYSICS     
    ##PLAYER PHYSICS
      if messi.rect.bottom >= floor.top:
        messi.rect.bottom = floor.top
        messi.player_speed_y = 0

      messi.player_speed_y += messi.gravity
      messi.rect.y += messi.player_speed_y

      if cris.rect.bottom >= floor.top:
        cris.rect.bottom = floor.top
        cris.player_speed_y = 0

      cris.player_speed_y += cris.gravity
      cris.rect.y += cris.player_speed_y
      
    ##BALL PHYSICS
    
    my_ball.bouncing()
    santy_ball.bouncing()

    my_ball.hitPlayer(messi.rect)
    my_ball.hitPlayer(cris.rect)
    santy_ball.hitPlayer(messi.rect)
    santy_ball.hitPlayer(cris.rect)

    for ball in (my_ball, santy_ball):
      if ball.ball_x + ball.radius < 0:
        messi_score += 1
        messi_goal_timer = 90
        reset_ball(ball)
      elif ball.ball_x - ball.radius > 800:
        cris_score += 1
        cris_goal_timer = 90
        reset_ball(ball)

    if cris_goal_timer > 0:
      cris_goal_timer -= 1
    if messi_goal_timer > 0:
      messi_goal_timer -= 1
    
      
      
  #GAME STATE
  ##MAIN SCREEN
    if state == "main_screen":
        pygame.draw.rect(screen, (255, 230, 0), start_rect)
        text = font.render("Start", True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=start_rect.center))
    
    ##MENU
    if state == "menu":
      screen.fill((0, 255, 255))
      pygame.draw.rect(screen, messi.player_colour, player1_rect)
      pygame.draw.rect(screen, cris.player_colour, player2_rect)
      #pygame.draw.rect(screen, (0, 255, 0), player3_rect)
    
    ##IN GAME
    if state == "game":
      
      screen.blit(stadium_background, (0, 0))
      if cris_goal_timer > 0:
        current_cris_sprite = cris_goal_sprite
      elif cris_is_running:
        current_cris_sprite = cris_run_sprite
      else:
        current_cris_sprite = cris_sprite
      if messi_goal_timer > 0:
        current_messi_sprite = messi_goal_sprite
      elif messi_is_running:
        current_messi_sprite = messi_run_sprite
      else:
        current_messi_sprite = messi_sprite

      screen.blit(current_cris_sprite, cris.rect)
      screen.blit(current_messi_sprite, messi.rect)
      #add channel alpha to grass layer
      pygame.draw.rect(screen, (50, 255, 50), floor)
      score_text = font.render(f"Cris {cris_score} - Messi {messi_score}", True, (0, 0, 0))
      screen.blit(score_text, (300, 20))
      pygame.draw.circle(screen, (255, 255, 250), (my_ball.ball_x, my_ball.ball_y), my_ball.getRedius())
      pygame.draw.circle(screen, (123, 123, 123), (santy_ball.ball_x,santy_ball.ball_y), santy_ball.getRedius())
    pygame.display.flip()
    clock.tick(60)
print("Game Over")
pygame.quit()
sys.exit()
