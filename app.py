import openai
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
from gtts import gTTS
from playsound import playsound
import random

app = Flask(__name__)

openai.api_key = 'GPTChatAPIkey'


def t2s(text):
    tts = gTTS(text, lang='en', tld='co.uk')
    ran = str(random.randint(0, 2000000))
    tts.save(f"audio{ran}.mp3")
    return playsound(f"audio{ran}.mp3", False)



def gpt_chat(user_input):
    chatgpt_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_input,
        temperature=0.4,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=1,
        presence_penalty=0
    )
    return chatgpt_response["choices"][0]["text"]


@app.route('/')
def render_index_html():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def render_chat_with_chatgpt():
    user_input = request.form['text']
    out = gpt_chat(user_input)
    talk = t2s(out)
    return out, talk

if __name__ == '__main__':
    app.run()
