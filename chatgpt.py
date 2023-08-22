from langchain.chat_models import ChatOpenAI
from openai.error import AuthenticationError
from mysecrets import OPENAI_KEY

class ChatGPTModel:
    
    def respond(self, question):
      try:
        print("Question to ChatGPT: ", question)
        chat_model = ChatOpenAI(openai_api_key=OPENAI_KEY)
        response = chat_model.predict(question)
        return response
      except AuthenticationError:
         return "Looks like your openai key is not valid. Please check"
