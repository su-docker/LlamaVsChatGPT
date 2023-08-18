from flask import Flask, request, render_template
from chatgpt import ChatGPTModel
from llama import LlamaModel

app = Flask("LLMChatBot")

@app.post("/")
def reply():
    print("data", request.json["message"])
    return request.json["message"]

@app.get("/")
def index():
    return "Hello World!"

@app.get("/demo1")
def demo1():
    return render_template("demo1.html")

@app.post("/llama")
def llama():
    question = request.json["question"]
    print(question)
    model = LlamaModel()
    return model.respond(question)

@app.post("/chatgpt")
def chatgpt():
    question = request.json["question"]
    model = ChatGPTModel()
    return model.respond(question)