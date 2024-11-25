# constants.py
import os

# Màn hình
SCREEN_WIDTH = 1028
SCREEN_HEIGHT = 512
FPS = 60

# Đường dẫn tài nguyên
ASSET_PATH = os.path.join(os.path.dirname(__file__), "../assets")
IMAGE_PATH = os.path.join(ASSET_PATH, "images")

# File hình ảnh
BACKGROUND_IMG = os.path.join(IMAGE_PATH, "background.png")
GROUND_IMG = os.path.join(IMAGE_PATH, "lq-base.png")
PIPE_IMG = os.path.join(IMAGE_PATH, "pipe-red.png")
BIRD_IMGS = [
    os.path.join(IMAGE_PATH, "redbird-downflap.png"),
    os.path.join(IMAGE_PATH, "redbird-midflap.png"),
    os.path.join(IMAGE_PATH, "redbird-upflap.png"),
]
