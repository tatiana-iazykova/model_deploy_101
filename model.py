from typing import Union, Tuple

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class Model:

    def __init__(self):
        model_checkpoint = 'cointegrated/rubert-tiny-sentiment-balanced'
        self.tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
        if torch.cuda.is_available():
            self.model.cuda()
        self.model = self.model.eval()

    def predict(self, text: str, return_proba: bool) -> Union[str, Tuple[str, float]]:
        with torch.inference_mode():
            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True).to(self.model.device)
            proba = torch.sigmoid(self.model(**inputs).logits).cpu().numpy()[0]

        if return_proba:
            return self.model.config.id2label[proba.argmax()], proba.max().item()

        return self.model.config.id2label[proba.argmax()]
