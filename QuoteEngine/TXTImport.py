from .IngestorInterface import IngestorInterface
from .DogQuotes import DogQuotes

class TxtImport(IngestorInterface):
    model_extentions =['txt']

    @classmethod
    def parse(cls, path:str):
        if not cls.can_ingest(path):
            raise Exception('type not supported')
    
        quotes =[]
        file = open(path, 'r',encoding="utf-8-sig")
        
        for row in file.readlines():
            parsedrow = row.rstrip("\n").split(" - ")
            quote = DogQuotes(
                parsedrow[0],
                parsedrow[1]
            )
            quotes.append(quote)
            print(parsedrow)
        file.close()
        return quotes



