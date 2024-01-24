from .IngestorInterface import IngestorInterface
from .DOCXImport import DocxImport
from .PDFImport import PdfImport
from .CSVImport import CSVImport
from .TXTImport import TxtImport


class Ingestor(IngestorInterface):
    model_extentions = [DocxImport, PdfImport, CSVImport, TxtImport]

    @classmethod
    def parse(cls,path:str):
        for extention in cls.model_extentions:
            if extention.can_ingest(path):
                return extention.parse(path)