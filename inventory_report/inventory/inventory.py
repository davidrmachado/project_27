from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        if path.endswith(".csv"):
            with open(path, 'r') as csv_archive:
                dict = csv.DictReader(csv_archive)
                data = list(dict)

                return Inventory.generate_report(data, report_type)

        elif path.endswith(".json"):
            with open(path, "r") as json_archive:
                data = json.load(json_archive)

                return Inventory.generate_report(data, report_type)

        elif path.endswith(".xml"):
            with open(path, 'r') as xml_file:
                data_xml = xmltodict.parse(xml_file.read())
                data = data_xml["dataset"]["record"]

                return Inventory.generate_report(data, report_type)

    @staticmethod
    def generate_report(data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)

        elif report_type == "completo":
            return CompleteReport.generate(data)
