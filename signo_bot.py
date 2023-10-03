import openai

# Configure a sua chave de API do OpenAI
openai.api_key = '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'

def enviar_mensagem(conversa_atual):
    resposta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=conversa_atual,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return resposta.choices[0].text.strip()

# Conversa inicial
conversa_anterior = """
Você: Olá, como posso te ajudar?
Bot: Eu sou um assistente virtual treinado para responder suas perguntas sobre signos.
Você: Qual é o seu nome?
Bot: Meu nome é SignoBot. Como posso ajudar hoje?
"""

# Mensagem do usuário (substitua por mensagens dos usuários)
mensagem_usuario = "Diga-me sobre o signo de Áries."

# Construa a conversa atual
conversa_atual = conversa_anterior + 'Você: ' + mensagem_usuario

# Obtenha a resposta do bot
resposta = enviar_mensagem(conversa_atual)
print(f'Resposta do SignoBot: {resposta}')