class SafetyChecker:

    def check(
        self,
        answer: str,
        evidences: list,
    ) -> bool:

        if not answer.strip():
            return False

        if not evidences:
            return False

        evidence_text = " ".join(
            evidence.content.lower()
            for evidence in evidences
        )

        answer_words = set(
            answer.lower().split()
        )

        evidence_words = set(
            evidence_text.split()
        )

        common_words = (
            answer_words & evidence_words
        )

        # Simple grounding check
        if len(common_words) < 5:
            return False

        return True