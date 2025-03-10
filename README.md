# Math Assistant Crew

Math Assistant Crew is an AI-powered project designed to answer mathematical problems with detailed reasoning and step-by-step explanations. Built using Crew AI, this project aims to provide accurate, well-structured solutions to complex math queries while enhancing users' understanding of problem-solving techniques.


## Features

- AI-driven problem-solving with reasoning

- Step-by-step explanations for better understanding

- Support for various mathematical topics (algebra, geometry, calculus, etc.)

- Customizable workflow for different problem types

## Prerequisites

Before you begin, ensure you have the following installed:

- Python >=3.10 <3.13

- pip (Python package manager)

- A compatible Large Language Model (e.g., OpenAI, Anthropic, etc.)

- API keys for LLM providers

## Installation

Clone the repository and install dependencies:
```
# Clone the repository

git clone https://github.com/huongtravo0910/ai_agent_math_assistant.git

cd ai_agent_math_assistant

# Create a virtual environment

python -m venv math_assistant_env

source math_assistant/bin/activate  

# On Windows use `math_assistant\\Scripts\\activate`

```

## Configuration

Create a `.env` file in the project root and add your API keys:

```
API_KEY=your_api_key
MODEL=your_model
```

## Preparing the Problem

Before running the project, add your question to the problem.txt file:

```
echo "Your question here" > problem.txt
```

## Running the Project

Run the main script to start the Crew AI agents:

```
crewai run
```


## Customization

Modify agents/ to define your own AI agents.

Adjust tasks/ to orchestrate tasks as per your needs.

Update .env to use different API keys or services.

## Troubleshooting

API Errors: Ensure your API keys are correct and active.

Virtual Environment Issues: Ensure the virtual environment is activated.

---

Happy Coding! 🚀

