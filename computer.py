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