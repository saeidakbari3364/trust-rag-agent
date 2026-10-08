class AdaptiveReplanner:

    def replan(
        self,
        question: str,
        previous_evidence_count: int,
    ) -> list[str]:

        if previous_evidence_count == 0:

            return [
                "Broaden the search query",
                "Search additional knowledge sources",
                "Validate the newly retrieved evidence",
            ]

        return [
            "Refine the search query",
            "Retrieve additional evidence",
            "Validate the new evidence",
        ]

    def create_search_query(
        self,
        question: str,
    ) -> str:

        important_words = [
            word.strip("?,.!:")
            for word in question.split()
            if len(word.strip("?,.!:")) > 3
        ]

        return " ".join(
            important_words
        )