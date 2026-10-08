import os
import json
import subprocess

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    description: str


class Plan(BaseModel):
    tasks: list[Task]


class LLMPlanner:

    def __init__(self):

        api_key = os.getenv("API_KEY")

        if not api_key:
            raise ValueError(
                "API_KEY is not set."
            )

        self.api_key = api_key

        self.url = (
            "https://api.bazaarlink.ai/v1/chat/completions"
        )

    def create_plan(self, question: str) -> Plan:

        system_prompt = """
You are an AI planning module.

Create a short and logical plan for answering
the user's question.

Return ONLY valid JSON.

The JSON must have exactly this structure:

{
    "tasks": [
        {
            "id": 1,
            "description": "..."
        }
    ]
}

Return between 3 and 5 tasks.
"""

        payload = {
            "model": "qwen/qwen3.7-flash:free",
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        }

        result = subprocess.run(
    [
        "curl",
        "--silent",
        "--show-error",
        "--http1.1",
        self.url,
        "-H",
        f"Authorization: Bearer {self.api_key}",
        "-H",
        "Content-Type: application/json",
        "-d",
        json.dumps(payload, ensure_ascii=False),
    ],
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
    check=True,
)

        response_data = json.loads(result.stdout)

        content = (
            response_data["choices"][0]
            ["message"]["content"]
        )

        data = json.loads(content)

        return Plan(**data)