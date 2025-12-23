import yaml

# Fix for PyYAML compatibility with ChatterBot 1.0.4
# Newer PyYAML requires a Loader argument for security
_original_yaml_load = yaml.load
def _safe_yaml_load(data, Loader=yaml.SafeLoader):
    return _original_yaml_load(data, Loader=Loader)
yaml.load = _safe_yaml_load

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# Creating ChatBot Instance
CB = ChatBot('ChatBot')
 # Training with Personal Ques & Ans
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "You're welcome.",
    "who developed you",
    "I am developed by Saikat Sheet",
    "Do you know the birthday date of Saikat",
    "Yes, 9th January, 2002"
]
trainer = ListTrainer(CB)
trainer.train(conversation)
# # Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(CB)
trainer_corpus.train('chatterbot.corpus.english')
