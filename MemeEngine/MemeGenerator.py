from PIL import Image, ImageFont, ImageDraw
import os

class MemeGenerator():

    def __init__(self, 
                 img_save_path: str = './output',
                 img_load_path: str = None,
                 text: str = "", 
                 author: str = "", 
                 width: int = 500, 
                 font_path: str = 'MemeEngine/font/Montserrat-SemiBold.ttf',
                 font_size: int = 16
                 ):
        
        self.img_load_path = img_load_path
        if self.img_load_path:
            self.load_image(self.img_load_path)

        self.img_save_path = img_save_path
        if not os.path.exists(img_save_path):
            os.makedirs(img_save_path)
        self.num =1


        self.text = text
        self.author = author
        self.width = int(width)
        self.font_path = font_path
        self.font_size= font_size
        self.image = None


    def load_image(self, load_path: str):
        try:
            self.image = Image.open(load_path)
        except:
            raise Exception("Image load failed")

    def resize_image(self, width):
        if (not width) and (not self.width):
            raise ValueError(f'you need to provide width')
        
        ratio = width/float(self.image.size[0])
        height = int(ratio*float(self.image.size[1]))
        self.image = self.image.resize((width, height))

    def add_font(self):
        return ImageFont.truetype(self.font_path, size=self.font_size)

    def add_caption_and_save(self, img_save_path):
        message = f'{self.text} - {self.author}'
        draw = ImageDraw.Draw(self.image)
        draw.text((10,30), message, font=self.add_font(), fill='black')
        meme_save_path = os.path.join(self.img_save_path,f"meme--{self.num}.jpg")
        self.num += 1
        self.image.save(meme_save_path)
        return meme_save_path

    def make_meme(self, img_load_path, text, author, img_save_path='./output', width=500):
        self.load_image(img_load_path)
        self.text = text
        self.author = author
        self.resize_image(width)

        return self.add_caption_and_save(img_save_path)