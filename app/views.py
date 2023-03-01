from app import app
from flask import render_template, request
import openai
import os

openai.api_key = os.getenv("OPENAI_API")
COMPLETIONS_MODEL = "text-davinci-002"
message = []
prompt_history = '''prompt: Imagine you are a German. You speak only German language. 
I will ask in english language. But you have to respond in German. '''



@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_msg = request.form["message"]
        gpt_msg = getgpt(user_msg)
        message.insert(0, "User: " + user_msg)
        message.insert(0, "GPT3: " + gpt_msg)
        print("message ", message)
    return render_template("home.html", message=message)


def getgpt(user_input):
    gpt_response = openai.Completion.create(
        prompt=prompt_history+user_input+'?',
        temperature=0,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model=COMPLETIONS_MODEL,
    )["choices"][0]["text"].strip(" \n")
    return gpt_response
