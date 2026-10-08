from .planner import Planner
from .evidence import EvidenceRetriever
from .validator import EvidenceValidator
from .replanner import AdaptiveReplanner
from .answer_generator import AnswerGenerator
from .safety import SafetyChecker


class TrustRAGAgent:

    def __init__(self):

        self.planner = Planner()

        self.retriever = EvidenceRetriever()

        self.validator = EvidenceValidator()

        self.replanner = AdaptiveReplanner()

        self.answer_generator = AnswerGenerator()

        self.safety_checker = SafetyChecker()

    def run(self, question: str):

        print("\nQuestion:")
        print(question)

        # --------------------------------------------------
        # 1. Planning
        # --------------------------------------------------

        print("\n[1] Planning...")

        plan = self.planner.create_plan(
            question
        )

        for task in plan:

            print(
                f"{task.id}. "
                f"{task.description}"
            )

        # --------------------------------------------------
        # 2. Evidence Retrieval
        # --------------------------------------------------

        print(
            "\n[2] Retrieving evidence..."
        )

        evidences = self.retriever.retrieve(
            question
        )

        print(
            f"Retrieved {len(evidences)} "
            "evidence items."
        )

        # --------------------------------------------------
        # 3. Evidence Validation
        # --------------------------------------------------

        print(
            "\n[3] Validating evidence..."
        )

        valid_evidences = self.validator.validate(
            question,
            evidences,
        )

        print(
            f"Valid evidence: "
            f"{len(valid_evidences)}"
        )

        # --------------------------------------------------
        # 4. Check Evidence Sufficiency
        # --------------------------------------------------

        sufficient = self.validator.is_sufficient(
            question,
            valid_evidences,
        )

        if not sufficient:

            print(
                "\n[4] Evidence is insufficient."
            )

            # --------------------------------------------------
            # 5. Adaptive Re-planning
            # --------------------------------------------------

            print(
                "\n[5] Adaptive re-planning..."
            )

            new_plan = self.replanner.replan(
                question,
                len(valid_evidences),
            )

            for i, task in enumerate(
                new_plan,
                start=1,
            ):

                print(
                    f"{i}. {task}"
                )

            # --------------------------------------------------
            # Create New Search Query
            # --------------------------------------------------

            new_query = (
                self.replanner.create_search_query(
                    question
                )
            )

            print(
                "\nNew search query:"
            )

            print(new_query)

            # --------------------------------------------------
            # 6. Retrieve Again
            # --------------------------------------------------

            print(
                "\n[6] Re-retrieving evidence..."
            )

            new_evidences = (
                self.retriever.retrieve(
                    new_query
                )
            )

            print(
                f"Retrieved "
                f"{len(new_evidences)} "
                "new evidence items."
            )

            # --------------------------------------------------
            # 7. Validate Again
            # --------------------------------------------------

            print(
                "\n[7] Re-validating evidence..."
            )

            new_valid_evidences = (
                self.validator.validate(
                    question,
                    new_evidences,
                )
            )

            print(
                "Valid evidence after "
                "re-planning: "
                f"{len(new_valid_evidences)}"
            )

            # --------------------------------------------------
            # Check Again
            # --------------------------------------------------

            new_sufficient = (
                self.validator.is_sufficient(
                    question,
                    new_valid_evidences,
                )
            )

            if not new_sufficient:

                print(
                    "\nEvidence is still "
                    "insufficient."
                )

                print(
                    "Agent cannot provide "
                    "a trustworthy answer."
                )

                return None

            # --------------------------------------------------
            # Generate Answer After Re-planning
            # --------------------------------------------------

            print(
                "\n[8] Generating answer "
                "from new evidence..."
            )

            answer = (
                self.answer_generator.generate(
                    question,
                    new_valid_evidences,
                )
            )

            print(
                "\nAnswer:"
            )

            print(answer)

            # --------------------------------------------------
            # Safety Check
            # --------------------------------------------------

            print(
                "\n[9] Safety check..."
            )

            is_safe = (
                self.safety_checker.check(
                    answer,
                    new_valid_evidences,
                )
            )

            if is_safe:

                print(
                    "Safety check: PASSED"
                )

            else:

                print(
                    "Safety check: FAILED"
                )

            return answer

        # --------------------------------------------------
        # Normal Answer Generation
        # --------------------------------------------------

        print(
            "\n[4] Evidence is sufficient."
        )

        print(
            "\n[5] Generating answer..."
        )

        answer = (
            self.answer_generator.generate(
                question,
                valid_evidences,
            )
        )

        print(
            "\nAnswer:"
        )

        print(answer)

        # --------------------------------------------------
        # Safety Check
        # --------------------------------------------------

        print(
            "\n[6] Safety check..."
        )

        is_safe = (
            self.safety_checker.check(
                answer,
                valid_evidences,
            )
        )

        if is_safe:

            print(
                "Safety check: PASSED"
            )

        else:

            print(
                "Safety check: FAILED"
            )

        return answer