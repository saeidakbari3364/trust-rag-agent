from src.trust_rag_agent.agent import TrustRAGAgent


def main():

    agent = TrustRAGAgent()

    question = (
        "What are the main challenges of continual learning "
        "in AI agents?"
    )

    agent.run(question)


if __name__ == "__main__":
    main()