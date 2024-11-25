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

# Chim
BIRD_SCALE = 0.5  # Tỷ lệ giảm kích thước
BIRD_GRAVITY = 0.4  # Trọng lực tác động lên chim
BIRD_JUMP_STRENGTH = -8  # Sức bật khi nhấn phím nhảy
BIRD_MAX_FALL_SPEED = 8  # Tốc độ rơi tối đa

# Ống
PIPE_SCALE = 0.7  # Tỷ lệ giảm kích thước
PIPE_SPEED = 4  # Tốc độ di chuyển của ống

# Khoảng cách ống
PIPE_GAP = 180   # Khoảng cách giữa ống trên và dưới
