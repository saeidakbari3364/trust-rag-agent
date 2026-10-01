from trust_rag_agent.planner import Planner


def test_planner_creates_tasks():

    planner = Planner()

    plan = planner.create_plan(
        "What is continual learning?"
    )

    assert len(plan) == 4
    assert plan[0].description == "Understand the user question"