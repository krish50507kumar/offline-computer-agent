from PIL import Image, ImageDraw
import pyautogui as gui

MODEL_IMG_WIDTH = 1280

def draw_cursor(img, x, y, color="lime"):
    draw = ImageDraw.Draw(img)
    size = 14
    draw.line([(x, y), (x + size, y + size // 2)], fill=color, width=3)
    draw.line([(x, y), (x + size // 2, y + size)], fill=color, width=3)
    draw.ellipse([(x - 4, y - 4), (x + 4, y + 4)], outline=color, width=2)
    return img

def capture_for_model(save_path):
    screenshot = gui.screenshot()
    real_w, real_h = screenshot.size
    cursor_x, cursor_y = gui.position()
    screenshot = draw_cursor(screenshot, cursor_x, cursor_y)
    scale = MODEL_IMG_WIDTH / real_w
    model_w = MODEL_IMG_WIDTH
    model_h = round(real_h * scale)
    resized = screenshot.resize((model_w, model_h), Image.LANCZOS)
    resized.save(save_path)
    scale_x = real_w / model_w
    scale_y = real_h / model_h
    pad_top = 0
    return save_path, scale_x, scale_y, model_w, model_h, pad_top

def draw_debug_marker(model_image_path, x, y, save_path="screenshots/debug_marker.png", label=""):

    img = Image.open(model_image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    r = 10
    draw.line([(x - r, y), (x + r, y)], fill="red", width=2)
    draw.line([(x, y - r), (x, y + r)], fill="red", width=2)
    draw.ellipse([(x - r, y - r), (x + r, y + r)], outline="red", width=2)
    if label:
        draw.text((x + r + 4, y - r), label, fill="red")
    img.save(save_path)
    return save_path