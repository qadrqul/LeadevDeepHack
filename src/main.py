from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

chat = GigaChat(credentials="OWYzYzU1MzEtNGZhZi00ZDQxLWI2ODMtM2QxY2EyYTY5ZWEzOjhmOGNjMTAwLWUwOGUtNDgzZC1iZWFhLTcyMGE5YjY2YzAwZg==", verify_ssl_certs=False, scope="GIGACHAT_API_CORP")

messages = [
    SystemMessage(
        content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
    )
]

while(True):
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    print("Bot: ", res.content)