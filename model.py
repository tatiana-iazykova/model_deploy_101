from typing import Union, Tuple, Any, Dict

import joblib

from config import Config
from constants import CONFIG_PATH
from dto import Card
from utils import load_config


class Model:

    def __init__(self):
        self.config = Config(**load_config(CONFIG_PATH))
        self.model = joblib.load(self.config.model_path)
        self.thr = self.config.threshold
        self.template = self.config.template

    def predict(self, item_card: Card) -> int:

        text = self.template.format(item_card.Title, item_card.Description)
        pred = int(self.model.predict_proba([text])[0][1] > self.thr)

        return pred
