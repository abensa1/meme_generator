from abc import ABC, abstractclassmethod

class IngestorInterface(ABC):
    model_extentions= []


    @classmethod
    def can_ingest(cls, path:str ) -> bool:
        mod = path.split('.')[-1]
        return mod in cls.model_extentions

    @classmethod
    @abstractclassmethod
    def parse(cls, path:str) -> list:
        pass