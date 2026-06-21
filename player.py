import pygame

class Player:
    def __init__(self, name, start_x, start_y, player_colour, floor_pos, width=70, height=50):
        self.name = name
        self.start_x = start_x
        self.start_y = start_y
        self.player_colour = player_colour
        self.player_y = floor_pos
        self.player_speed_y = 0
        self.jump_strength = -10
        self.player_x = 0
        self.gravity = 1
        self.rect = pygame.Rect(start_x, start_y, width, height)
        self.sprites = {}
        self.running = False
        self.goal_timer = 0

    def attach_sprites(self, sprites):
        self.sprites = sprites

    def sprite_for_state(self):
        if self.goal_timer > 0 and "goal" in self.sprites:
            return self.sprites["goal"]
        if self.running and "run" in self.sprites:
            return self.sprites["run"]
        return self.sprites.get("idle")
