from pathlib import Path


class Evidence:

    def __init__(
        self,
        source: str,
        content: str,
        score: int,
    ):
        self.source = source
        self.content = content
        self.score = score


class EvidenceRetriever:

    def __init__(self, knowledge_dir: str = "knowledge"):

        self.knowledge_dir = Path(knowledge_dir)

    def retrieve(
        self,
        question: str,
    ) -> list[Evidence]:

        evidences = []

        question_words = set(
            question.lower().split()
        )

        for file_path in self.knowledge_dir.glob("*.txt"):

            text = file_path.read_text(
                encoding="utf-8"
            )

            paragraphs = text.split("\n\n")

            for paragraph in paragraphs:

                paragraph_words = set(
                    paragraph.lower().split()
                )

                score = len(
                    question_words
                    & paragraph_words
                )

                if score > 0:

                    evidences.append(
                        Evidence(
                            source=file_path.name,
                            content=paragraph,
                            score=score,
                        )
                    )

        evidences.sort(
            key=lambda evidence: evidence.score,
            reverse=True,
        )

        return evidences