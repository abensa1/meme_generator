from .IngestorInterface import IngestorInterface
from .DogQuotes import DogQuotes
from docx import Document

class DocxImport(IngestorInterface):
    model_extentions =['docx']

    @classmethod
    def parse(cls, path:str):
        if not cls.can_ingest(path):
            raise Exception('type not supported')
    
        quotes =[]
        doc = Document(path)

        for row in doc.paragraphs:
            if row.text != "":
                row = row.text.split("-")
                quote = DogQuotes(
                    row[0],
                    row[1]
                )
                quotes.append(quote)

        return quotes




