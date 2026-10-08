import os
import json
import subprocess

from .evidence import Evidence


class AnswerGenerator:

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

    def generate(
        self,
        question: str,
        evidences: list[Evidence],
    ) -> str:

        # Use only the top 3 verified evidence items
        selected_evidences = evidences[:3]

        evidence_text = "\n\n".join(
            [
                (
                    f"Source: {evidence.source}\n"
                    f"Evidence: {evidence.content}"
                )
                for evidence in selected_evidences
            ]
        )

        system_prompt = (
            "You are a trustworthy question-answering agent.\n\n"
            "Answer the user's question ONLY using "
            "the provided evidence.\n\n"
            "Do not use outside knowledge.\n"
            "Do not invent facts.\n"
            "If the evidence is insufficient, "
            "say that the evidence is insufficient.\n"
            "Give a short and clear answer."
        )

        user_prompt = (
            f"Question:\n"
            f"{question}\n\n"
            f"Verified Evidence:\n"
            f"{evidence_text}"
        )

        payload = {
            "model": "qwen/qwen3.7-flash:free",
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        }

        payload_json = json.dumps(
            payload,
            ensure_ascii=False,
        )

        # Send JSON through stdin instead of
        # passing it as a command-line argument.
        result = subprocess.run(
            [
                "curl",
                "-4",
                "--http1.1",
                "--silent",
                "--show-error",
                "--max-time",
                "120",
                self.url,
                "-H",
                f"Authorization: Bearer {self.api_key}",
                "-H",
                "Content-Type: application/json",
                "--data-binary",
                "@-",
            ],
            input=payload_json,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        if result.returncode != 0:

            raise RuntimeError(
                "LLM API request failed.\n"
                f"curl exit code: {result.returncode}\n"
                f"curl error: {result.stderr}"
            )

        if not result.stdout.strip():

            raise RuntimeError(
                "LLM API returned an empty response."
            )

        try:

            response_data = json.loads(
                result.stdout
            )

        except json.JSONDecodeError as e:

            raise RuntimeError(
                "Invalid JSON response from LLM API.\n"
                f"Response: {result.stdout}"
            ) from e

        try:

            return (
                response_data["choices"][0]
                ["message"]["content"]
            )

        except (KeyError, IndexError) as e:

            raise RuntimeError(
                "Unexpected response format from LLM API.\n"
                f"Response: {response_data}"
            ) from e