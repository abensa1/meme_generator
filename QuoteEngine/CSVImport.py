from .IngestorInterface import IngestorInterface
from .DogQuotes import DogQuotes
import pandas as pd

class CSVImport(IngestorInterface):
    model_extentions =['csv']

    @classmethod
    def parse(cls, path:str):
        if not cls.can_ingest(path):
            raise Exception('type not supported')
    
        quotes =[]
        df = pd.read_csv(path, header=0)

        for index,row in df.iterrows():
            quote = DogQuotes(
                row['body'],
                row['author']
            )
            quotes.append(quote)
        
        return quotes




