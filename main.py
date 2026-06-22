import pygame
import sys
import os
from config import WIDTH, HEIGHT, BLACK, WHITE, GRAY, BUTTON_FONT, SMALL_FONT, stadium_bg
from init_phase import InitPhase
from game import GamePhase
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World Cup - Character Selection")
clock = pygame.time.Clock()

bg_music_path = os.path.join("assets", "sounds", "Pitbull.mp3")
try:
    pygame.mixer.music.load(bg_music_path)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
except Exception:
    pass

init_phase = InitPhase(screen, clock)
game_phase = GamePhase(screen, clock)

selected_players = None
state = "init"

running = True
while running:
    if state == "init":
        result = init_phase.handle_events()
        if result == "quit":
            running = False
        else:
            done = init_phase.update()
            if done == "done":
                selected_players = init_phase.get_selected_players()
                state = "playing"
            init_phase.draw()

    elif state == "playing":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                init_phase = InitPhase(screen, clock)
                selected_players = None
                state = "init"

        if stadium_bg:
            screen.blit(stadium_bg, (0, 0))

        if selected_players:
            p1, p2 = selected_players
            info = SMALL_FONT.render(
                f"{p1['flag']} {p1['name']}  VS  {p2['flag']} {p2['name']}", True, WHITE)
            screen.blit(info, info.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
