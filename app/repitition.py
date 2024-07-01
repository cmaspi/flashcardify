import os
import pickle
from collections import defaultdict
import numpy as np

curr_path = os.path.dirname(__file__)


class exponential_decay_weight:

    def __init__(self) -> None:
        self.weights = defaultdict(lambda: 1)
        if os.path.exists(f"{curr_path}/../data/saved_weights.pkl"):
            with open(f"{curr_path}/../data/saved_weights.pkl", 'rb') as f:
                temp_weights = pickle.load(f)
            for w, v in temp_weights.items():
                self.weights[w] = v
        with open(f"{curr_path}/../data/saved_weights.pkl", 'wb') as f:
            pickle.dump(dict(self.weights), f)

    def get_weights(self, dictionary):
        return np.array([self.weights[w] for w in dictionary.keys()],
                        dtype=np.float64)

    def update_weights(self, history):
        for w, v in history.items():
            if v is False:
                self.weights[w] = 1
            else:
                self.weights[w] /= 2
        with open(f"{curr_path}/../data/saved_weights.pkl", 'wb') as f:
            pickle.dump(dict(self.weights), f)
