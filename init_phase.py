import pygame
from config import (
    WIDTH, HEIGHT, WHITE, BLACK, YELLOW, GOLD, GRAY, DARK_GRAY,
    SELECTED_COLOR, stadium_bg,
    TITLE_FONT, BUTTON_FONT, SMALL_FONT, NAME_FONT, CHARACTERS,
    load_trophy_frames,
)

TROPHY_FRAME_DELAY = 30
COUNTDOWN_SECONDS = 1.0


class InitPhase:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.state = "start"
        self.selected_index = 0
        self.selected_player1 = None
        self.selected_player2 = None
        self.countdown_value = 3
        self.countdown_timer = 0
        self.trophy_frames = load_trophy_frames()
        self.trophy_frame_index = 0
        self.trophy_frame_timer = 0

    def draw_background(self):
        if stadium_bg:
            self.screen.blit(stadium_bg, (0, 0))
        else:
            for y in range(HEIGHT):
                t = y / HEIGHT
                r = int(20 * (1 - t) + 10 * t)
                g = int(40 * (1 - t) + 20 * t)
                b = int(80 * (1 - t) + 40 * t)
                pygame.draw.line(self.screen, (r, g, b), (0, y), (WIDTH, y))
            field_rect = pygame.Rect(0, HEIGHT - 80, WIDTH, 80)
            pygame.draw.rect(self.screen, (34, 139, 34), field_rect)
            for i in range(0, WIDTH, 60):
                pygame.draw.line(self.screen, (40, 160, 40), (i, HEIGHT - 80), (i + 20, HEIGHT), 2)

    def draw_start_screen(self):
        self.draw_background()

        title = TITLE_FONT.render("WORLD CUP 2026", True, YELLOW)
        self.screen.blit(title, title.get_rect(center=(WIDTH // 2, 140)))

        subtitle = SMALL_FONT.render("Choose your champion!", True, WHITE)
        self.screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 210)))

        if self.trophy_frames:
            img = self.trophy_frames[self.trophy_frame_index]
            self.screen.blit(img, img.get_rect(center=(WIDTH // 2, 360)))

        btn_w, btn_h = 260, 70
        btn_rect = pygame.Rect(WIDTH // 2 - btn_w // 2, 490, btn_w, btn_h)
        hover = btn_rect.collidepoint(pygame.mouse.get_pos())
        btn_color = GOLD if hover else YELLOW
        pygame.draw.rect(self.screen, btn_color, btn_rect, border_radius=15)
        pygame.draw.rect(self.screen, BLACK, btn_rect, 3, border_radius=15)

        btn_text = BUTTON_FONT.render("START GAME", True, BLACK)
        self.screen.blit(btn_text, btn_text.get_rect(center=btn_rect.center))
        return btn_rect

    def draw_selection_screen(self):
        self.draw_background()

        picking = 1 if self.selected_player1 is None else 2
        title = TITLE_FONT.render(f"PLAYER {picking} - SELECT YOUR PLAYER", True, YELLOW)
        self.screen.blit(title, title.get_rect(center=(WIDTH // 2, 60)))

        card_w, card_h = 140, 210
        total_w = len(CHARACTERS) * card_w + (len(CHARACTERS) - 1) * 20
        start_x = (WIDTH - total_w) // 2
        start_y = 140
        card_rects = []

        for i, ch in enumerate(CHARACTERS):
            x = start_x + i * (card_w + 20)
            y = start_y
            card_rect = pygame.Rect(x, y, card_w, card_h)

            border = SELECTED_COLOR if i == self.selected_index else DARK_GRAY
            border_w = 4 if i == self.selected_index else 2
            pygame.draw.rect(self.screen, border, card_rect, border_w, border_radius=12)
            inner = pygame.Rect(x + 2, y + 2, card_w - 4, card_h - 4)
            pygame.draw.rect(self.screen, (40, 40, 70), inner, border_radius=10)

            img_x = x + (card_w - 120) // 2
            img_y = y + 15
            surf = ch["goal_surface"] if i == self.selected_player1 else ch["surface"]
            self.screen.blit(surf, (img_x, img_y))

            name = NAME_FONT.render(ch["name"], True, WHITE)
            self.screen.blit(name, name.get_rect(center=(x + card_w // 2, y + 155)))

            flag_text = SMALL_FONT.render(ch["flag"], True, WHITE)
            self.screen.blit(flag_text, flag_text.get_rect(center=(x + card_w // 2, y + 182)))

            card_rects.append(card_rect)

            if i == self.selected_player1:
                label = SMALL_FONT.render("PICKED", True, SELECTED_COLOR)
                self.screen.blit(label, label.get_rect(center=(x + card_w // 2, y - 10)))

            if i == self.selected_index:
                arrow = SMALL_FONT.render("▲", True, SELECTED_COLOR)
                self.screen.blit(arrow, arrow.get_rect(center=(x + card_w // 2, y + card_h + 10)))

        sel = CHARACTERS[self.selected_index]
        info_y = 390
        info = SMALL_FONT.render(
            f"Highlighted: {sel['flag']}  {sel['name']} - {sel['country']}", True, WHITE)
        self.screen.blit(info, info.get_rect(center=(WIDTH // 2, info_y)))

        if self.selected_player1 is not None:
            p1 = CHARACTERS[self.selected_player1]
            p1_info = SMALL_FONT.render(f"Player 1: {p1['flag']} {p1['name']}", True, SELECTED_COLOR)
            self.screen.blit(p1_info, p1_info.get_rect(center=(WIDTH // 2, info_y + 30)))

        btn_w, btn_h = 220, 55
        btn_rect = pygame.Rect(WIDTH // 2 - btn_w // 2, 460, btn_w, btn_h)
        hover = btn_rect.collidepoint(pygame.mouse.get_pos())
        btn_color = GOLD if hover else YELLOW
        pygame.draw.rect(self.screen, btn_color, btn_rect, border_radius=12)
        pygame.draw.rect(self.screen, BLACK, btn_rect, 3, border_radius=12)

        btn_text = BUTTON_FONT.render("CONFIRM", True, BLACK)
        self.screen.blit(btn_text, btn_text.get_rect(center=btn_rect.center))

        hint = SMALL_FONT.render(
            "Use LEFT / RIGHT arrows to choose  |  Click card or CONFIRM to pick", True, GRAY)
        self.screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 20)))
        return btn_rect, card_rects

    def draw_countdown_screen(self):
        self.draw_background()

        p1 = CHARACTERS[self.selected_player1]
        p2 = CHARACTERS[self.selected_player2]

        versus = BUTTON_FONT.render("VS", True, WHITE)
        self.screen.blit(versus, versus.get_rect(center=(WIDTH // 2, 230)))

        card_w, card_h = 160, 160
        p1_x = WIDTH // 2 - 220
        p2_x = WIDTH // 2 + 60
        card_y = 280

        for px, player in [(p1_x, p1), (p2_x, p2)]:
            frame = pygame.Rect(px, card_y, card_w, card_h)
            pygame.draw.rect(self.screen, (40, 40, 70), frame, border_radius=12)
            pygame.draw.rect(self.screen, SELECTED_COLOR, frame, 3, border_radius=12)
            self.screen.blit(player["goal_surface"], (px + 20, card_y + 20))

            name = NAME_FONT.render(f"{player['flag']} {player['name']}", True, WHITE)
            self.screen.blit(name, name.get_rect(center=(px + card_w // 2, card_y - 20)))

            country = SMALL_FONT.render(player["country"], True, GRAY)
            self.screen.blit(country, country.get_rect(center=(px + card_w // 2, card_y + card_h + 15)))

        cd_font = pygame.font.SysFont("Arial", 80, bold=True)
        cd_text = cd_font.render(str(self.countdown_value), True, YELLOW)
        self.screen.blit(cd_text, cd_text.get_rect(center=(WIDTH // 2, 100)))

        hint = SMALL_FONT.render("Press ESC to go back", True, GRAY)
        self.screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 20)))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == "selection":
                        if self.selected_player1 is not None:
                            self.selected_player1 = None
                        else:
                            self.state = "start"
                    elif self.state == "countdown":
                        self.state = "selection"
                        self.selected_index = 0
                        self.selected_player1 = None
                        self.selected_player2 = None
                        self.countdown_value = 3
                        self.countdown_timer = 0

                if self.state == "selection":
                    if event.key == pygame.K_LEFT:
                        self.selected_index = (self.selected_index - 1) % len(CHARACTERS)
                    elif event.key == pygame.K_RIGHT:
                        self.selected_index = (self.selected_index + 1) % len(CHARACTERS)
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        return self._confirm_selection()
                elif self.state == "start":
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        self.state = "selection"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                result = self._handle_click(pygame.mouse.get_pos())
                if result is not None:
                    return result

        return None

    def _confirm_selection(self):
        if self.selected_player1 is None:
            self.selected_player1 = self.selected_index
            self.selected_index = 0
        else:
            self.selected_player2 = self.selected_index
            self.state = "countdown"
            self.countdown_value = 3
            self.countdown_timer = 0
        return None

    def _handle_click(self, pos):
        if self.state == "start":
            btn = self.draw_start_screen()
            if btn.collidepoint(pos):
                self.state = "selection"
                return None

        elif self.state == "selection":
            btn, cards = self.draw_selection_screen()
            if btn.collidepoint(pos):
                return self._confirm_selection()
            for i, rect in enumerate(cards):
                if rect.collidepoint(pos):
                    if self.selected_player1 is None:
                        self.selected_player1 = i
                        self.selected_index = 0
                    else:
                        self.selected_player2 = i
                        self.state = "countdown"
                        self.countdown_value = 3
                        self.countdown_timer = 0
                    return None
        return None

    def update(self):
        if self.state == "start":
            if self.trophy_frames:
                self.trophy_frame_timer += 1
                if self.trophy_frame_timer >= TROPHY_FRAME_DELAY:
                    self.trophy_frame_timer = 0
                    self.trophy_frame_index = (self.trophy_frame_index + 1) % len(self.trophy_frames)

        elif self.state == "countdown":
            dt = self.clock.get_time() / 1000.0
            self.countdown_timer += dt
            if self.countdown_timer >= COUNTDOWN_SECONDS:
                self.countdown_timer -= COUNTDOWN_SECONDS
                self.countdown_value -= 1
                if self.countdown_value <= 0:
                    return "done"
        return None

    def draw(self):
        if self.state == "start":
            self.draw_start_screen()
        elif self.state == "selection":
            self.draw_selection_screen()
        elif self.state == "countdown":
            self.draw_countdown_screen()

    def get_selected_players(self):
        if self.selected_player1 is not None and self.selected_player2 is not None:
            return (CHARACTERS[self.selected_player1], CHARACTERS[self.selected_player2])
        return None