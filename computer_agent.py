from config import available_tools, instructions, parse_json_response
from llm import LLM
from computer import capture_for_model
from tools import Tools
import json
import time
from pathlib import Path
import logging
logger = logging.getLogger(__name__)


class ComputerAgent:
    def __init__(self, model, task, pause=2, history_limit=4):
        self.tools = available_tools()
        self.task = task
        self.tool = Tools()
        self.vision_model = LLM(model)
        self.instruction = instructions()
        self.screenshot_path = Path(r"D:\workspace\Dev tools\PythonProjects\AgenticAi\screenshots\screenshot.png")
        self.completed = 0
        self.pause = pause
        self.history = []
        self.history_limit = history_limit
        Path("screenshots").mkdir(exist_ok=True)

    def observe(self):
        screenshot_path, scale_x, scale_y, model_w, model_h, pad_top = capture_for_model(self.screenshot_path)
        return screenshot_path, scale_x, scale_y, model_w, model_h, pad_top

    def reason(self, screenshot_path, scale_x, scale_y, model_w, model_h):
        response = self.vision_model.action(
            self.task, self.tools, [screenshot_path], self.instruction,
            model_w, model_h, history=self.history,
        )
        try:
            act = parse_json_response(response)
            logger.info("RAW RESPONSE: %s", response)
            return act
        except (json.JSONDecodeError, ValueError):
            logger.info("INVALID/EMPTY JSON FROM MODEL")
            logger.info("RAW RESPONSE: %s", response)
            return {}

    def execute(self, act, scale_x, scale_y, model_w, model_h, pad_top):
        tool_name = act["tool"]
        params = act.get("params", {})
        if "x" in params:
            x = params["x"]
            y = params["y"]

            if not (0 <= x < model_w and 0 <= y < model_h):
                logger.info(f"INVALID MODEL COORDINATES: ({x}, {y})")
        if tool_name == "task_complete":
            logger.info("MODEL CLAIMED TASK COMPLETE")
        self.tool.action(act, scale_x=scale_x, scale_y=scale_y, pad_top=pad_top)
        time.sleep(self.pause)

        self.history.append({"tool": tool_name, "params": params})
        self.history = self.history[-self.history_limit:]

    def start(self):
        logger.info("STARTED")
        while not self.completed:
            screenshot_path, scale_x, scale_y, model_w, model_h, pad_top = self.observe()
            act = self.reason(screenshot_path, scale_x, scale_y, model_w, model_h)
            if act == {}:
                continue
            self.execute(act, scale_x, scale_y, model_w, model_h, pad_top)
        logger.info(f"COMPLETED")