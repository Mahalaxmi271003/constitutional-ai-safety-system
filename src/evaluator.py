from transformers import pipeline


class SafetyEvaluator:
    def __init__(self):
        print("Loading BERT safety evaluator...")

        self.classifier = pipeline(
            "text-classification",
            model="unitary/toxic-bert"
        )

        print("BERT safety evaluator loaded successfully.")

    def evaluate(self, text):
        result = self.classifier(text)[0]

        label = result["label"]
        score = result["score"]

        # Only flag the response when the toxic prediction
        # has sufficiently high confidence.
        is_safe = not (
            label.lower() == "toxic" and score >= 0.5
        )

        return {
            "label": label,
            "score": round(score, 4),
            "is_safe": is_safe
        }