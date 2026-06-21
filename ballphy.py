import pygame


class Ball:

    def __init__(self, ball_x, ball_y):

        self.ball_x = ball_x
        self.ball_y = ball_y

        self.radius = 40

        self.bvel_x = 0
        self.bvel_y = -300

        self.gravity = 900
        self.bounce = 0.7
        self.air_drag = 0.995
        self.ground_friction = 0.92


    def update(self, dt):

        self.bvel_y += self.gravity * dt

        self.ball_x += self.bvel_x * dt
        self.ball_y += self.bvel_y * dt

        self.bvel_x *= self.air_drag

        self.checkGround()


    def checkGround(self):

        if self.ball_y + self.radius >= 500:

            self.ball_y = 500 - self.radius

            self.bvel_y = -self.bvel_y * self.bounce

            self.bvel_x *= self.ground_friction


    def hitPlayer(self, player_rect):

        ball_rect = pygame.Rect(
            self.ball_x - self.radius,
            self.ball_y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        if ball_rect.colliderect(player_rect):

            hit_position = self.ball_x - player_rect.centerx

            self.bvel_x = hit_position * 8
            self.bvel_y = -600


    def setPosition(self, x, y):

        self.ball_x = x
        self.ball_y = y


    def getRadius(self):

        return self.radius