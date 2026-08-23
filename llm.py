import ollama


class LLM:
    def __init__(self, model="qwen3-vl:2b"):
        self.model = model

    def action(self, true_goal, tools, images, instructions, model_w, model_h, history=None):
        history_text = ""
        if history:
            history_text = "Your last actions (these did NOT produce the intended result — try a DIFFERENT location or approach, do not repeat the same coordinates):\n"
            for i, h in enumerate(history, 1):
                history_text += f"{i}. {h['tool']} {h['params']}\n"

        messages = [
            {
                "role": "system",
                "content": instructions
            },
            {
                "role": "user",
                "content": f"""Goal: {true_goal}

    Tools: {tools}

    {history_text}
    Image coordinate system:
    - Image size: {model_w} × {model_h} pixels
    - Top-left pixel: (0, 0)
    - Return coordinates as INTEGER PIXEL VALUES within this image, e.g. {{"x": 452, "y": 310}} — NOT normalized 0-1 floats.
    - Valid x range: 0 through {model_w - 1}
    - Valid y range: 0 through {model_h - 1}

    Example:
    {{"tool": "click", "params": {{"x": 300, "y": 400}}}}

    Look at the screenshot. Return the next single action as JSON, using this image's coordinate space.""",
                "images": images
            }
        ]
        response = ollama.chat(model=self.model, messages=messages,think=False,options={"num_predict": 800})
        # print("FULL RESPONSE:", response)
        return response["message"]["content"]