import pygame
import os

pygame.font.init()

WIDTH, HEIGHT = 900, 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
YELLOW = (255, 215, 0)
GOLD = (255, 200, 0)
GRAY = (180, 180, 180)
DARK_GRAY = (60, 60, 60)
SELECTED_COLOR = (0, 255, 100)
BG_COLOR_TOP = (20, 40, 80)
BG_COLOR_BOTTOM = (10, 20, 40)

stadium_bg = None
_stadium_path = os.path.join("assets", "backgrounds", "stadium_bakcground.png")
try:
    raw = pygame.image.load(_stadium_path)
    stadium_bg = pygame.transform.scale(raw, (WIDTH, HEIGHT))
except Exception:
    stadium_bg = None

TITLE_FONT = pygame.font.SysFont("Arial", 64, bold=True)
BUTTON_FONT = pygame.font.SysFont("Arial", 36, bold=True)
SMALL_FONT = pygame.font.SysFont("Arial", 22, bold=True)
NAME_FONT = pygame.font.SysFont("Arial", 28, bold=True)

CHARACTERS = [
    {"name": "Messi",    "folder": "assets/characters/messi",  "image": "messi_right.png",      "flag": "🇦🇷", "country": "Argentina"},
    {"name": "Cristiano","folder": "assets/characters/cristiano",   "image": "cris_right.png",  "flag": "🇵🇹", "country": "Portugal"},
    {"name": "Neymar",   "folder": "assets/characters/neymar", "image": "neymar_right.png",     "flag": "🇧🇷", "country": "Brazil"},
    {"name": "Mbappe",   "folder": "assets/characters/mbappe",  "image": "mbappe_right.png",      "flag": "🇫🇷", "country": "France"},
    {"name": "Vinicius", "folder": "assets/characters/vini",   "image": "vini_right.png",       "flag": "🇧🇷", "country": "Brazil"},
]

for ch in CHARACTERS:
    path = os.path.join(ch["folder"], ch["image"])
    try:
        img = pygame.image.load(path)
        ch["surface"] = pygame.transform.scale(img, (120, 120))
    except Exception:
        ch["surface"] = pygame.Surface((120, 120))
        ch["surface"].fill(GRAY)

    goal_name = ch["image"].replace(".png", "_goal.png")
    goal_path = os.path.join(ch["folder"], goal_name)
    try:
        goal_img = pygame.image.load(goal_path)
        ch["goal_surface"] = pygame.transform.scale(goal_img, (120, 120))
    except Exception:
        ch["goal_surface"] = ch["surface"]


def load_trophy_frames():
    frames = []
    wc_dir = os.path.join("assets", "wc")
    TROPHY_SIZE = 240
    if os.path.isdir(wc_dir):
        for filename in sorted(os.listdir(wc_dir)):
            if filename.lower().endswith(".png"):
                path = os.path.join(wc_dir, filename)
                try:
                    img = pygame.image.load(path)
                    orig_w, orig_h = img.get_width(), img.get_height()
                    scale = TROPHY_SIZE / max(orig_w, orig_h)
                    new_w = int(orig_w * scale)
                    new_h = int(orig_h * scale)
                    img = pygame.transform.scale(img, (new_w, new_h))
                    frames.append(img)
                except Exception:
                    pass
    return frames
