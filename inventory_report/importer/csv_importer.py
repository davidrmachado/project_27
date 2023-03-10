from .importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith(".csv"):
            with open(path, "r") as file:
                return [row for row in csv.DictReader(file)]
        else:
            raise ValueError("Arquivo inválido")
