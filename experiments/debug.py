import ollama
from pathlib import Path

models = {
    1: "qwen3-vl:2b",
    2: "qwen2.5vl:3b",
    3: "gemma3:4b",
    4: "qwen3-vl:4b",
}
model = models[4]

image = Path(r"D:\workspace\Dev tools\PythonProjects\AgenticAi\screenshots\screenshot1.png")
message = []
while True:
    user_input = input("prompt||exit: ")
    if user_input == "exit":
        break
    message += [
        {
            "role": "user",
            "content": user_input,
            "images": [str(image)],
        }
    ]
    response = ollama.chat(model=model, messages=message)
    print("LLM: " + response["message"]["content"])
    message +=[
        {
            "role":"LLM",
            "content": response["message"]["content"],
        }
    ]