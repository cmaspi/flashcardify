import sys
import os
curr_path = os.path.dirname(__file__)
sys.path.append(curr_path)

from read_data import get_data
from repitition import exponential_decay_weight
import numpy as np


class Question_Sampler:
    dictionary = get_data()
    weights_obj = exponential_decay_weight()
    tamil_words = list(dictionary.keys())
    hindi_words = list(dictionary.values())

    def get_choices(self, choices_list, correct_answer):
        choices = np.random.choice(choices_list, 4, False)
        if correct_answer not in choices:
            choices[0] = correct_answer
        np.random.shuffle(choices)
        return choices

    def get_question(self, language='tamil', mode='mcq'):
        weights = np.array(self.weights_obj.get_weights(self.dictionary))
        weights /= weights.sum()
        tamil_word = np.random.choice(list(self.dictionary.keys()),
                                      1,
                                      False,
                                      p=weights)[0]
        hindi_word = self.dictionary[tamil_word]
        choices = []
        if language == 'tamil':
            question = tamil_word
            answer = hindi_word
            if mode == 'mcq':
                choices = self.get_choices(self.hindi_words, answer)
        else:
            question = hindi_word
            answer = tamil_word
            if mode == 'mcq':
                choices = self.get_choices(self.tamil_words, answer)
        return question, answer, choices
