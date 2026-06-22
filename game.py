import pygame
import player
import os
import ballphysics
class GamePhase:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.state = "game"
        self.selected_index = 0
        self.selected_player1 = None
        self.selected_player2 = None
        self.font = pygame.font.Font(None, 28)

        self.cris_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_right.png")).convert_alpha(),
            (70, 96)
        )
        self.cris_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_left.png")).convert_alpha(),
            (70, 96)
        )
        self.cris_run_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_run_right.png")).convert_alpha(),
            (70, 96)
        )
        self.cris_run_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_run_left.png")).convert_alpha(),
            (70, 96)
        )
        self.cris_goal_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "cristiano", "cris_goal.png")).convert_alpha(),
            (70, 96)
        )
        self.messi_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "messi", "messi_right.png")).convert_alpha(),
            (70, 96)
        )
        self.messi_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "messi", "messi_left.png")).convert_alpha(),
            (70, 96)
        )
        self.messi_run_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "messi", "messi_run_right.png")).convert_alpha(),
            (70, 96)
        )
        self.messi_run_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "messi", "messi_run_left.png")).convert_alpha(),
            (70, 96)
        )
        self.messi_goal_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "messi", "messi_goal.png")).convert_alpha(),
            (70, 96)
        )
        self.stadium_background = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "backgrounds", "stadium_background2.jpg")).convert(),
            (800, 600)
        )
        self.grass_layer = pygame.Surface((800, 100), pygame.SRCALPHA)
        self.grass_layer.fill((50, 255, 50, 30))
            
        self.player_pos = None

        #IN GAME

        ##STRUCTURE
        self.floor = pygame.Rect(0, 500, 800, 200)

        ##PLAYER
        self.start_x =50
        self.start_y = 200
        self.player_colour = (0,0,0)
        self.player_y = self.floor.top
        self.player_speed_y = 0
        self.jump_strength = -18
        self.player_x = 0
        self.gravity = 1

        ##CHARACTER

        self.messi = player.Player('messi',650,200,(0,0,255),self.floor.top,70,96)
        #cris = pygame.Rect(self.start_x,self.start_y, 50, 50)
        self.cris = player.Player('bicho',50,200,(255,0,0),self.floor.top,70,96)
        #neymar = pygame.Rect(start_x,start_y, 50, 50)
        self.selected_players = [self.messi, self.cris]
        self.player_selected = None
        self.rival_selected = None

        ##BALL
        self.ball_y = 400
        self.ball_x = 300
        self.my_ball = ballphysics.Ball(self.ball_x, self.ball_y)
        self.player_score = 0
        self.rival_score = 0
        self.cris_goal_timer = 0
        self.messi_goal_timer = 0
        self.cris_is_running_right = False
        self.messi_is_running_right = False
        self.cris_is_running_left = False
        self.messi_is_running_left = False
        self.selected_player_direction = "right"
        self.selected_rival_direction = "left"

    def reset_ball(ball):
        ball.ball_x = 400
        ball.ball_y = 200
        ball.bvel_x = 0
        ball.bvel_y = -8   

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT")
                return "quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.selected_players = None
                return "quit" 

    def draw(self):
        print("DRAWING GAME")
        self.draw_start_screen()

    def draw_start_screen(self):
        print("DRAWING START SCREEN")
        self.screen.blit(self.stadium_background, (0, 0))
        if self.cris_goal_timer > 0:
            current_cris_sprite = self.cris_goal_sprite
        elif self.cris_is_running_right:
            current_cris_sprite = self.cris_run_right_sprite
        elif self.cris_is_running_left:
            current_cris_sprite = self.cris_run_left_sprite
        else:
            if self.selected_player_direction == "right":
                current_cris_sprite = self.cris_right_sprite
            elif self.selected_player_direction == "left":
                current_cris_sprite = self.cris_left_sprite
        if self.messi_goal_timer > 0:
            current_messi_sprite = self.messi_goal_sprite
        elif self.messi_is_running_right:
            current_messi_sprite = self.messi_run_right_sprite
        elif self.messi_is_running_left:
            current_messi_sprite = self.messi_run_left_sprite
        else:
            if self.selected_rival_direction == "right":
                current_messi_sprite = self.messi_right_sprite
            elif self.selected_rival_direction == "left":
                current_messi_sprite = self.messi_left_sprite

        for selected_player in (self.player_selected, self.rival_selected):
            if selected_player == self.cris:
                self.screen.blit(current_cris_sprite, self.cris.rect)
            elif selected_player == self.messi:
                self.screen.blit(current_messi_sprite, self.messi.rect)

        self.screen.blit(self.grass_layer, (0, self.floor.top))
        score_text = self.font.render(f"{self.player_score} - {self.rival_score}", True, (0, 0, 0))
        self.screen.blit(score_text, (300, 20))
        pygame.draw.circle(self.screen, (255, 255, 250), (self.my_ball.ball_x, self.my_ball.ball_y), self.my_ball.getRedius())