from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class LlamaModel:
  def respond(self, question):
    llm = Ollama(model="llama2", 
            base_url="http://localhost:11434", 
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
    return llm(question)

