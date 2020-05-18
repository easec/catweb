from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://stordevsumj.blob.core.windows.net/easec/cats%2Fcat1.gif",
    "https://stordevsumj.blob.core.windows.net/easec/cats%2Fcat2.gif",
    "https://stordevsumj.blob.core.windows.net/easec/cats%2Fcat3.gif?"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
