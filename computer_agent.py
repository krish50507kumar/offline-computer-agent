from config import available_tools,instructions,parse_json_response
from llm import LLM
from computer import capture_for_model
from tools import Tools
import json
import time
from pathlib import Path
import logging
logger = logging.getLogger(__name__)
class ComputerAgent:
    def __init__(self,model,task,pause = 2):
        self.tools = available_tools()
        self.task = task
        self.tool = Tools()
        self.vision_model = LLM(model)
        self.instruction = instructions()
        self.screenshot_path = Path(r"D:\workspace\Dev tools\PythonProjects\AgenticAi\screenshots\screenshot.png")
        self.completed = 0
        self.pause = pause
        Path("screenshots").mkdir(exist_ok=True)

    def observe(self):
        screenshot_path, scale_x, scale_y, model_w, model_h=capture_for_model(self.screenshot_path)
        return screenshot_path, scale_x, scale_y, model_w, model_h

    def reason(self,screenshot_path, scale_x, scale_y, model_w, model_h):
        response = self.vision_model.action(
            self.task,
            self.tools,
            [screenshot_path],
            self.instruction,
            model_w,
            model_h,
        )
        try:
            act = parse_json_response(response)
            logger.info("RAW RESPONSE: %s", response)
            return act
        except json.JSONDecodeError:
            logger.info("INVALID JSON FROM MODEL")
            logger.info("RAW RESPONSE: %s", response)

        return {}

    def execute(self,act , scale_x, scale_y, model_w, model_h):
        tool_name = act["tool"]
        params = act.get("params", {})
        if "x" in params:
            x = params["x"]
            y = params["y"]

            if not (0 <= x < model_w and 0 <= y < model_h):
                logger.info(f"INVALID MODEL COORDINATES: ({x}, {y})")
        if tool_name == "task_complete":
            logger.info("MODEL CLAIMED TASK COMPLETE")
        self.tool.action(act, scale_x=scale_x, scale_y=scale_y)
        time.sleep(self.pause)
    def start(self):
        logger.info("STARTED")
        while not self.completed:
            screenshot_path, scale_x, scale_y, model_w, model_h = self.observe()
            act = self.reason(screenshot_path, scale_x, scale_y, model_w, model_h)
            if act == {}:
                continue
            self.execute(act, scale_x, scale_y, model_w, model_h)
        logger.info(f"COMPLETED")
