# Assistente de Viagem Conversacional com LangChain e Ollama

Este projeto implementa um Assistente de Viagem inteligente e conversacional, utilizando o framework LangChain e o servidor local Ollama para rodar o modelo de linguagem Llama3:8b. O assistente é projet projetado para ajudar os usuários a planejar suas viagens, oferecendo sugestões de destinos, roteiros e dicas práticas, tudo isso enquanto mantém o contexto da conversa.

## Visão Geral

A construção de assistentes de IA que mantêm um histórico de conversa e atuam em um papel específico é uma aplicação poderosa dos LLMs. Este projeto demonstra:
1.  **Integração LangChain + Ollama:** Como conectar o LangChain a um modelo de linguagem que está sendo executado localmente via Ollama.
2.  **Modelagem de Papel (Role-Playing):** O sistema é instruído a agir como um "Assistente de Viagem", com uma diretriz inicial clara para coletar informações essenciais sobre a viagem.
3.  **Histórico de Conversa:** Utilização do `RunnableWithMessageHistory` para que o assistente "lembre" das interações anteriores na mesma sessão, permitindo um diálogo mais fluido e contextualizado.
4.  **Interface de Linha de Comando:** Uma interface simples baseada em texto para interagir com o assistente.

## Estrutura do Projeto

* `app.py`: O script Python principal que contém a lógica do assistente, a configuração do LangChain e a interação com Ollama.
* `requirements.txt`: Lista as dependências Python necessárias para o projeto.
* `.env`: (Opcional, mas recomendado) Arquivo para armazenar variáveis de ambiente, como API keys, se o projeto for expandido para incluir outros serviços.

## Tecnologias Utilizadas

* **Python 3**
* **LangChain**: Framework para orquestrar LLMs e construir aplicações de IA.
    * `langchain-community`: Para modelos de chat (ChatOllama) e histórico de mensagens.
    * `langchain-core`: Para prompts e runnables.
* **Ollama**: Plataforma para executar LLMs localmente.
* **Llama3:8b**: Modelo de linguagem grande da Meta (você pode usar outro modelo Llama3 se preferir).
* **`python-dotenv`**: Para carregar variáveis de ambiente (se usadas).
* **`requests`**: (Indiretamente, via `langchain-community`) Para comunicação HTTP com o servidor Ollama.

## Pré-requisitos

Antes de executar este projeto, você precisa ter o Ollama instalado e o modelo `llama3:8b` baixado.

1.  **Instale o Ollama:** Siga as instruções de instalação em [https://ollama.com/](https://ollama.com/).
2.  **Baixe o modelo Llama3:8b:** Abra seu terminal e execute:
    ```bash
    ollama pull llama3:8b
    ```
    Certifique-se de que o servidor Ollama esteja em execução em segundo plano (geralmente ele inicia automaticamente após a instalação e ao baixar um modelo).

## Interagindo com o Assistente

Ao executar `app.py`, você verá a mensagem de boas-vindas e poderá começar a conversar com o Assistente de Viagem.

**Exemplo de interação:**

```
Bem-vindo ao Assistente de Viagem! Digite 'sair' para encerrar.

Você: Olá!

Assistente de Viagem: Olá! Para onde você está planejando ir, com quantas pessoas e por quanto tempo?

Você: Vamos para Paris, eu e mais três amigos, por 7 dias.

Assistente de Viagem: Ótimo! Paris é uma escolha fantástica. Com 4 pessoas por 7 dias, podemos montar um roteiro inesquecível. Você tem alguma preferência de atividades (cultura, gastronomia, compras, etc.) ou algum bairro em mente?

Você: Queremos ver os principais pontos turísticos.

Assistente de Viagem: Excelente! Em 7 dias, vocês podem conhecer os pontos turísticos mais icônicos de Paris. Sugiro um roteiro que inclua a Torre Eiffel, o Museu do Louvre, a Catedral de Notre-Dame, e talvez um passeio de barco pelo Sena. Querem que eu detalhe um dia específico ou prefere dicas gerais?

Você: sair

Sessão encerrada. Até logo!
```
