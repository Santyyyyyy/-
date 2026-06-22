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
        self.neymar_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "neymar", "neymar_right.png")).convert_alpha(),
            (70, 96)
        )
        self.neymar_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "neymar", "neymar_left.png")).convert_alpha(),
            (70, 96)
        )
        self.neymar_run_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "neymar", "neymar_run_right.png")).convert_alpha(),
            (70, 96)
        )
        self.neymar_run_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "neymar", "neymar_run_left.png")).convert_alpha(),
            (70, 96)
        )
        self.neymar_goal_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "neymar", "neymar_goal.png")).convert_alpha(),
            (70, 96)
        )
        self.mbappe_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "mbappe", "mbappe_right.png")).convert_alpha(),
            (70, 96)
        )
        self.mbappe_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "mbappe", "mbappe_left.png")).convert_alpha(),
            (70, 96)
        )
        self.mbappe_run_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "mbappe", "mbappe_run_right.png")).convert_alpha(),
            (70, 96)
        )
        self.mbappe_run_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "mbappe", "mbappe_run_left.png")).convert_alpha(),
            (70, 96)
        )
        self.mbappe_goal_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "mbappe", "mbappe_goal.png")).convert_alpha(),
            (70, 96)
        )
        self.vini_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "vini", "vini_right.png")).convert_alpha(),
            (70, 96)
        )
        self.vini_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "vini", "vini_left.png")).convert_alpha(),
            (70, 96)
        )
        self.vini_run_right_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "vini", "vini_run_right.png")).convert_alpha(),
            (70, 96)
        )
        self.vini_run_left_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "vini", "vini_run_left.png")).convert_alpha(),
            (70, 96)
        )
        self.vini_goal_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "characters", "vini", "vini_goal.png")).convert_alpha(),
            (70, 96)
        )
        self.stadium_background = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "backgrounds", "stadium_background2.jpg")).convert(),
            (800, 600)
        )
        
        self.sprite_sets = {
            "Cristiano": {
                "right": self.cris_right_sprite, "left": self.cris_left_sprite,
                "run_right": self.cris_run_right_sprite, "run_left": self.cris_run_left_sprite,
                "goal": self.cris_goal_sprite,
            },
            "Messi": {
                "right": self.messi_right_sprite, "left": self.messi_left_sprite,
                "run_right": self.messi_run_right_sprite, "run_left": self.messi_run_left_sprite,
                "goal": self.messi_goal_sprite,
            },
            "Neymar": {
                "right": self.neymar_right_sprite, "left": self.neymar_left_sprite,
                "run_right": self.neymar_run_right_sprite, "run_left": self.neymar_run_left_sprite,
                "goal": self.neymar_goal_sprite,
            },
            "Mbappe": {
                "right": self.mbappe_right_sprite, "left": self.mbappe_left_sprite,
                "run_right": self.mbappe_run_right_sprite, "run_left": self.mbappe_run_left_sprite,
                "goal": self.mbappe_goal_sprite,
            },
            "Vinicius": {
                "right": self.vini_right_sprite, "left": self.vini_left_sprite,
                "run_right": self.vini_run_right_sprite, "run_left": self.vini_run_left_sprite,
                "goal": self.vini_goal_sprite,
            },
        }
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

        self.player1 = player.Player('p1',650,200,(0,0,255),self.floor.top,70,96)
        self.player2 = player.Player('p2',50,200,(255,0,0),self.floor.top,70,96)
        self.selected_players = [self.player1, self.player2]
        self.characters = ["Cristiano", "Messi", "Neymar", "Mbappe", "Vinicius"]

        # sprite set for each player (defaults until the menu calls set_players)
        self.player1_set = self.sprite_sets[self.selected_players[0]]  # Default to the first character
        self.player2_set = self.sprite_sets[self.selected_players[1]]  # Default to the second character

        ##BALL
        self.ball_y = 400
        self.ball_x = 300
        self.my_ball = ballphysics.Ball(self.ball_x, self.ball_y)
        self.player1_score = 0
        self.player2_score = 0
        self.player1_timer = 0
        self.player2_timer = 0
        self.player1_is_running_right = False
        self.player2_is_running_right = False
        self.player1_is_running_left = False
        self.player2_is_running_left = False
        self.player1_direction = "right"
        self.player2_direction = "left"

    def set_players(self, selected_players):
        if not selected_players:
            return
        p1, p2 = selected_players    # CHARACTERS dicts from the menu
        self.player1.name = p1["name"]
        self.player2.name = p2["name"] 
        self.player1_set = self.sprite_sets.get(p1["name"])
        self.player2_set = self.sprite_sets.get(p2["name"])

    def get_sprite(self, sprite_set, direction, is_running, timer):
        if timer > 0:
            return sprite_set["goal"]
        if is_running:
            return sprite_set["run_" + direction]
        return sprite_set[direction]

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
        p1_img = self.get_sprite(self.player1_set, self.player1_direction,
                         self.player1_is_running_right or self.player1_is_running_left,
                         self.player1_timer)
        self.screen.blit(p1_img, self.player1.rect)

        p2_img = self.get_sprite(self.player2_set, self.player2_direction,
                         self.player2_is_running_right or self.player2_is_running_left,
                         self.player2_timer)
        self.screen.blit(p2_img, self.player2.rect)
        

    def draw_start_screen(self):
        print("DRAWING START SCREEN")
        self.screen.blit(self.stadium_background, (0, 0))
        self.screen.blit(self.grass_layer, (0, self.floor.top))
        score_text = self.font.render(f"{self.player1_score} - {self.player2_score}", True, (0, 0, 0))
        self.screen.blit(score_text, (300, 20))
        pygame.draw.circle(self.screen, (255, 255, 250), (self.my_ball.ball_x, self.my_ball.ball_y), self.my_ball.getRedius())