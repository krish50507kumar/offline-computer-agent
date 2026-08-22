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

    Image size: {model_w}x{model_h}. (0,0) = top-left. x: 0-{model_w}. y: 0-{model_h}.

    Example:
    {{"tool": "click", "params": {{"x": 300, "y": 400}}}}

    Look at the screenshot. Return the next single action as JSON, using this image's coordinate space.""",
                "images": images
            }
        ]
        response = ollama.chat(model=self.model, messages=messages)
        return response["message"]["content"]