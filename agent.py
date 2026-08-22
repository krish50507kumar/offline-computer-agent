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
Create a file named test.txt inside this exact folder:

D:\\workspace\\Dev tools\\PythonProjects\\AgenticAi\\Doc

Required final state:

D:\\workspace\\Dev tools\\PythonProjects\\AgenticAi\\Doc\\test.txt

must exist.

Use the graphical interface to perform the task.
Do not use a terminal or modify Python source code.
"""
tool = Tools()
vision_model = LLM("gemma3:4b")
screenshot_dir = Path(
    r"D:\workspace\Dev tools\PythonProjects\AgenticAi\screenshots"
)
all_tools = available_tools()
instruction = instructions()
i = 1
screenshot_paths = []
while not completed:
    print("TAKING SCREENSHOT\n")
    screenshot_path = screenshot_dir / f"screenshot{i}.png"
    i += 1
    screenshot_path, scale_x, scale_y, model_w, model_h=capture_for_model(screenshot_path)
    # pyautogui.screenshot(screenshot_path)
    # model_h = 1080
    # model_w = 1920
    # scale_x = scale_y = 1
    print("SCREENSHOT TAKEN\n")
    screenshot_paths.append(screenshot_path)
    screenshot_paths = screenshot_paths[-3:]
    print("AGENT REASONING\n")
    response = vision_model.action(
        task,
        all_tools,
        screenshot_paths,
        instruction,
        model_w,
        model_h,
    )
    print("AGENT REASONED\n")
    try:
        act = parse_json_response(response)
        # act = json.loads(response)
        print("RAW RESPONSE:", repr(response))
    except json.JSONDecodeError:
        print("INVALID JSON FROM MODEL")
        print("RAW RESPONSE:", repr(response))
        continue
    tool.action(act,scale_x=scale_x, scale_y=scale_y)
    result = os.path.exists(r"D:\workspace\Dev tools\PythonProjects\AgenticAi\Doc\test.txt")
    if result:
        completed = True
    else:
        print("TASK NOT COMPLETED")

print("TASK COMPLETED")