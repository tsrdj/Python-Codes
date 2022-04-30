from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import chatterBotCorpusTrainer
my_bot = ChatBot(name='PyBot',read_only=True,
                 logic_adapters=
                 ['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])
small_talks=['hi there!',
             'Namaste!',
             'how do you do?',
             'how are you?',
             'i\'m cool.',
             'i\'m ok',
             'glad to hear that.',
             'i\m fine.',
             'sorry to hear that.',
             'what\'s your name?',
             'i\'m pybot. ask me a math question, please.']
talk_1 = ['Best Instagram Account',
          'ts_rdj']
list_trainer = ListTrainer(my_bot)

for item in (small_talks, talk_1):
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

print(my_bot.get_response("Namaste"))
print(my_bot.get_response("I feel Awesome Today"))
print(my_bot.get_response("What your name"))
