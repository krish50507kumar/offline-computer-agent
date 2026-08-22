import json
import re
def available_tools():
    image_coordinate_note = (
        "Coordinates are absolute positions in the provided screenshot image. "
        "Use the image dimensions stated in the prompt, not the physical screen resolution."
    )

    return [
        {
            "name": "click",
            "description": f"Click the left mouse button. {image_coordinate_note}",
            "parameters": {
                "x": {"type": "integer", "description": "Horizontal image coordinate."},
                "y": {"type": "integer", "description": "Vertical image coordinate."},
            },
            "returns": "None",
        },
        {
            "name": "double_click",
            "description": f"Double-click the left mouse button. {image_coordinate_note}",
            "parameters": {
                "x": {"type": "integer", "description": "Horizontal image coordinate."},
                "y": {"type": "integer", "description": "Vertical image coordinate."},
            },
            "returns": "None",
        },
        {
            "name": "move_mouse",
            "description": f"Move the mouse cursor without clicking. {image_coordinate_note}",
            "parameters": {
                "x": {"type": "integer", "description": "Horizontal image coordinate."},
                "y": {"type": "integer", "description": "Vertical image coordinate."},
            },
            "returns": "None",
        },
        {
            "name": "type_text",
            "description": "Type text into the currently focused application or input field.",
            "parameters": {
                "text": {
                    "type": "string",
                    "description": "The exact text to type.",
                }
            },
            "returns": "None",
        },
        {
            "name": "press_key",
            "description": "Press one keyboard key.",
            "parameters": {
                "key": {
                    "type": "string",
                    "description": (
                        "A key such as 'enter', 'escape', 'tab', 'backspace', "
                        "'delete', 'up', 'down', 'left', or 'right'."
                    ),
                }
            },
            "returns": "None",
        },
        {
            "name": "hot_key",
            "description": "Press multiple keyboard keys together.",
            "parameters": {
                "keys": {
                    "type": "array",
                    "description": "Keys to press together, for example ['ctrl', 'l'].",
                }
            },
            "returns": "None",
        },
        {
            "name": "scroll",
            "description": "Scroll vertically. Positive values scroll up; negative values scroll down.",
            "parameters": {
                "amount": {
                    "type": "integer",
                    "description": "Number of scroll units.",
                }
            },
            "returns": "None",
        },
        {
            "name": "drag",
            "description": f"Drag from one point to another. {image_coordinate_note}",
            "parameters": {
                "start_x": {"type": "integer", "description": "Starting horizontal image coordinate."},
                "start_y": {"type": "integer", "description": "Starting vertical image coordinate."},
                "end_x": {"type": "integer", "description": "Ending horizontal image coordinate."},
                "end_y": {"type": "integer", "description": "Ending vertical image coordinate."},
                "duration": {
                    "type": "number",
                    "description": "Drag duration in seconds.",
                },
                "button": {
                    "type": "string",
                    "description": "Mouse button to use, normally 'left'.",
                },
            },
            "returns": "None",
        },
        {
            "name": "wait",
            "description": "Wait before taking the next action.",
            "parameters": {
                "seconds": {
                    "type": "number",
                    "description": "Number of seconds to wait.",
                }
            },
            "returns": "None",
        },
        {
            "name": "alert",
            "description": "Display a message to the user in a GUI alert box.",
            "parameters": {
                "text": {
                    "type": "string",
                    "description": "Message to display.",
                }
            },
            "returns": "None",
        },
        {
            "name": "get_screen_info",
            "description": "Get the physical screen resolution. Do not use it for screenshot coordinates.",
            "parameters": {},
            "returns": "Screen width and height.",
        },
    ]
def instructions():
    return """You are a computer-use agent.

Output exactly ONE valid JSON object. Nothing else.

Format:
{"tool": "<tool_name>", "params": {...}}

Coordinates for click, move_mouse, double_click, and drag are coordinates
in the provided screenshot image—not physical screen coordinates.
Use only values within the image bounds given in the user message.

Rules:
1. Use ONLY the exact parameter names given for that tool in the tools list.
2. Only act on elements visible in the latest screenshot.
3. Never assume a previous action succeeded — verify from the latest screenshot.
4. Never guess coordinates — only click what you can see.
5. Do not modify source code or use a terminal unless explicitly required by the task.
"""



def parse_json_response(response):
    response = response.strip()

    # Remove Markdown code fences
    response = re.sub(r"^```(?:json)?\s*", "", response)
    response = re.sub(r"\s*```$", "", response)

    # Remove single backtick wrappers
    response = re.sub(r"^`(?:json)?\s*", "", response)
    response = re.sub(r"\s*`$", "", response)

    # Find the JSON object
    match = re.search(r"\{.*\}", response, re.DOTALL)

    if not match:
        raise ValueError(f"No JSON object found: {response!r}")

    return json.loads(match.group(0))