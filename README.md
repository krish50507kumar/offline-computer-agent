# Offline Computer Agent

An AI-powered computer-use agent that can understand a user's task, reason about the required actions, and interact with the computer through automated tools.

The project is designed around a local/offline-first architecture, allowing the agent to use a locally running language/vision model instead of depending entirely on cloud APIs.

## Features

- AI-powered task execution
- Local LLM integration
- Computer interaction through Python
- Tool-based agent architecture
- Screenshot-based computer interaction
- Configurable model settings
- Modular architecture
- Python-based implementation
- Offline/local model support

## Architecture

The project is divided into several modules:

```text
                    ┌────────────────────┐
                    │      User Task     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      Computer      │
                    │    computer.py     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │       Agent        │
                    │ computer_agent.py  │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │        LLM         │
                    │      llm.py        │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │       Tools        │
                    │     tools.py       │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │  Operating System  │
                    └────────────────────┘
```

## Project Structure

```text
AgenticAi/
│
├── computer_agent.py
├── computer.py
├── config.py
├── llm.py
├── main.py
├── tools.py
├── requirements.txt
├── .gitignore
│
├── screenshots/
│
└── README.md
```
### `computer.py`

Captures the screenshots of the screen.

Computer handle the screenshot scaling issues and make's the image work for any screen size.


### `computer_agent.py`

Contains the core agent logic.

The agent receives a task, communicates with the model, interprets the model's response, and determines which action should be executed.


### `llm.py`

Handles communication with the language/vision model.

The LLM acts as the reasoning component of the system and determines what the agent should do based on the current task and available information.

default model : **qwen3-vl:2b**


### `config.py`

Contains configuration used by the application, such as model settings and other configurable parameters.

### `tools.py`

Contains the tools available to the agent.

Tools allow the model to perform actions instead of simply generating text.


## Requirements

- Python 3.12+
- Windows
- Sufficient RAM for the selected local model
- GPU recommended for running vision-capable local models

A dedicated NVIDIA GPU can significantly improve local model performance.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/krish50507kumar/offline-computer-agent.git
cd offline-computer-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Configure the model and other settings in:

```text
config.py
```

The exact configuration depends on the local model/backend being used.

For local inference, make sure the required model is installed and available before starting the agent.

## Running the Agent

Run:

```bash
python main.py
```

The agent will start and wait for the specified task.

For example:

```text
Open Chrome and search for Python tutorials
```

The agent can then analyze the task and execute the required computer actions through its available tools.

## How It Works

The basic execution loop is:

```text
User Task
   │
   ▼
Agent receives task
   │
   ▼
Model analyzes task
   │
   ▼
Model selects an action
   │
   ▼
Tool executes action
   │
   ▼
Computer state changes
   │
   ▼
New screenshot/state
   │
   ▼
Model analyzes updated state
   │
   ▼
Repeat until task is completed
```

This allows the system to operate as an agent rather than simply producing a text response.

## Design Goals

The project is being developed with the following goals:

- Run AI models locally
- Reduce dependence on external APIs
- Enable computer-use automation
- Build a modular agent architecture
- Experiment with vision-language models
- Provide a foundation for more advanced autonomous computer interaction

## Current Limitations

This project is experimental.

The agent's reliability depends heavily on the capabilities of the selected model. Vision models can occasionally misinterpret screenshots, generate invalid actions, or fail to follow the expected output format.

Computer automation also carries inherent risks. An incorrectly generated action can potentially interact with the wrong application or UI element.

Use the agent in a controlled environment while developing and testing it.

## Roadmap

- [ ] Improve action parsing
- [ ] Improve screenshot understanding
- [ ] Add more computer tools
- [ ] Add action retry mechanisms
- [ ] Add task planning and memory
- [ ] Improve error handling
- [ ] Add safety checks before destructive actions
- [ ] Improve local model compatibility
- [ ] Add better logging and debugging
- [ ] Improve autonomous multi-step task execution

## Technologies

- Python
- Local LLM/VLM inference
- Computer automation
- Vision-based interaction
- Agentic AI architecture

## Project Status

**Experimental / Active Development**

The architecture and model integration are still evolving. APIs, tools, and configuration may change as the project develops.

## Author

**Krish Kumar**

GitHub:  
https://github.com/krish50507kumar

## License
Apache License 2.0

This project is currently under development.
