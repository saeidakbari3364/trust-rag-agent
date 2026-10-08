from trust_rag_agent.evidence import EvidenceRetriever


retriever = EvidenceRetriever()

question = (
    "What are the main challenges "
    "of continual learning in AI agents?"
)

evidences = retriever.retrieve(question)

print("\nQuestion:")
print(question)

print("\nRetrieved Evidence:")

for i, evidence in enumerate(evidences, start=1):

    print(f"\nEvidence {i}")
    print(f"Source: {evidence.source}")
    print(f"Content: {evidence.content}")