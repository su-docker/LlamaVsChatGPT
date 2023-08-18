from langchain.chat_models import ChatOpenAI
from mysecrets import OPENAI_KEY

class ChatGPTModel:
    
    def respond(self, question):
        chat_model = ChatOpenAI(openai_api_key=OPENAI_KEY)
        response = chat_model.predict(question)
        return response
