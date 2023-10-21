from flask import Flask, render_template, request, jsonify
import os
import openai
from dotenv import load_dotenv


from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


def configure():
    load_dotenv()


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def cha():
    msg = request.form["msg"]
    input = msg
    return chat(input)



def chat(text):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    return(response["choices"][0]["text"])


def main():
    configure()

if __name__ == '__main__':
    app.run()
