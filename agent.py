import json
from llm import LLM
from tools import Tools
from pathlib import Path
import pyautogui
import os
from config import available_tools,instructions,parse_json_response
from computer import capture_for_model
Path("screenshots").mkdir(exist_ok=True)
completed = False
task = """
Open Chrome.
Use the graphical interface to perform the task.
Do not use a terminal or modify Python source code.
"""
tool = Tools()
models = {
    1:"qwen3-vl:2b",# take too much time in responding
    2:"qwen2.5vl:3b",# not much vram to run
    3:"gemma3:4b", # fast in responding but bad at locating
    4:"qwen3-vl:4b",
}
model = models[3]
vision_model = LLM(model)
screenshot_dir = Path(
    r"D:\workspace\Dev tools\PythonProjects\AgenticAi\screenshots"
)
all_tools = available_tools()
instruction = instructions()
i = 1
screenshot_paths = []
while not completed:
    # print("TAKING SCREENSHOT\n")
    screenshot_path = screenshot_dir / f"screenshot{i}.png"
    # i += 1
    screenshot_path, scale_x, scale_y, model_w, model_h=capture_for_model(screenshot_path)
    # pyautogui.screenshot(screenshot_path)
    # model_h = 1080
    # model_w = 1920
    # scale_x = scale_y = 1
    # print("SCREENSHOT TAKEN\n")
    # screenshot_paths.append(screenshot_path)
    # screenshot_paths = screenshot_paths[-3:]
    screenshot_paths = [screenshot_path]
    # print("AGENT REASONING\n")
    response = vision_model.action(
        task,
        all_tools,
        screenshot_paths,
        instruction,
        model_w,
        model_h,
    )
    # print("AGENT REASONED\n")
    try:
        act = parse_json_response(response)
        # act = json.loads(response)
        print("RAW RESPONSE:", repr(response))
    except json.JSONDecodeError:
        print("INVALID JSON FROM MODEL")
        print("RAW RESPONSE:", repr(response))
        continue
    tool_name = act["tool"]
    params = act.get("params", {})
    if "x" in act["params"]:
        x = act["params"]["x"]
        y = act["params"]["y"]

        if not (0 <= x < model_w and 0 <= y < model_h):
            print(f"INVALID MODEL COORDINATES: ({x}, {y})")
            continue
    if tool_name == "task_complete":
        print("MODEL CLAIMED TASK COMPLETE")
        break
    tool.action(act,scale_x=scale_x, scale_y=scale_y)

print("TASK COMPLETED")