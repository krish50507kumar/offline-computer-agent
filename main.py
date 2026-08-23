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
Goal: Open Google Chrome, then navigate to YouTube (youtube.com).

Steps:
1. Check the screenshot first. If a Chrome window is already open, skip to step 3 — do NOT double-click the Chrome icon again.
2. If Chrome is not open, find the Chrome icon (on the desktop or taskbar) and double-click it ONCE. Then wait a few seconds for the window to appear.
3. Use hot_key with keys ["ctrl", "l"] to focus the browser's address bar. Do NOT click on the address bar directly.
4. Type "youtube.com" using type_text.
5. Press "enter" to navigate to the page.
6. Wait a few seconds for the YouTube homepage to load — look for the YouTube logo and video thumbnails.
7. Once YouTube is visible and loaded, the task is complete.
8. Respond with {"tool": "task_complete", "params": {}} as soon as you see YouTube loaded — do not click anything else afterward.

Use the graphical interface only. Do not use a terminal or modify Python source code.
"""
pause = 2
agent = ComputerAgent(model,task,pause)
agent.start()