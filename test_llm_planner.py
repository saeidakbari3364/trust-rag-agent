from dotenv import load_dotenv

from src.trust_rag_agent.llm_planner import LLMPlanner


load_dotenv()


planner = LLMPlanner()

question = (
    "What are the main challenges "
    "of continual learning in AI agents?"
)

plan = planner.create_plan(question)

print("\nQuestion:")
print(question)

print("\nGenerated Plan:")

for task in plan.tasks:
    print(f"{task.id}. {task.description}")