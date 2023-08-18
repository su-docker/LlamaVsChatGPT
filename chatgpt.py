from langchain.chat_models import ChatOpenAI
from mysecrets import OPENAI_KEY

class ChatGPTModel:
    
    def respond(self, question):
      print("Question to ChatGPT: ", question)
      chat_model = ChatOpenAI(openai_api_key=OPENAI_KEY)
      response = chat_model.predict(question)
      return response
