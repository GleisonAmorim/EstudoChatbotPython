from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crie uma instância do ChatBot
bot = ChatBot('Meu Chatbot')

# Crie um treinador para treinar o chatbot usando os dados de treinamento em inglês
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

# Função para interagir com o chatbot
def get_response(input_text):
    response = bot.get_response(input_text)
    return str(response)