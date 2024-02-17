import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine import MemeGenerator
from QuoteEngine import Ingestor, DogQuotes
from PIL import Image
from io import BytesIO

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for i in quote_files:
        try:
            quotes.extend(Ingestor.parse(i))
        except ValueError as er:
            print(er)

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, text=quote.body, author=quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get("image_url")
    img_data = requests.get(image_url, allow_redirects=True, stream=True)


    if img_data.status_code == 200:
        img = "./temp/temp_image.jpg"

        image = Image.open(BytesIO(img_data.content))
        try:
            if image.mode != "RGB":
                image = image.convert("RGB")
        except OSError as e:
            print(f"can't open file -- {image.mode} -- {e}")

        image.save(img)
        # with open(img, "wb") as im:
        #     im.write(img_data.content)

        body = request.form.get("body","")
        author = request.form.get("author","")
        path = meme.make_meme(img, text=body, author=author)
        os.remove(img)
        return render_template('meme.html', path=path)
    else:
        raise ValueError('Failed to Download Image')
    

if __name__ == "__main__":
    app.run(debug=True)

