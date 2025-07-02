import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

template = """Você é um Assistente de Viagem que ajuda o usuário a planejar viagens,
dando sugestões de destinos, roteiros e dicas práticas.
A primeira coisa que deve fazer é perguntar para onde o usuário vai, com quantas pessoas e por quanto tempo.
Responda sempre em português-br.

Histórico de mensagens:
{history}

Entrada do usuário:
{input}"""

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    MessagesPlaceholder(variable_name="history"), # Placeholder for chat history
    ("human", "{input}"),
])

llm = ChatOllama(
    model="llama3:8b",
    temperature=0.7
)

chain = prompt | llm

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

def start_travel_assistant():
    print("Bem-vindo ao Assistente de Viagem! Digite 'sair' para encerrar.\n")
    while True:
        user_question = input("Você: ")
        
        if user_question.lower() in ["sair", "exit"]:
            print("Sessão encerrada. Até logo!")
            break
        
        resposta = chain_with_history.invoke(
            {'input': user_question},
            config={'configurable': {'session_id': 'user123'}}
        )
        
        print("Assistente de Viagem:", resposta.content)
        
if __name__ == "__main__":
    start_travel_assistant()