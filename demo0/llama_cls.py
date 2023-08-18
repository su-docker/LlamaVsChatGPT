from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = Ollama(model="llama2", 
            base_url="http://localhost:11434", 
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

llm("Tell me briefly, why the ocean is blue?")

