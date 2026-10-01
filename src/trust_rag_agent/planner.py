from pydantic import BaseModel


class Task(BaseModel):
    id: int
    description: str


class Planner:

    def create_plan(self, question: str) -> list[Task]:
        return [
            Task(
                id=1,
                description="Understand the user question"
            ),
            Task(
                id=2,
                description="Retrieve relevant evidence"
            ),
            Task(
                id=3,
                description="Validate the evidence"
            ),
            Task(
                id=4,
                description="Generate an evidence-based answer"
            ),
        ]