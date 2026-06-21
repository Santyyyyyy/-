import pygame

##BALL


class Ball:    
    def __init__(self, ball_x,ball_y):

        self.ball_x = ball_x
        self.ball_y = ball_y
        self.gravity = 0.8
        self.radius = 40
        self.bvel_x = 0
        self.bvel_y = -8
        self.friction = 0.98
        self.bounce = 1
    ##BALL PHYSICS
    def bouncing(self):
        self.bvel_y += self.gravity
        self.ball_x += self.bvel_x
        self.ball_y += self.bvel_y
        
        if  self.ball_y + self.radius >= 500:
            self.ball_y = 500 - self.radius
            self.bvel_y = -self.bvel_y * self.bounce
            self.bvel_x *= self.friction

    def hitPlayer(self, player_rect):
        ball_rect = pygame.Rect(
            self.ball_x - self.radius,
            self.ball_y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        if ball_rect.colliderect(player_rect):
            if player_rect.centerx < self.ball_x:
                self.ball_x = player_rect.right + self.radius
                self.bvel_x = 8
            else:
                self.ball_x = player_rect.left - self.radius
                self.bvel_x = -8

            self.bvel_y = -10

    def setPosition(self,ball_x,ball_y):
        self.ball_x = ball_x
        self.ball_y = ball_y
        return (self.ball_x, self.ball_y)
    
    def getRedius(self):
        return self.radius         
