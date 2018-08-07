from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/13/enhanced/webdr11/anigif_enhanced-6320-1446488067-2.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-29111-1381845968-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr11/anigif_enhanced-19123-1446482575-20.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr09/anigif_enhanced-22830-1446482729-4.gif?"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
