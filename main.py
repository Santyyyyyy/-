import pygame
import sys

import os

import ballphysics
import player

# Player size scaling
PLAYER_SCALE = 2.5
BASE_WIDTH = 70
BASE_HEIGHT = 96
PLAYER_WIDTH = int(BASE_WIDTH * PLAYER_SCALE)
PLAYER_HEIGHT = int(BASE_HEIGHT * PLAYER_SCALE)

pygame.init()
print("Game starting...")
screen = pygame.display.set_mode((800, 600))
print("Window created")
pygame.display.set_caption("Event Handling")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

cris_right_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_right.png")).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)
cris_left_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_left.png")).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)
cris_run_right_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_run_right.png")).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)
cris_run_left_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_run_left.png")).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)
cris_goal_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_goal.png")).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)
messi_right_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "characters", "messi", "messi_right.png")).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)
messi_left_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "characters", "messi", "messi_left.png")).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)
messi_run_right_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "characters", "messi", "messi_run_right.png")).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)
messi_run_left_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "characters", "messi", "messi_run_left.png")).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)
messi_goal_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "characters", "messi", "messi_goal.png")).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)
stadium_background = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "backgrounds", "stadium_background2.jpg")).convert(),
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

messi = player.Player('messi',50,200,(0,0,255),floor.top,PLAYER_WIDTH,PLAYER_HEIGHT)
#cris = pygame.Rect(start_x,start_y, 50, 50)
cris = player.Player('bicho',650,200,(255,0,0),floor.top,PLAYER_WIDTH,PLAYER_HEIGHT)
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
messi_goal_timer = 0
cris_is_running_right = False
messi_is_running_right = False
cris_is_running_left = False
messi_is_running_left = False
selected_player_direction = "right"
selected_rival_direction = "left"

def reset_ball(ball):
  ball.ball_x = 400
  ball.ball_y = 200
  ball.bvel_x = 0
  ball.bvel_y = -8


running = True
state = "main_screen"
screen.fill((30, 30, 30))


my_ball=ballphysics.Ball(ball_x,ball_y)
game_time_left = 15.0

while running:
    #print(f"Initial delta time: {dt} seconds" if 'dt' in locals() else "Initial delta time: calculating...")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
    
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          if state == "main_screen":
            if start_rect.collidepoint(event.pos):
                player_selected = cris
                rival_selected = messi
                state = "game"
    
    # Calculate delta time for consistent timing
    dt = clock.get_time() / 1000.0
    
    #PLAYER MOVILITY & PHYSICS     
    if state == "game":
      cris_is_running_right = False
      messi_is_running_right = False
      cris_is_running_left = False
      messi_is_running_left = False
      
      #PLAYER MOVILITY
      if keys[pygame.K_LEFT] and player_selected.rect.left > 0:
        player_selected.rect.x -= 5
        if player_selected == cris:
          cris_is_running_left = True
        elif player_selected == messi:
          messi_is_running_left = True
        selected_player_direction = "left"
        
      if keys[pygame.K_RIGHT] and player_selected.rect.right < 800:
        player_selected.rect.x += 5
        if player_selected == cris:
          cris_is_running_right = True
        elif player_selected == messi:
          messi_is_running_right = True
        selected_player_direction = "right"
      
      if keys[pygame.K_UP]: 
        player_selected.rect.y -= 50  
      
      if keys[pygame.K_a] and rival_selected.rect.left > 0:
        rival_selected.rect.x -= 5
        if rival_selected == cris:
          cris_is_running_left = True
        elif rival_selected == messi:
          messi_is_running_left = True
        selected_rival_direction = "left"
        
      if keys[pygame.K_d] and rival_selected.rect.right < 800:
        rival_selected.rect.x += 5
        if rival_selected == cris:
          cris_is_running_right = True
        elif rival_selected == messi:
          messi_is_running_right = True
        selected_rival_direction = "right"
      
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
            #santy_ball.bouncing()
            my_ball.hitPlayer(player_selected.rect)
            my_ball.hitPlayer(rival_selected.rect)
            #santy_ball.hitPlayer(player_selected.rect)
            #santy_ball.hitPlayer(rival_selected.rect)
      
      
            #for ball in (my_ball, santy_ball):
            if my_ball.ball_x + my_ball.radius > 800:
              rival_score += 1
              if rival_selected == cris:
                cris_goal_timer = 90
              elif rival_selected == messi:
                messi_goal_timer = 90
              reset_ball(my_ball)
            elif my_ball.ball_x - my_ball.radius < 0:
              player_score += 1
              if player_selected == cris:
                cris_goal_timer = 90
              elif player_selected == messi:
                messi_goal_timer = 90
              reset_ball(my_ball)
      
            if cris_goal_timer > 0:
              cris_goal_timer -= 1
            if messi_goal_timer > 0:
              messi_goal_timer -= 1
            
            # Update game timer
            game_time_left = max(0.0, game_time_left - dt)

    #GAME STATE
    ##MAIN SCREEN
    if state == "main_screen":
        instruction_text = font.render("Player one move with WASD, Player two move with arrow keys", True, (255, 255, 255))
        screen.blit(instruction_text, instruction_text.get_rect(center=(400, 150)))
        pygame.draw.rect(screen, (255, 230, 0), start_rect)
        text = font.render("Start", True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=start_rect.center))
        
    if game_time_left <= 0:
        state = "game_over"
    ##IN GAME
    if state == "game":
      screen.blit(stadium_background, (0, 0))
      if cris_goal_timer > 0:
        current_cris_sprite = cris_goal_sprite
      elif cris_is_running_right:
        current_cris_sprite = cris_run_right_sprite
      elif cris_is_running_left:
        current_cris_sprite = cris_run_left_sprite
      else:
        if selected_player_direction == "right":
          current_cris_sprite = cris_right_sprite
        elif selected_player_direction == "left":
          current_cris_sprite = cris_left_sprite
      if messi_goal_timer > 0:
        current_messi_sprite = messi_goal_sprite
      elif messi_is_running_right:
        current_messi_sprite = messi_run_right_sprite
      elif messi_is_running_left:
        current_messi_sprite = messi_run_left_sprite
      else:
        if selected_rival_direction == "right":
          current_messi_sprite = messi_right_sprite
        elif selected_rival_direction == "left":
          current_messi_sprite = messi_left_sprite
    
      for selected_player in (player_selected, rival_selected):
        if selected_player == cris:
          screen.blit(current_cris_sprite, cris.rect)
        elif selected_player == messi:
          screen.blit(current_messi_sprite, messi.rect)
    
      #dt = min(dt, 0.05)
      #print(f"Delta time: {dt:.4f} seconds")
    
      screen.blit(grass_layer, (0, floor.top))
      score_text = font.render(f"{rival_score} - {player_score}", True, (0, 0, 0))
      screen.blit(score_text, (300, 20))
      timer_text = font.render(f"Time: {int(game_time_left)}", True, (0, 0, 0))
      screen.blit(timer_text, (10, 10))
      pygame.draw.circle(screen, (255, 255, 250), (my_ball.ball_x, my_ball.ball_y), my_ball.getRedius())
      #pygame.draw.circle(screen, (123, 123, 123), (santy_ball.ball_x,santy_ball.ball_y), santy_ball.getRedius())
    if state == "game_over":
        screen.fill((0, 0, 0))
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        final_score_text = font.render(f"Final Score: {rival_score} - {player_score}", True, (255, 255, 255))
        screen.blit(game_over_text, game_over_text.get_rect(center=(400, 250)))
        screen.blit(final_score_text, final_score_text.get_rect(center=(400, 300)))
    
    pygame.display.flip()
    clock.tick(60)
print("Game Over")
pygame.quit()
sys.exit()