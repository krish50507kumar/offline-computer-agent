def available_tools():
    return [
        {
            "name": "click",
            "description": "Click the left mouse button at an absolute screen coordinate.",
            "parameters": {
                "x": {
                    "type": "integer",
                    "description": "Horizontal screen coordinate."
                },
                "y": {
                    "type": "integer",
                    "description": "Vertical screen coordinate."
                }
            },
            "returns": "None"
        },
        {
            "name": "double_click",
            "description": "Double-click the left mouse button at an absolute screen coordinate.",
            "parameters": {
                "x": {
                    "type": "integer",
                    "description": "Horizontal screen coordinate."
                },
                "y": {
                    "type": "integer",
                    "description": "Vertical screen coordinate."
                }
            },
            "returns": "None"
        },
        {
            "name": "move_mouse",
            "description": "Move the mouse cursor to an absolute screen coordinate without clicking.",
            "parameters": {
                "x": {
                    "type": "integer",
                    "description": "Horizontal screen coordinate."
                },
                "y": {
                    "type": "integer",
                    "description": "Vertical screen coordinate."
                }
            },
            "returns": "None"
        },
        {
            "name": "type_text",
            "description": "Type text using the keyboard into the currently focused application or input field.",
            "parameters": {
                "text": {
                    "type": "string",
                    "description": "The exact text to type."
                }
            },
            "returns": "None"
        },
        {
            "name": "press_key",
            "description": "Press a single keyboard key.",
            "parameters": {
                "key": {
                    "type": "string",
                    "description": "Key to press, such as 'enter', 'escape', 'tab', 'backspace', 'delete', 'up', 'down', 'left', or 'right'."
                }
            },
            "returns": "None"
        },
        {
            "name": "hot_key",
            "description": "Press multiple keyboard keys together, such as Ctrl+L or Ctrl+C.",
            "parameters": {
                "keys": {
                    "type": "array",
                    "description": "Keys to press together, for example ['ctrl', 'l']."
                }
            },
            "returns": "None"
        },
        {
            "name": "scroll",
            "description": "Scroll vertically. Positive values scroll up and negative values scroll down.",
            "parameters": {
                "amount": {
                    "type": "integer",
                    "description": "Number of scroll units. Positive for up, negative for down."
                }
            },
            "returns": "None"
        },
        {
            "name": "drag",
            "description": "Drag the mouse from one screen coordinate to another.",
            "parameters": {
                "start_x": {
                    "type": "integer",
                    "description": "Starting horizontal coordinate."
                },
                "start_y": {
                    "type": "integer",
                    "description": "Starting vertical coordinate."
                },
                "end_x": {
                    "type": "integer",
                    "description": "Destination horizontal coordinate."
                },
                "end_y": {
                    "type": "integer",
                    "description": "Destination vertical coordinate."
                },
                "duration": {
                    "type": "number",
                    "description": "Duration of the drag in seconds."
                },
                "button": {
                    "type": "string",
                    "description": "Mouse button to use, normally 'left'."
                }
            },
            "returns": "None"
        },
        {
            "name": "wait",
            "description": "Wait for a specified number of seconds before taking the next action.",
            "parameters": {
                "seconds": {
                    "type": "number",
                    "description": "Number of seconds to wait."
                }
            },
            "returns": "None"
        },
        {
            "name": "alert",
            "description": "Display a message to the user using a GUI alert box.",
            "parameters": {
                "text": {
                    "type": "string",
                    "description": "Message to display to the user."
                }
            },
            "returns": "None"
        },
        {
            "name": "get_screen_info",
            "description": "Get the current screen resolution.",
            "parameters": {},
            "returns": "Screen width and height."
        }
    ]
def instructions():
    return """You are a computer-use agent.

Output exactly ONE JSON object. Nothing else. No text, no markdown, no explanation, no reasoning.

Format:
{{"tool": "<tool_name>", "params": {{...}}}}

Rules:
1. Use ONLY the exact parameter names given for that tool in the tools list.
2. Only act on elements visible in the current screenshot.
3. Never assume a previous action succeeded — verify from the latest screenshot.
4. Never guess coordinates — only click what you can see.
5. Do not modify source code or use a terminal unless explicitly required by the task.

Output must be valid JSON and nothing but JSON."""

import json
import re

def parse_json_response(response):
    response = response.strip()

    match = re.search(r"\{.*\}", response, re.DOTALL)

    if not match:
        raise ValueError(f"No JSON object found: {response!r}")

    return json.loads(match.group(0))