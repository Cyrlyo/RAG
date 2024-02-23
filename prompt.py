MESSAGE_TEMPLATE = {
    "role": "user",
    "content": None
}

class oneshot():
    def __init__(self) -> None:
        self.message_template = MESSAGE_TEMPLATE

    def sentiment_basics(self, review: str) -> dict:

        self.message_template["content"] = f"Give me the sentiment of this review: '{review}'"

        return self.message_template

    def sentiment_basics_1(self, review: str) -> dict:

        self.message_template["content"] = f"Give me the sentiment of this review: '{review}'. Answer with 1 word, 'positive' or 'negative'"

        return self.message_template


    def sentiment_basics_2(self, review: str) -> dict:

        self.message_template["content"] = f"Give me the sentiment of this review: '{review}'. The first word of your answer have to be 'positive' or 'negative'"

        return self.message_template

    def sentiment_augmented(self, review: str) -> dict:

        self.message_template["content"] = f"Classify the text into negative or positive. \nText: {review}\nSentiment:"

        return self.message_template

    def sentiment_augmented_1(self, review: str) -> dict:

        self.message_template["content"] = f"Classify the text into negative or positive, the first word of your answer will be one of those. \nText: {review}\nSentiment:"

        return self.message_template

