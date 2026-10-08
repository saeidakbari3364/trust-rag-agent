from trust_rag_agent.replanner import AdaptiveReplanner


replanner = AdaptiveReplanner()


question = (
    "What are the main challenges "
    "of continual learning in AI agents?"
)


plan = replanner.replan(
    question,
    previous_evidence_count=1,
)


print("\nQuestion:")
print(question)


print("\nAdaptive Re-planning:")

for i, task in enumerate(plan, start=1):

    print(f"{i}. {task}")