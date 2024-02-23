import pandas as pd
import random

MESSAGE_TEMPLATE = {
    "role": "user",
    "content": None
}

class zeroshot():
    def __init__(self) -> None:
        self.message_template = MESSAGE_TEMPLATE

    def ask(self, message):
        self.message_template["content"] = message
        return self.message_template

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

class oneshot():
    def __init__(self) -> None:
        self.template = {
            "role": "user",
            "content": None
        }
    
    def find_random_sample(self, df: pd.DataFrame):
        
        review_raw = df.sample()
        example = df.sample()
        if review_raw.index == example.index:
            example_idx = review_raw.index + random.randint(1, df.shape[0])
            example = df.loc[example_idx]
        
        review = review_raw["sentiment"]
  
        return review.item(), example["review"].item(), example["sentiment"].item()
        
    def sentiment_basic(self, review, review_truth, sentiment_truth):
        
        self.template["content"] = f"{review_truth} // {sentiment_truth}\nClassify the text into negative or positive,\
            the first word of your answer will be one of those. \nText: {review}\nSentiment:"

        return self.template