from .IngestorInterface import IngestorInterface
from .TXTImport import TxtImport
import subprocess
import os

class PdfImport(IngestorInterface):
    model_extentions =['pdf']

    @classmethod
    def parse(cls, path:str):
        if not cls.can_ingest(path):
            raise Exception('type not supported')

        temp = './temppdf.txt'
        call = subprocess.call(['pdftotext','-layout','-nopgbrk', path, temp])
        pdf_quotes=  TxtImport.parse(temp)
        os.remove(temp)
        return pdf_quotes




