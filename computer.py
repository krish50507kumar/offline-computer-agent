from PIL import Image
import pyautogui as gui

MODEL_IMG_WIDTH = 1280


def capture_for_model(save_path):
    screenshot = gui.screenshot()
    real_w, real_h = screenshot.size

    scale = MODEL_IMG_WIDTH / real_w
    model_w = MODEL_IMG_WIDTH
    model_h = round(real_h * scale)

    resized = screenshot.resize((model_w, model_h), Image.LANCZOS)
    resized.save(save_path)

    scale_x = real_w / model_w
    scale_y = real_h / model_h

    return save_path, scale_x, scale_y, model_w, model_h

from PIL import Image, ImageDraw

# def draw_debug_marker(model_image_path, x, y, save_path="screenshots/debug_marker.png", label=""):
#
#     img = Image.open(model_image_path).convert("RGB")
#     draw = ImageDraw.Draw(img)
#
#     r = 10
#     # Crosshair
#     draw.line([(x - r, y), (x + r, y)], fill="red", width=2)
#     draw.line([(x, y - r), (x, y + r)], fill="red", width=2)
#     # Circle outline
#     draw.ellipse([(x - r, y - r), (x + r, y + r)], outline="red", width=2)
#
#     if label:
#         draw.text((x + r + 4, y - r), label, fill="red")
#
#     img.save(save_path)
#     return save_path