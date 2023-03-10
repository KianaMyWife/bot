from flask import Flask, request
import requests
import json
import random
import openai
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '在此输入apikey 样式:sk-s5S5BoV...'

openai.api_key = "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"  # 修改这里为自己申请的api_key

@app.route('/message')
def mess():  # put application's code here
    message = "你好"
    # openai.api_key = "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"  # 修改这里为自己申请的api_key
    messages = [
        {"role": "system", "content": "You are a coding tutor bot to help user write and optimize python code."},
        {"role": "user", "content": message}]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],

    )

    print(completion)
    messages.append({"role": "assistant", "content": completion.choices[0].message.content})
    res = {
        "resmsg": completion.choices[0].message.content,
        "code": 200
    }
    return res

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
