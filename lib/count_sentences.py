#!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if type(val) is not str:
            print("The value must be a string.")
        else:
            self._value = val

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        text = self.value.replace("!", ".").replace("?", ".")
        parts = text.split(".")
        sentences = [p.strip() for p in parts if p.strip()]
        return len(sentences)

