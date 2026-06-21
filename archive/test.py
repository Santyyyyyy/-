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

cris_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "cristiano", "cristiano.png")).convert_alpha(),
    (70, 96)
)

cris_run_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "cristiano", "cristiano_run.png")).convert_alpha(),
    (70, 96)
)
cris_goal_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "cristiano", "cristiano_goal.png")).convert_alpha(),
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
players = [messi, cris]
player_selected = None
rival_selected = None

##BALL
ball_y = 400
ball_x = 300

player_score = 0
rival_score = 0
cris_goal_timer = 0
cris_is_running = False

def reset_ball(ball):
  ball.ball_x = 400
  ball.ball_y = 200
  ball.bvel_x = 0
  ball.bvel_y = -8


running = True
state = "main_screen"
screen.fill((30, 30, 30))


my_ball=ballphysics.Ball(ball_x,ball_y)

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
              player_selected = messi
              state = "menu2"
            elif player2_rect.collidepoint(event.pos):
              player_selected = cris
              state = "menu2"

          elif state == "menu2":
            if player1_rect.collidepoint(event.pos):
              rival_selected = messi
              state = "menu2"
            elif player2_rect.collidepoint(event.pos):
              rival_selected = cris
              state = "menu2"
               
            elif player3_rect.collidepoint(event.pos):
              #player_pos = neymar
            
              

                state = "game"
         
    #PLAYER MOVILITY & PHYSICS     
    if state == "game":
      cris_is_running = False
      
      #PLAYER MOVILITY
      if keys[pygame.K_LEFT] and player_selected.rect.left > 0:
        player_selected.rect.x -= 5
        if player_selected == cris:
          cris_is_running = True
        elif player_selected == messi:
          messi_is_running = True

      if keys[pygame.K_RIGHT] and player_selected.rect.right < 800:
        player_selected.rect.x += 5
        if player_selected == cris:
          cris_is_running = True
        elif player_selected == messi:
          messi_is_running = True

      if keys[pygame.K_UP]: 
        player_selected.rect.y -= 50  

        #and player.bottom >= floor.top:
        #player_speed_y = jump_strength
        #player.y += player_speed_y

      if keys[pygame.K_a] and rival_selected.rect.left > 0:
        rival_selected.rect.x -= 5
        if rival_selected == cris:
          cris_is_running = True
        elif rival_selected == messi:
          messi_is_running = True
          
      if keys[pygame.K_d] and rival_selected.rect.right < 800:
        rival_selected.rect.x += 5
        if rival_selected == cris:
          cris_is_running = True
        elif rival_selected == messi:
          messi_is_running = True

      if keys[pygame.K_w]: 
        rival_selected.rect.y -= 50   

      # Simple player collision: stop them from overlapping.
      if player_selected.rect.colliderect(rival_selected.rect):
        if player_selected.rect.centerx < rival_selected.rect.centerx:
          player_selected.rect.right = rival_selected.rect.left
        else:
          player_selected.rect.left = rival_selected.rect.right
     
    #PHYSICS     
    ##PLAYER PHYSICS
      for selected_player in (player_selected, rival_selected):
        if selected_player.rect.bottom >= floor.top:
          selected_player.rect.bottom = floor.top
          selected_player.player_speed_y = 0

        selected_player.player_speed_y += selected_player.gravity
        selected_player.rect.y += selected_player.player_speed_y
      
      if state == "game":
            my_ball.bouncing()
            my_ball.hitPlayer(player_selected.rect)
            my_ball.hitPlayer(rival_selected.rect)


            for ball in (my_ball):
              if ball.ball_x + ball.radius < 0:
                rival_score += 1
                reset_ball(ball)
              elif ball.ball_x - ball.radius > 800:
                player_score += 1
                cris_goal_timer = 90
                reset_ball(ball)

            if cris_goal_timer > 0:
              cris_goal_timer -= 1
    
      
      
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
      
    if player_selected is None:
        menu_text = font.render("Select player one", True, (0, 0, 0))

    if state == "menu2":
      screen.fill((0, 255, 255))
      pygame.draw.rect(screen, messi.player_colour, player1_rect)
      pygame.draw.rect(screen, cris.player_colour, player2_rect)
      #pygame.draw.rect(screen, (0, 255, 0), player3_rect)
      if rival_selected is None:
        menu_text = font.render("Select player two", True, (0, 0, 0))


    
    ##IN GAME
    if state == "game":
      screen.blit(stadium_background, (0, 0))
      if cris_goal_timer > 0:
        current_cris_sprite = cris_goal_sprite
      elif cris_is_running:
        current_cris_sprite = cris_run_sprite
      else:
        current_cris_sprite = cris_sprite

      for selected_player in (player_selected, rival_selected):
        if selected_player == cris:
          screen.blit(current_cris_sprite, cris.rect)
        else:
          pygame.draw.rect(screen, selected_player.player_colour, selected_player.rect)

      screen.blit(grass_layer, (0, floor.top))
      score_text = font.render(f"{player_score} - {rival_score}", True, (0, 0, 0))
      screen.blit(score_text, (300, 20))
      pygame.draw.circle(screen, (255, 255, 250), (my_ball.ball_x, my_ball.ball_y), my_ball.getRedius())
    pygame.display.flip()
    clock.tick(60)
print("Game Over")
pygame.quit()
sys.exit()
