import ollama


class LLM:
    def __init__(self, model="qwen3-vl:2b"):
        self.model = model

    def action(self, true_goal, tools, images, instructions, model_w, model_h):
        messages = [
            {
                "role": "system",
                "content": instructions
            },
            {
                "role": "user",
                "content": f"""Goal: {true_goal}

    Tools: {tools}

    Image coordinate system:
    - Image size: {model_w} × {model_h} pixels
    - Top-left pixel: (0, 0)
    - Valid x range: 0 through {model_w - 1}
    - Valid y range: 0 through {model_h - 1}
    - Return coordinates in this resized screenshot's coordinate system.
    - Do NOT use the physical monitor resolution.

    Example:
    {{"tool": "click", "params": {{"x": 300, "y": 400}}}}

    Look at the screenshot. Return the next single action as JSON, using this image's coordinate space.""",
                "images": images
            }
        ]
        response = ollama.chat(model=self.model, messages=messages)
        return response["message"]["content"]