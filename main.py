# import time
# import json
# from llm import LLM
# from tools import Tools
# from pathlib import Path
# import os
# from config import available_tools,instructions
# from computer import capture_for_model
# tool = Tools()
# all_tools = available_tools()
# instruction = instructions()
# screenshot_paths = []
# task = """
# Create a file named test.txt inside this exact folder:
#
# D:\\workspace\\Dev tools\\PythonProjects\\AgenticAi\\Doc
#
# Required final state:
#
# D:\\workspace\\Dev tools\\PythonProjects\\AgenticAi\\Doc\\test.txt
#
# must exist.
#
# Use the graphical interface to perform the task.
# Do not use a terminal or modify Python source code.
# """
# i =1
# vision_model = LLM("qwen3-vl:2b")
# screenshot_dir = Path(
#     r"D:\workspace\Dev tools\PythonProjects\AgenticAi\screenshots"
# )
# print("TAKING SCREENSHOT\n")
# screenshot_path = screenshot_dir / f"screenshot{i}.png"
# i += 1
# screenshot_path, scale_x, scale_y, model_w, model_h=capture_for_model(screenshot_path)
# print("SCREENSHOT TAKEN\n")
# screenshot_paths.append(screenshot_path)
# screenshot_paths = screenshot_paths[-3:]
# t0 = time.time()
# response = vision_model.action(task, all_tools, screenshot_paths, instruction, model_w=model_w, model_h=model_h)
# print(f"LLM call took {time.time() - t0:.1f}s")

from pathlib import Path

print("Current directory:", Path.cwd())

Path("screenshots").mkdir(exist_ok=True)

print("Created:", Path("screenshots").resolve())
print("Exists:", Path("screenshots").exists())