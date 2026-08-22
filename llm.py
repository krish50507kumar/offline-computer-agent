import ollama


class LLM:
    def __init__(self, model="qwen3-vl:2b"):
        self.model = model

    def action(self, true_goal, tools, images, instructions):

        messages = [
            {
                "role": "system",
                "content": instructions
            },
            {
                "role": "user",
                "content": f"""
True goal:
{true_goal}

Available tools:
{tools}

Look at the provided screenshot and determine the next action required
to achieve the true goal.

Return ONLY valid JSON in exactly this format:
Inspect the screenshot and choose the NEXT SINGLE ACTION.

Return ONLY the JSON tool call.

{{
    "tool": "tool_name",
    "params": []
}}

Do not include explanations, markdown, or any text outside the JSON.
I only want json nothing else do not even return your reasoning keep it till your self and only give json,
not my words only json.
""",
                "images": images
            }
        ]

        response = ollama.chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]