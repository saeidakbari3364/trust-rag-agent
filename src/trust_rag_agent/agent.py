from app.planner import Planner


class TrustRAGAgent:

    def __init__(self):
        self.planner = Planner()

    def run(self, question: str):

        plan = self.planner.create_plan(question)

        print("\nQuestion:")
        print(question)

        print("\nPlan:")

        for task in plan:
            print(f"{task.id}. {task.description}")

        return plan