import openai
from flask import Flask, render_template, request

openai.api_key = "<YOUR_API_KEY>"
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        donnees = request.form
        prompt = donnees.get('prompt')
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        return render_template("index.html", image_url=image_url)
    else:
        return render_template("index.html")