import json

from _testcapi import testBuf

from llm import LLM
from tools import Tools
import pyautogui
from pathlib import Path
import os
from config import available_tools,instructions

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
vision_model = LLM("qwen3-vl:2b")
screenshot_dir = Path(
    r"D:\workspace\Dev tools\PythonProjects\AgenticAi\screenshots"
)
all_tools = available_tools()
instruction = instructions()
i = 1
screenshot_paths = []

while not completed:

    screenshot_path = screenshot_dir / f"screenshot{i}.png"

    pyautogui.screenshot(screenshot_path)

    screenshot_paths.append(screenshot_path)
    screenshot_paths = screenshot_paths[-3:]
    response = vision_model.action(
        task,
        all_tools,
        screenshot_paths,
        instruction
    )
    try:
        act = json.loads(response)
        print("RAW RESPONSE:", repr(response))
    except json.JSONDecodeError:
        print("INVALID JSON FROM MODEL")
        print("RAW RESPONSE:", repr(response))
        continue
    tool.action(act)
    result = os.path.exists(r"D:\workspace\Dev tools\PythonProjects\AgenticAi\Doc\test.txt")
    if result:
        completed = True
    else:
        print("TASK NOT COMPLETED")
    i+=1
print("TASK COMPLETED")