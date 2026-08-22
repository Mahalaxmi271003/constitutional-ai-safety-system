from src.generator import TextGenerator
from src.evaluator import SafetyEvaluator


class ConstitutionalAISafetySystem:
    def __init__(self, max_retries=3):
        self.generator = TextGenerator()
        self.evaluator = SafetyEvaluator()
        self.max_retries = max_retries

    def generate_safe_response(self, prompt):
        attempts = []

        for attempt in range(1, self.max_retries + 1):

            response = self.generator.generate(prompt)

            evaluation = self.evaluator.evaluate(response)

            attempts.append({
                "attempt": attempt,
                "response": response,
                "evaluation": evaluation
            })

            if evaluation["is_safe"]:
                return {
                    "prompt": prompt,
                    "final_response": response,
                    "status": "SAFE",
                    "attempts": attempts
                }

        return {
            "prompt": prompt,
            "final_response": attempts[-1]["response"],
            "status": "REVIEW_REQUIRED",
            "attempts": attempts
        }