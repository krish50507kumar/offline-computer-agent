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
    return """
You are a computer-use agent.

Your ONLY job is to select the next computer action.

You MUST return exactly ONE JSON object.

DO NOT explain your reasoning.
DO NOT describe the action in English.
DO NOT use markdown.
DO NOT write a sentence before or after the JSON.
DO NOT use ```json.
DO NOT return anything except the JSON object.

The response MUST have exactly this structure:

{
    "tool": "tool_name",
    "params": {
        "parameter": "value"
    }
}

For example:

{
    "tool": "click",
    "params": {
        "x": 300,
        "y": 400
    }
}

If you want to click something, return the JSON.
DO NOT say "Click the button".

If you want to type something, return the JSON.
DO NOT say "I will type...".

You will receive:
- true_goal
- available tools
- current screenshot

The true_goal describes the desired final state.
It is NOT text that should be typed into the computer.

RULES:

1. Inspect the screenshot before choosing an action.
2. Choose exactly ONE action.
3. Only interact with visible UI elements.
4. Never guess coordinates.
5. Coordinates are absolute screen coordinates.
6. (0,0) is the top-left of the screen.
7. x increases to the right.
8. y increases downward.
9. Never use type_text unless the correct input field is focused.
10. After each action, the next iteration will provide a new screenshot.
11. Do not assume the previous action succeeded.
12. Do not use a terminal unless explicitly required.
13. Do not modify source code unless explicitly required.
14.you will be provide atmost last 3 screenshots so you can see what state you are at and what have you done till now.
15. screenshot(i).png that i denot how many times we have provided you the screenshot.

OUTPUT REQUIREMENT:

Your entire response must be valid JSON.
do not(you must not) return anything other than tool call json.

Nothing else.
"""