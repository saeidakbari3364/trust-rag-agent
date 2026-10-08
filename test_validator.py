from trust_rag_agent.evidence import EvidenceRetriever
from trust_rag_agent.validator import EvidenceValidator


retriever = EvidenceRetriever()

validator = EvidenceValidator()


question = (
    "What are the main challenges "
    "of continual learning in AI agents?"
)


evidences = retriever.retrieve(question)


valid_evidences = validator.validate(
    question,
    evidences,
)


print("\nQuestion:")
print(question)


print("\nValid Evidence:")

for i, evidence in enumerate(
    valid_evidences,
    start=1,
):

    print(f"\nEvidence {i}")
    print(f"Score: {evidence.score}")
    print(f"Source: {evidence.source}")
    print(f"Content: {evidence.content}")