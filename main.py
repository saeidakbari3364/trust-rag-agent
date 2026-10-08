from dotenv import load_dotenv


from src.trust_rag_agent.agent import TrustRAGAgent


load_dotenv()


def main():

    agent = TrustRAGAgent()

    question = (
        "What are the challenges of quantum computing "
    "for AI agents?"
    )

    agent.run(question)


if __name__ == "__main__":
    main()