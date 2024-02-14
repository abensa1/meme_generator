# Meme Engine

The modules contains and incorporates all the necessary models required for genereating memes

## How to use

- Import the 'Memegenerator' module class
- Run the main module by adding the image load path parameter like so:
```
meme = MemeGenerator('./temp')
```
- Once the class has been instantiated, you can run the 'make_meme' function to generate the meme with quotes:
```
path = meme.make_meme(img, text=quote.body, author=quote.author)
```
- the last step would be to return or print the 'path' of there the meme was saved
```
return path
```

## Librarires
The modules use the following open source libraries:
- [pillow]
- [os]