import os
import random
import argparse

from QuoteEngine import Ingestor, DogQuotes
from MemeEngine import MemeGenerator


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]
    # print(img)
        
    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = DogQuotes(body, author)

    meme = MemeGenerator('./temp')
    path = meme.make_meme(img, text=quote.body, author=quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', type=str, 
                        default=None, help="path to an image")
    parser.add_argument('-b','--body', type=str, 
                        default=None, help="body path")
    parser.add_argument('-a','--author', type=str, default=None, help="Author name written to image.")
    args = parser.parse_args()
    generate_meme(args.path, args.body, args.author)
