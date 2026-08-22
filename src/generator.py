from transformers import pipeline


class TextGenerator:
    def __init__(self):
        print("Loading GPT-2 model...")

        self.generator = pipeline(
            "text-generation",
            model="gpt2"
        )

        print("GPT-2 model loaded successfully.")

    def generate(self, prompt, max_length=100):
        result = self.generator(
            prompt,
            max_length=max_length,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7,
            pad_token_id=50256
        )

        return result[0]["generated_text"]