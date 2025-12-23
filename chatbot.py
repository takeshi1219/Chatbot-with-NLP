import yaml
import nltk
import os

# Download required NLTK data
nltk_data_dir = os.path.join(os.path.dirname(__file__), 'nltk_data')
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.insert(0, nltk_data_dir)

for package in ['punkt', 'punkt_tab', 'averaged_perceptron_tagger', 
                'averaged_perceptron_tagger_eng', 'stopwords', 'wordnet']:
    try:
        nltk.data.find(f'tokenizers/{package}')
    except LookupError:
        try:
            nltk.data.find(f'taggers/{package}')
        except LookupError:
            try:
                nltk.data.find(f'corpora/{package}')
            except LookupError:
                nltk.download(package, download_dir=nltk_data_dir, quiet=True)

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
