import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.getLogger("httpx").setLevel(logging.WARNING)

from computer_agent import ComputerAgent
# model which I have pulled through ollama
models = {
    1:"qwen3-vl:2b",
    2:"qwen2.5vl:3b",
    3:"gemma3:4b",
    4:"qwen3-vl:4b",
    5: "moondream",
    6:"qwen3.5:4b",
}
model = models[6]
task = """
Goal: Open Google Chrome and wait until its window is visible with a page loaded.

Steps:
1. Find the Chrome icon (on the desktop or taskbar) and double-click it.
2. Wait a few seconds for the window to appear.
3. Once you see a Chrome browser window with a webpage or new-tab page visible, the task is complete.
4. Respond with {"tool": "task_complete", "params": {}} as soon as you see the Chrome window — do not click anything else afterward.

Use the graphical interface only. Do not use a terminal or modify Python source code.
"""
pause = 2
agent = ComputerAgent(model,task,pause)
agent.start()