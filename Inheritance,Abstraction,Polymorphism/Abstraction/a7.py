from abc import ABC, abstractmethod
class Question(ABC):
    @abstractmethod
    def evaluate_answer(self):
        pass

class MCQ(Question):
    def evaluate_answer(self):
        print("Evaluating MCQ answer")

class TrueFalse(Question):
    def evaluate_answer(self):
        print("Evaluating True/False answer")

class Descriptive(Question):
    def evaluate_answer(self):
        print("Evaluating Descriptive answer")

q1 = MCQ()
q2 = TrueFalse()
q3 = Descriptive()
q1.evaluate_answer()
q2.evaluate_answer()
q3.evaluate_answer()