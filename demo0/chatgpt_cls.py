from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from mysecrets import OPENAI_KEY


chat_model = ChatOpenAI(openai_api_key=OPENAI_KEY)

response = chat_model.predict("Tell me briefly, why the ocean is blue?")
print(response)


