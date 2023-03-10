from .importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith(".json"):
            with open(path, "r") as file:
                return json.loads(file.read())
        else:
            raise ValueError("Arquivo inválido")
