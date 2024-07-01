from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from app.get_questions import Question_Sampler
import numpy as np


class MCQApp(App):

    def __init__(self, **kwargs):
        self.question_sampler = Question_Sampler()
        super().__init__(**kwargs)

    def build(self):
        self.title = 'Recall it!'
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.show_question()
        return self.layout

    def show_question(self):
        p1 = np.random.random()
        p2 = np.random.random()
        if p1 < 0.5:
            language = 'tamil'
        else:
            language = 'hindi'
        if p2 < 0.9:
            mode = 'mcq'
        else:
            mode = 'fill'

        question, answer, choices = self.question_sampler.get_question(
            language, mode)
        self.layout.clear_widgets()
        self.question_label = Label(text=f'{question}', font_size=24)
        self.layout.add_widget(self.question_label)
        for option in choices:
            btn = Button(text=option)
            btn.bind(on_release=lambda instance: self.check_answer(
                instance, answer, question if language == 'tamil' else answer))
            self.layout.add_widget(btn)

    def check_answer(self, instance, answer, tamil_word):
        if instance.text == answer:
            self.question_sampler.weights_obj.update_weights(
                {tamil_word: True})
            self.show_popup("Correct!", "You selected the correct answer.",
                            self.show_question)
        else:
            self.question_sampler.weights_obj.update_weights(
                {tamil_word: False})
            self.show_popup(
                "Wrong!",
                f"You selected the wrong answer. The correct answer is {answer}",
                self.show_question)

    def show_popup(self, title, message, callback):
        content = BoxLayout(orientation='vertical', padding=10)
        label = Label(text=message)
        close_btn = Button(text="Next", size_hint_y=None, height=50)
        content.add_widget(label)
        content.add_widget(close_btn)
        popup = Popup(title=title, content=content, size_hint=(0.6, 0.4))
        close_btn.bind(on_release=popup.dismiss)
        close_btn.bind(on_release=lambda *args: callback())
        popup.open()


if __name__ == '__main__':
    MCQApp().run()
