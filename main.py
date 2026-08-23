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
Double-click the Google Chrome icon on the desktop to open it.
Use the graphical interface only. Do not use a terminal or modify Python source code.
"""
pause = 2
agent = ComputerAgent(model,task,pause)
agent.start()