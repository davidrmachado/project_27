from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith(".xml"):
            with open(path, "r") as file:
                return xmltodict.parse(file.read())["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
