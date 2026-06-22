import pygame
import player
import os

class GamePhase:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.state = "game"
        self.selected_index = 0
        self.selected_player1 = None
        self.selected_player2 = None

        cris_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_right.png")).convert_alpha(),
            (70, 96)
        )
        cris_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_left.png")).convert_alpha(),
            (70, 96)
        )
        cris_run_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_run_right.png")).convert_alpha(),
            (70, 96)
        )
        cris_run_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_run_left.png")).convert_alpha(),
            (70, 96)
        )
        cris_goal_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_goal.png")).convert_alpha(),
            (70, 96)
        )
        messi_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "messi", "messi_right.png")).convert_alpha(),
            (70, 96)
        )
        messi_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "messi", "messi_left.png")).convert_alpha(),
            (70, 96)
        )
        messi_run_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "messi", "messi_run_right.png")).convert_alpha(),
            (70, 96)
        )
        messi_run_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "messi", "messi_run_left.png")).convert_alpha(),
            (70, 96)
        )
        messi_goal_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "messi", "messi_goal.png")).convert_alpha(),
            (70, 96)
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

        messi = player.Player('messi',650,200,(0,0,255),floor.top,70,96)
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