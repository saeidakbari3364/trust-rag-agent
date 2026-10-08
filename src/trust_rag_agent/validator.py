from .evidence import Evidence


STOP_WORDS = {
    "what",
    "are",
    "the",
    "is",
    "of",
    "for",
    "in",
    "to",
    "a",
    "an",
    "and",
    "on",
    "with",
    "can",
    "do",
    "does",
}


class EvidenceValidator:

    def _important_words(
        self,
        text: str,
    ) -> set[str]:

        return {
            word.strip("?,.!:")
            for word in text.lower().split()
            if word.strip("?,.!:") not in STOP_WORDS
        }

    def validate(
        self,
        question: str,
        evidences: list[Evidence],
        min_score: int = 1,
    ) -> list[Evidence]:

        valid_evidences = []

        question_words = self._important_words(
            question
        )

        for evidence in evidences:

            evidence_words = self._important_words(
                evidence.content
            )

            common_words = (
                question_words
                & evidence_words
            )

            relevance_score = len(
                common_words
            )

            if relevance_score >= min_score:

                valid_evidences.append(
                    evidence
                )

        return valid_evidences

    def is_sufficient(
        self,
        question: str,
        evidences: list[Evidence],
        minimum_evidence: int = 2,
    ) -> bool:

        if len(evidences) < minimum_evidence:
            return False

        question_words = self._important_words(
            question
        )

        relevant_count = 0

        for evidence in evidences:

            evidence_words = self._important_words(
                evidence.content
            )

            common_words = (
                question_words
                & evidence_words
            )

            if len(common_words) >= 2:
                relevant_count += 1

        return relevant_count >= minimum_evidence